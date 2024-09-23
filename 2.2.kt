fun findGreaterThanNeighbors(arr: IntArray) {
    for (i in 1 until arr.size - 1) {
        if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
            println(arr[i])
        }
    }
}


fun findGreaterThanNeighborsWhile(arr: IntArray) {
    var i = 1
    while (i < arr.size - 1) {
        if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
            println(arr[i])
        }
        i++
    }
}

fun findGreaterThanNeighborsForEach(arr: IntArray) {
    arr.forEachIndexed { index, value ->
        if (index > 0 && index < arr.size - 1 && value > arr[index - 1] && value > arr[index + 1]) {
            println(value)
        }
    }
}

