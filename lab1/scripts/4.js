function ex4() {
    document.getElementById("four").style.display = 'flex';
}

const students = [
    ["Иванов", "Иван", 2, "01"],
    ["Петров", "Петр", 3, "02"],
    ["Сидоров", "Сергей", 1, "01"],
    ["Кузнецов", "Николай", 4, "03"],
    ["Смирнова", "Елена", 2, "02"],
    ["Васильева", "Анна", 3, "01"]
];

function getStudents() {
    const directionCode = document.getElementById("directionCode").value;
    const studentList = document.getElementById("studentList");
    studentList.innerHTML = ""; // Очищаем список перед выводом

    students.forEach(student => {
        const [lastName, firstName, course, code] = student;

        if (code === directionCode) {
            const listItem = document.createElement("li");
            listItem.textContent = `${lastName} ${firstName}, Курс: ${course}, Код направления: ${code}`;
            studentList.appendChild(listItem);
        } else {
            console.log(`Другие направления: ${lastName} ${firstName}, Курс: ${course}, Код направления: ${code}`);
        }
    });

    if (studentList.innerHTML === "") {
        const listItem = document.createElement("li");
        listItem.textContent = "Студенты с таким кодом направления не найдены.";
        studentList.appendChild(listItem);
    }
}