import re


class Optimizador:

    def __init__(self, codigo):
        self.codigo = codigo[:]
        self.reporte = []

    def optimizar(self):
        cambio = True
        iteracion = 0
        while cambio and iteracion < 10:
            cambio = False
            iteracion += 1

            nuevo, c1 = self.propagacion_constantes(self.codigo)
            if c1:
                self.codigo = nuevo
                cambio = True

            nuevo, c2 = self.eliminacion_repetidas(self.codigo)
            if c2:
                self.codigo = nuevo
                cambio = True

        return self.codigo

        # ==========================================
        # 1) PROPAGACIÓN DE CONSTANTES
        # ==========================================

    def propagacion_constantes(self, codigo):

        valores = {}
        resultado = []
        cambio = False

        instrucciones_control = (
            'if', 'goto', 'FUNC', 'END',
            'param', 'pop', 'return', 'DECLARE'
        )

        for linea in codigo:

            linea_strip = linea.strip()

            # No tocar instrucciones de control
            if any(linea_strip.startswith(k) for k in instrucciones_control):
                resultado.append(linea)
                 # Después de un salto ya no sabemos las constantes
                if linea_strip.startswith("if") or linea_strip.startswith("goto"):
                    valores.clear()

                continue

            # No tocar etiquetas
            if linea_strip.endswith(':'):
                resultado.append(linea)
                 # Comienza una nueva región de código
                valores.clear()

                continue

            # Asignaciones
            if '=' in linea_strip:

                lado_izq, lado_der = map(str.strip, linea_strip.split('=', 1))

                # Reemplazar usando las constantes conocidas hasta aquí
                nuevo_der = lado_der

                for var, val in valores.items():
                    nuevo_der = re.sub(
                        rf'\b{re.escape(var)}\b',
                        val,
                        nuevo_der
                    )
                # Constant Folding
                try:
                    if re.fullmatch(r'[-+*/(). 0-9]+', nuevo_der):
                        nuevo_der = str(eval(nuevo_der))
                except:
                    pass

                if nuevo_der != lado_der:
                    cambio = True
                    self.reporte.append(
                        f"Propagación: {linea_strip} → {lado_izq} = {nuevo_der}"
                    )

                resultado.append(f"{lado_izq} = {nuevo_der}")

               # Actualizar tabla de constantes

                # Si quedó un número
                if re.fullmatch(r'-?\d+(\.\d+)?', nuevo_der):
                    valores[lado_izq] = nuevo_der

                # Si quedó una variable o temporal
                elif re.fullmatch(r'[A-Za-z_]\w*', nuevo_der):

                    # Si conocemos el valor de esa variable, copiar el valor
                    if nuevo_der in valores:
                        valores[lado_izq] = valores[nuevo_der]
                    else:
                        valores[lado_izq] = nuevo_der

                # Si es una expresión más compleja, dejar de considerarla constante
                else:
                    valores.pop(lado_izq, None)

            else:
                resultado.append(linea)

        return resultado, cambio

    # ==========================================
    # 2) ELIMINACIÓN DE ACCIONES REPETIDAS
    # ==========================================

    def eliminacion_repetidas(self, codigo):
        expresiones_vistas = {}
        cambio = False
        resultado = []

        for linea in codigo:
            linea_strip = linea.strip()

            m = re.match(r'^(t\d+)\s*=\s*(.+)$', linea_strip)
            if m:
                temp = m.group(1)
                expr = m.group(2).strip()

                if 'call' in expr:
                    expresiones_vistas[temp] = expr
                    resultado.append(linea)
                elif expr in expresiones_vistas:
                    temp_anterior = expresiones_vistas[expr]
                    # En vez de emitir t1 = t0, reemplazamos t1 por t0
                    # en todas las líneas ya emitidas y marcamos cambio
                    resultado = [
                        re.sub(rf'\b{re.escape(temp)}\b', temp_anterior, l)
                        for l in resultado
                    ]
                    # No agregamos esta línea — la eliminamos
                    self.reporte.append(
                        f"Eliminación de repetidas: {linea_strip} → eliminada, usos reemplazados por {temp_anterior}"
                    )
                    cambio = True
                else:
                    expresiones_vistas[expr] = temp
                    resultado.append(linea)
            else:
                resultado.append(linea)

        return resultado, cambio

    # ==========================================
    # REPORTE
    # ==========================================

    def imprimir_reporte(self, original, optimizado):
        print("\n===== OPTIMIZACIONES APLICADAS =====")
        if self.reporte:
            for r in self.reporte:
                print(" -", r)
        else:
            print(" (ninguna optimización aplicada)")

        print("\n===== COMPARACIÓN =====")
        print(f" Líneas originales:   {len(original)}")
        print(f" Líneas optimizadas:  {len(optimizado)}")
        print(f" Líneas eliminadas:   {len(original) - len(optimizado)}")
        if len(original) > 0:
            porcentaje = (1 - len(optimizado) / len(original)) * 100
            print(f" Reducción:           {porcentaje:.1f}%")
        print("=" * 40)