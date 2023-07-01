let a = '100';
let b = 200;

a = parseInt(a);
let result = a + b;


let array = [1,2,3,4,5,6,7,8,9,10];
console.log(array[3]);
array[5] = 15;

let matrix = [[1,2,3], [1,2,3], [1,2,3]];

console.log(matrix[0][1]);
matrix[1][2]=10;
console.log(matrix);



let age = prompt('Может ввести свой возраст');
age = parseInt(age);
let years = age + 10;
alert('Сколько лет пользователю будет через 10 лет:  '+ years);

let nom1 = prompt('Видите первое число');
let nom2 = prompt('Видите второе число');
let sum = parseInt(nom1)+parseInt(nom2);
alert('Сумма:  '+ sum);

let str1 = prompt('Видите первое слова');
let str2 = prompt('Видите второе слова');
alert('Ваша слова:   '+ str1 + str2 );

let namee = prompt('Видите имя');
let lastname = prompt('Видите фамилия');
alert('Привет:   '+ namee +'  '+ lastname);

let wight = prompt('Длина прямоугольника');
let hight = prompt('Ширина прямоугольника');
let s = wight*hight;
alert('Площадь этого прямоугольника:   ' + s);