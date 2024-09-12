function ex2() {
        document.getElementById("second").style.display = 'block';

        const tableBody = document.querySelector('#scheduleTable tbody');

        const schedule = [
            {time: "08:00 - 09:30", subject: "Математика", teacher: "Иванов И.И."},
            {time: "10:00 - 11:30", subject: "Физика", teacher: "Петров П.П."},
            {time: "12:00 - 13:30", subject: "Химия", teacher: "Сидоров С.С."},
            {time: "14:00 - 15:30", subject: "История", teacher: "Кузнецова А.А."},
            {time: "16:00 - 17:30", subject: "Информатика", teacher: "Лебедев Л.Л."}
        ];


        schedule.forEach(item => {
            const row = document.createElement("tr");

            const timeCell = document.createElement("td");
            timeCell.textContent = item.time;
            row.appendChild(timeCell);

            const subjectCell = document.createElement("td");
            subjectCell.textContent = item.subject;
            row.appendChild(subjectCell);

            const teacherCell = document.createElement("td");
            teacherCell.textContent = item.teacher;
            row.appendChild(teacherCell);

            tableBody.appendChild(row);
        });
    }