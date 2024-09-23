class Car(var name: String, var speed: Int)

data class Vehicle(var name: String, var speed: Int)

fun main() {
    // Создание объектов Car
    val car1 = Car("Lada", 100)
    val car2 = Car("Lada", 100)

    // Сравнение car1 и car2
    println("car1 == car2: ${car1 == car2}") // Сравнение значений
    println("car1 === car2: ${car1 === car2}") // Сравнение ссылок
    println("car1 hashCode: ${car1.hashCode()}")
    println("car2 hashCode: ${car2.hashCode()}")

    // Создание объекта car3
    val car3 = car1
    println("car1 == car3: ${car1 == car3}") // Сравнение значений
    println("car1 === car3: ${car1 === car3}") // Сравнение ссылок
    println("car1 hashCode: ${car1.hashCode()}")
    println("car3 hashCode: ${car3.hashCode()}")

    // Изменение свойства name
    car3.name = "Belaz"
    println("car1 name: ${car1.name}, car3 name: ${car3.name}")

    // Создание объектов Vehicle
    val vehicle1 = Vehicle("Ural", 100)
    val vehicle2 = Vehicle("Ural", 100)

    // Сравнение vehicle1 и vehicle2
    println("vehicle1 == vehicle2: ${vehicle1 == vehicle2}") // Сравнение значений
    println("vehicle1 === vehicle2: ${vehicle1 === vehicle2}") // Сравнение ссылок
    println("vehicle1 hashCode: ${vehicle1.hashCode()}")
    println("vehicle2 hashCode: ${vehicle2.hashCode()}")

    // Создание копий vehicle1
    val vehicle3 = vehicle1.copy("ZIL")
    val vehicle4 = vehicle1.copy()

    // Сравнение vehicle3 и vehicle1
    println("vehicle3 == vehicle1: ${vehicle3 == vehicle1}") // Сравнение значений
    println("vehicle3 === vehicle1: ${vehicle3 === vehicle1}") // Сравнение ссылок

    // Сравнение vehicle4 и vehicle1
    println("vehicle4 == vehicle1: ${vehicle4 == vehicle1}") // Сравнение значений
    println("vehicle4 === vehicle1: ${vehicle4 === vehicle1}") // Сравнение ссылок
}
