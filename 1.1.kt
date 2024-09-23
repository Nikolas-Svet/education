fun main(args: Array<String>) {
    println("Введите целое положительное число:")
    val input = readln()

    // Способ 1: преобразование строки в число
    val firstDigit = input.first().digitToInt()
    val lastDigit = input.last().digitToInt()
    val sum = firstDigit + lastDigit

    println("Сумма первой и последней цифры: $sum")
}