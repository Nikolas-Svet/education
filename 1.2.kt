fun main(args: Array<String>) {
    var count = 0
    var sum = 0

    println("Введите числа (введите 0 для завершения):")

    while (true) {
        val input = readln().toInt()
        if (input == 0) break
        count++
        sum += input
    }

    val average = if (count > 0) sum.toDouble() / count else 0.0

    println("Количество введенных чисел: $count")
    println("Общая сумма: $sum")
    println("Среднее арифметическое: $average")
}