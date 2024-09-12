function ex3() {
    document.getElementById("third").style.display = 'flex';
}

function main() {
    inputValue = document.getElementById("number").value;
    console.log("1212sss ", inputValue);
    if (inputValue % 2 !== 0) {
        sum = 0;
        for (i = 1; i <= inputValue; i ++) {
            sum += i;
        }
        document.getElementById("print").textContent = sum;
    } else {
        val = 1;
        for (i = 1; i <= inputValue; i ++) {
            val *= i;
        }
        document.getElementById("print").textContent = val;
    }
}