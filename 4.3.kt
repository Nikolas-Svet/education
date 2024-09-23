class Vector(private val x: Double, private val y: Double, private val z: Double) {

    // Метод для вычисления длины вектора
    fun length(): Double {
        return Math.sqrt(x * x + y * y + z * z)
    }

    // Метод для вычисления скалярного произведения с другим вектором
    infix fun dot(other: Vector): Double {
        return x * other.x + y * other.y + z * other.z
    }

    // Инфиксная функция для удобного вызова
    operator fun times(other: Vector): Double {
        return this dot other
    }
}

fun main() {
    val vector1 = Vector(1.0, 2.0, 3.0)
    val vector2 = Vector(4.0, 5.0, 6.0)

    println("Длина вектора 1: ${vector1.length()}")
    println("Скалярное произведение: ${vector1 * vector2}")
}
