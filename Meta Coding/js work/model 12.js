class student{
    constructor(namee, age, course) {
        this.namee = namee;
        this.age = age;
        this.course = course;
    }


    showInfo() {
        console.log(
            `Имя: ${this.namee}, Возраст: ${this.age}, Курс: ${this.course}`
        );
    }
    increaseAge(){
        this.age = parseInt(this.age)+1;
        console.log(
            `Имя: ${this.namee}, Возраст: ${this.age}, Курс: ${this.course}`
        );
    }
}

let name1 = new student('Иван','20','3');
name1.showInfo();

let name2 =new student('Анна','22','4');
name2.showInfo();

let name3 = new student('Иван','20','3');
name1.increaseAge();

let name4 =new student('Анна','22','4');
name2.increaseAge();