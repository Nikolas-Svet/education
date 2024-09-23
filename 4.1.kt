class NumberArray(private val numbers: IntArray) {

    // Метод для вычисления суммы положительных элементов
    fun sumOfPositive(): Int {
        return numbers.filter { it > 0 }.sum()
    }

    // Метод для вычисления произведения всех элементов массива
    fun product(): Int {
        return numbers.fold(1) { acc, num -> acc * num }
    }

    // Метод для вычисления среднего арифметического
    fun average(): Double {
        return numbers.average()
    }
}

fun main() {
    val numberArray = NumberArray(intArrayOf(1, -2, 3, 4, -5))

    println("Сумма положительных элементов: ${numberArray.sumOfPositive()}")
    println("Произведение элементов массива: ${numberArray.product()}")
    println("Среднее арифметическое значение: ${numberArray.average()}")
}
