enum class Command {
    UP, DOWN, LEFT, RIGHT
}

class Point(var x: Int, var y: Int) {
    override fun toString(): String {
        return "Текущие координаты: ($x, $y)"
    }
}

class Turtle {
    fun move(point: Point, command: Command) {
        when (command) {
            Command.UP -> {
                println("Произведено перемещение по оси X на 0, по оси Y на 1")
                point.y += 1
            }
            Command.DOWN -> {
                println("Произведено перемещение по оси X на 0, по оси Y на -1")
                point.y -= 1
            }
            Command.LEFT -> {
                println("Произведено перемещение по оси X на -1, по оси Y на 0")
                point.x -= 1
            }
            Command.RIGHT -> {
                println("Произведено перемещение по оси X на 1, по оси Y на 0")
                point.x += 1
            }
        }
    }
}

fun main() {
    val point = Point(0, 0)
    val turtle = Turtle()

    // Примеры перемещений
    turtle.move(point, Command.UP)
    println(point)

    turtle.move(point, Command.RIGHT)
    println(point)

    turtle.move(point, Command.DOWN)
    println(point)

    turtle.move(point, Command.LEFT)
    println(point)
}
