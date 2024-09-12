function ex5() {
    document.getElementById("five").style.display = 'flex';
}

// Объект школьника
const student = {
    firstName: "Иван",
    lastName: "Иванов",
    middleName: "Иванович",
    birthYear: 2005,
    class: 9,
    favoriteSubjects: ["Математика", "Физика", "Информатика"],

    registrationAddress: {
        country: "Россия",
        city: "Москва",
        houseNumber: 12,
        apartmentNumber: 45
    },

    residenceAddress: {
        country: "Россия",
        city: "Москва",
        houseNumber: 15,
        apartmentNumber: 67
    },

    showInfo: function () {
        const studentInfoDiv = document.getElementById("student-info");

        const infoHtml = `
            <p><strong>Фамилия:</strong> ${this.lastName}</p>
            <p><strong>Имя:</strong> ${this.firstName}</p>
            <p><strong>Отчество:</strong> ${this.middleName}</p>
            <p><strong>Год рождения:</strong> ${this.birthYear}</p>
            <p><strong>Класс:</strong> ${this.class}</p>
            <p><strong>Любимые дисциплины:</strong> ${this.favoriteSubjects.join(", ")}</p>
            <h3>Место прописки:</h3>
            <p>${this.registrationAddress.country}, ${this.registrationAddress.city}, Дом: ${this.registrationAddress.houseNumber}, Квартира: ${this.registrationAddress.apartmentNumber}</p>
            <h3>Место проживания:</h3>
            <p>${this.residenceAddress.country}, ${this.residenceAddress.city}, Дом: ${this.residenceAddress.houseNumber}, Квартира: ${this.residenceAddress.apartmentNumber}</p>
        `;

        // Вставляем данные в HTML
        studentInfoDiv.innerHTML = infoHtml;
    }
};

// Добавляем обработчик события для кнопки
document.getElementById("show-info-btn").addEventListener("click", function () {
    student.showInfo();
});
