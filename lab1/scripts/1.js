function ex1() {
        document.getElementById("first").style.display = 'block';

        const tableBody = document.querySelector('#multiplicationTable tbody');
        const number = 5;

        for (let i = 1; i <= 10; i++) {
            const row = document.createElement('tr');

            const multiplierCell = document.createElement('td');
            multiplierCell.textContent = `${number} x ${i}`;
            row.appendChild(multiplierCell);

            const resultCell = document.createElement('td');
            resultCell.textContent = number * i;
            row.appendChild(resultCell);

            tableBody.appendChild(row);
        }
    }