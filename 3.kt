fun main() {
    println("Введите коэффициенты a, b и c для квадратного уравнения ax^2 + bx + c = 0:")

    val a = readLine()?.toDoubleOrNull() ?: return
    val b = readLine()?.toDoubleOrNull() ?: return
    val c = readLine()?.toDoubleOrNull() ?: return

    quadraticRoot(a, b, c)
}

fun sqr(n: Double): Double {
    return n * n
}

fun discriminant(a: Double, b: Double, c: Double): Double {
    return sqr(b) - 4 * a * c
}

fun rootsNumber(a: Double, b: Double, c: Double): Int {
    val d = discriminant(a, b, c)
    return when {
        d > 0 -> 2 // два различных корня
        d == 0.0 -> 1 // один корень
        else -> 0 // нет корней
    }
}

fun quadraticRoot(a: Double, b: Double, c: Double) {
    val numRoots = rootsNumber(a, b, c)
    when (numRoots) {
        2 -> {
            val d = discriminant(a, b, c)
            val root1 = (-b + Math.sqrt(d)) / (2 * a)
            val root2 = (-b - Math.sqrt(d)) / (2 * a)
            println("Два корня: x1 = $root1, x2 = $root2")
        }
        1 -> {
            val root = -b / (2 * a)
            println("Один корень: x = $root")
        }
        0 -> println("Нет корней")
    }
}
