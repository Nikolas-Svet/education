fun main() {
    println("Введите количество простых чисел n:")
    val n = readLine()?.toIntOrNull() ?: return

    var count = 0
    var num = 2

    while (count < n) {
        if (isPrime(num)) {
            count++
            println("$count-ое число: $num")
        }
        num++
    }
}

fun isPrime(number: Int): Boolean {
    if (number < 2) return false
    for (i in 2..Math.sqrt(number.toDouble()).toInt()) {
        if (number % i == 0) return false
    }
    return true
}
