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
        # Recolectar constantes Y copias simples (var = var/temporal)
        valores = {}
        for linea in codigo:
            linea_strip = linea.strip()
            # var = numero  O  var = otraVar/temporal
            m = re.match(r'^([A-Za-z_]\w*)\s*=\s*([A-Za-z_]\w*|-?\d+\.?\d*)$', linea_strip)
            if m:
                var = m.group(1)
                val = m.group(2)
                valores[var] = val

        if not valores:
            return codigo, False

        cambio = False
        resultado = []
        instrucciones_control = ('if', 'goto', 'FUNC', 'END', 'param', 'pop', 'return', 'DECLARE')

        for linea in codigo:
            linea_strip = linea.strip()

            if any(linea_strip.startswith(k) for k in instrucciones_control):
                resultado.append(linea)
                continue
            if linea_strip.endswith(':'):
                resultado.append(linea)
                continue

            if '=' in linea_strip:
                partes = linea_strip.split('=', 1)
                lado_izq = partes[0].strip()
                lado_der = partes[1].strip()

                nuevo_der = lado_der
                for var, val in valores.items():
                    nuevo_der = re.sub(rf'\b{re.escape(var)}\b', val, nuevo_der)

                if nuevo_der != lado_der:
                    nueva_linea = f"{lado_izq} = {nuevo_der}"
                    self.reporte.append(f"Propagación: {linea_strip} → {nueva_linea}")
                    resultado.append(nueva_linea)
                    cambio = True
                else:
                    resultado.append(linea)
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

                if expr in expresiones_vistas:
                    temp_anterior = expresiones_vistas[expr]
                    nueva_linea = f"{temp} = {temp_anterior}"
                    self.reporte.append(
                        f"Eliminación de repetidas: {linea_strip} → {nueva_linea}"
                    )
                    resultado.append(nueva_linea)
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