let sum=0
for (let i = 1; i < 11; i++) {
    sum = i+sum;
}

console.log(sum);
document.write(sum);

let myarray = [1, 2, 3, 4, 5];
for (let y =0; y<5; y++){
    array = myarray[y]*2; 
    console.log(array);
    document.write(array);
}

let a = 1;
let num = 1;
while (a) {
    console.log(num);
    document.write(num);
    num = a * 2;
    a = num;
    if (num > 256) {
        break;
    }
}

