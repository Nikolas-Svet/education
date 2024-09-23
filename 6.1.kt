abstract class Figure {
    abstract fun area(): Double
    abstract fun perimeter(): Double
}

class Square(private val side: Double) : Figure() {
    override fun area(): Double {
        return side * side
    }

    override fun perimeter(): Double {
        return 4 * side
    }
}

class Circle(private val radius: Double) : Figure() {
    override fun area(): Double {
        return Math.PI * radius * radius
    }

    override fun perimeter(): Double {
        return 2 * Math.PI * radius
    }
}

class Triangle(private val a: Double, private val b: Double, private val c: Double) : Figure() {
    override fun area(): Double {
        val s = perimeter() / 2
        return Math.sqrt(s * (s - a) * (s - b) * (s - c))
    }

    override fun perimeter(): Double {
        return a + b + c
    }
}

fun main() {
    val square = Square(4.0)
    println("Квадрат: площадь = ${square.area()}, периметр = ${square.perimeter()}")

    val circle = Circle(3.0)
    println("Окружность: площадь = ${circle.area()}, периметр = ${circle.perimeter()}")

    val triangle = Triangle(3.0, 4.0, 5.0)
    println("Треугольник: площадь = ${triangle.area()}, периметр = ${triangle.perimeter()}")
}

