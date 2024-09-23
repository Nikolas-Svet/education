fun main() {
    val randomNumber = (0..10).random()
    var guessed = false

    println("Угадайте число от 0 до 10:")

    while (!guessed) {
        val userGuess = readln().toInt()

        when {
            userGuess > randomNumber -> println("Много")
            userGuess < randomNumber -> println("Мало")
            else -> {
                println("Угадал!")
                guessed = true
            }
        }
    }
}
