fun main() {
    val words: List<String?> = listOf("hello", null, "world", "kotlin", null)

    // Используя оператор if
    println("Используя оператор if:")
    for (word in words) {
        if (word != null) {
            println(word.toUpperCase())
        }
    }

    // Используя оператор безопасного вызова ?
    println("\nИспользуя оператор безопасного вызова:")
    for (word in words) {
        word?.let { println(it.toUpperCase()) }
    }

    // Используя функцию let
    println("\nИспользуя функцию let:")
    for (word in words) {
        word?.let { println(it.toUpperCase()) }
    }

    // Используя Элвис-оператор ?:
    println("\nИспользуя Элвис-оператор:")
    for (word in words) {
        println((word ?: "empty").toUpperCase())
    }
}
