fun arrayStatsFor(arr: IntArray) {
    var product = 1
    var min = arr[0]
    var max = arr[0]

    for (number in arr) {
        product *= number
        if (number < min) min = number
        if (number > max) max = number
    }

    println("Произведение: $product, Min: $min, Max: $max")
}

fun arrayStatsWhile(arr: IntArray) {
    var product = 1
    var min = arr[0]
    var max = arr[0]
    var i = 0

    while (i < arr.size) {
        product *= arr[i]
        if (arr[i] < min) min = arr[i]
        if (arr[i] > max) max = arr[i]
        i++
    }

    println("Произведение: $product, Min: $min, Max: $max")
}

fun arrayStatsReduce(arr: IntArray) {
    val product = arr.reduce { acc, number -> acc * number }
    val min = arr.minOrNull() ?: return
    val max = arr.maxOrNull() ?: return

    println("Произведение: $product, Min: $min, Max: $max")
}

fun arrayStatsForEach(arr: IntArray) {
    var product = 1
    var min = arr[0]
    var max = arr[0]

    arr.forEach { number ->
        product *= number
        if (number < min) min = number
        if (number > max) max = number
    }

    println("Произведение: $product, Min: $min, Max: $max")
}
