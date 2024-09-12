let students = [
    ["Иванов", "Иван", "Иванович", 1, "123"],
    ["Петров", "Петр", "Петрович", 2, "456"],
    ["Сидоров", "Алексей", "Алексеевич", 3, "789"],
    ["Смирнов", "Сергей", "Сергеевич", 4, "321"],
    ["Кузнецов", "Андрей", "Андреевич", 5, "654"],
    ["Попов", "Александр", "Александрович", 6, "987"]
];

function ex7() {
    document.getElementById("seven").style.display = 'flex';
}
function findDirection() {
    let code = prompt("Введите код направления:");

    console.log("Студенты с кодом направления:", code);
    students.forEach(student => {
        if (student[4] === code) {
            alert(`ФИО: ${student[0]} ${student[1]} ${student[2]}, Класс: ${student[3]}`);
        } else {
            console.log(`Другие студенты: ${student[0]} ${student[1]} ${student[2]}, Класс: ${student[3]}`);
        }
    });
}
