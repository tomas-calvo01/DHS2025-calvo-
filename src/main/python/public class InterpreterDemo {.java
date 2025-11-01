public class InterpreterDemo {

    static class Context {
    }

    static abstract class Expression {
        abstract int interpret(Context ctx);
    }

    static class NumberExpr extends Expression {
        private final int value;
        NumberExpr(int value) { this.value = value; }
        @Override
        int interpret(Context ctx) {
            return value;
        }
    }

    static class Add extends Expression {
        private final Expression left;
        private final Expression right;
        Add(Expression left, Expression right) {
            this.left = left;
            this.right = right;
        }
        @Override
        int interpret(Context ctx) {
            return left.interpret(ctx) + right.interpret(ctx);
        }
    }

    static class Subtract extends Expression {
        private final Expression left;
        private final Expression right;
        Subtract(Expression left, Expression right) {
            this.left = left;
            this.right = right;
        }
        @Override
        int interpret(Context ctx) {
            return left.interpret(ctx) - right.interpret(ctx);
        }
    }

    public static void main(String[] args) {
        Context ctx = new Context();
        Expression expr = new Subtract(
                new Add(new NumberExpr(3), new NumberExpr(5)),
                new NumberExpr(2)
        );
        int resultado = expr.interpret(ctx);
        System.out.println("Resultado: " + resultado);
    }
}
