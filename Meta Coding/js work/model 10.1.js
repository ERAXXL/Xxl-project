let words = ["apple", "banana", "orange", "grapefruit"];
let a = 0;
for (let i = 0; i < words.length; i++) {
    let word = words[i].length;
    a = word + a;
}
let b = a / words.length;
console.log("Средняя длина слова:  " +b);


//Ex2

let nul = 100;
let numbers = [10, 8, 60, 40, 11];
for (let x = 0; x < numbers.length; x++) {
    let number = numbers[x];
    if (nul >  number) {
        nul = number;
    }
}
console.log('Наименьшее число:  ' + nul);

let sum =0;
let numbers2 = [2, 4, 6, 8, 10];
for (let y = 0; y < numbers2.length; y++) {
    sum = (numbers2[y] ** 2) + sum; 
}
console.log('Сумму квадратов:  ' + sum)