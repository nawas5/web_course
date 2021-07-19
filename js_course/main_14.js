// работа с датой
var date = new Date();
// можно выводить текущую дату и тд

console.log(date.getFullYear());
console.log(date.getMonth());
console.log(date.getMinutes());
// для вывода минут
console.log(date.getDate());

date.setDate(2);
console.log(date.getDate());
// можно установить свою дату для обработки
var time_date = new Date();

// массивы и несколько свойств для массивов
var arr = [5, 6, 7, 8, 9];
console.log(arr.length);
console.log(arr.join(", "));
// как можно выводить - например строчно через join

var stroka = arr.reverse().join(", ");
console.log(stroka.split(", "));

var string = "Строка";
console.log(string[0]); // Выведет символ "C"
console.log(string[3] + string[1]); // Выведет символы "от" (4 и 2 символ)
// были числами стали другие

// создание классов и объектов
// описание для всех - сколько угодно объектов и у них есть свои параметры

class Person {
    constructor(name, age, happiness) {
        this.name = name;
        this.age = age;
        this.happiness = happiness;
    }


    info() {
    console.log("Человек: " + this.name + " Возраст: " + this.age + " Насnроение: " + this.happiness);
    }
}

var alex = new Person('Alex', 15, true);
console.log(alex.name);

var bob = new Person('Bob', 22, false);
console.log(bob.name);

bob.info();