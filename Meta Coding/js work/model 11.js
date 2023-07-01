function sum(a, b) {
    console.log(a+b);
}

sum(1, 5);

let newarray = [];
function arr(myarray) {
    for (let i = 0; i < myarray.length; i++ ) {
        newarray.push(myarray[i] * 2);
    }
    return newarray;
}

let array=[1,2,1,1];
console.log(arr(array));

let take = (num) => num%2 == 0 ? 'четным ': 'нечетным';

console.log(take(5));