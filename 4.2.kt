class EnhancedArray(private val numbers: IntArray) {

    // Метод для получения массива с удвоенными четными и утроенными нечетными элементами
    fun modifiedArray(): IntArray {
        return numbers.map { if (it % 2 == 0) it * 2 else it * 3 }.toIntArray()
    }

    // Метод для получения максимального элемента
    fun maxElement(): Int? {
        return numbers.maxOrNull()
    }

    // Метод для получения минимального элемента
    fun minElement(): Int? {
        return numbers.minOrNull()
    }

    // Свойство для получения суммы элементов массива
    val sum: Int
        get() = numbers.sum()
}

fun main() {
    val enhancedArray = EnhancedArray(intArrayOf(1, 2, 3, 4, 5))

    println("Модифицированный массив: ${enhancedArray.modifiedArray().joinToString()}")
    println("Максимальный элемент: ${enhancedArray.maxElement()}")
    println("Минимальный элемент: ${enhancedArray.minElement()}")
    println("Сумма элементов массива: ${enhancedArray.sum}")
}
