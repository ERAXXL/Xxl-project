
let age = prompt('Введите ваш возраст:');
if (age>=18) {
    alert('Добро пожаловать!');
}
else {
    alert("Извините, доступ запрещен!");
}

let num = prompt('Введите число!');
num = parseInt(num);
if (num>0) {
    alert("Число положительное");
}
else if (num==0) {
    alert("Число равно нулю");
}
else {
    alert("Число отрицательное");
}

let month = prompt('Какой текущий месяц в цифрах');
month = parseInt(month);
if (month > 2 && month < 6 ) {
    alert("Сейчас весна!");
}
else if (month > 5 && month < 9 ) {
    alert("Сейчас лето!");
}
else if (month > 8 && month < 12 ){
    alert("Сейчас осень!")
}
else {
    alert("Сейчас зима!");
}



let num1 = prompt('Number 1');
let num2 = prompt('Number 2');
num1 = parseFloat(num1);
num2 = parseFloat(num2);
if (num1 > num2) {
    alert('Win:  ' + num1);
}
if (num1 < num2) {
    alert('Win:  ' + num2);
}
else{
    alert('draw')
}


let day = prompt('Day');
day= parseInt(day);
if (day > 5) {
    alert('Будний день');
}
else{
    alert('Выходной день');
}
