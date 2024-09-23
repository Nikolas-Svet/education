fun main() {
    println("Введите первое число:")
    val firstNumber = readLine()?.toDoubleOrNull()

    println("Введите второе число:")
    val secondNumber = readLine()?.toDoubleOrNull()

    println("Введите знак операции (+, -, *, /):")
    val operation = readLine()

    if (firstNumber != null && secondNumber != null) {
        val result = when (operation) {
            "+" -> firstNumber + secondNumber
            "-" -> firstNumber - secondNumber
            "*" -> firstNumber * secondNumber
            "/" -> if (secondNumber != 0.0) firstNumber / secondNumber else "Деление на ноль"
            else -> "Неверный знак операции"
        }
        println("Результат: $result")
    } else {
        println("Некорректный ввод чисел.")
    }
}
