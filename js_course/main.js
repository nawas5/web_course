// как будто уже в теге script
// document.write("JavaScript тут!");
// console.log("JavaScript тут!");
// console.info("JavaScript тут!");
// console.error("JavaScript ошибка!");
// console.warn("JavaScript ошибка!");

// чистка кэша, чтобы файл подгрузился, когда подключили код и файл не хочет грузиться



// var num = 5;
// console.log("Переменная num = ", num);
// num = 6;
// console.log("Переменная: " + num + ".");
// // const - если переопределить - ошибка

// var x = 15.;
// var y = 7.4;
// console.log("Результат: " + (x - y));
// console.log("Результат: " , x - y);

// var num = "12";
// console.log("Результат: " + (Number(num) + x));
// // здесь не нужно импортировать модули - например. аналогично Python 
// // import numpy as np
// // import math 
// // здесь просто вызывается модуль Math

// var x = 90, a = 8;
// var res = x < a ? (x + a) : (x - a);
// console.log(res);

// // Array для массивов

// var some = new Array(); // Создание пустого массива
// some[0] = '1'; // Добавление 1 элемента
// some[1] = 2; // Добавление 2 элемента
// console.log(some[0]); // Вывод первого элемента
// var array = new Array(1, 5, 2); // Создание массива со значениями сразу же

// var elements = new Array(23, 6, 0, true, "Первый");
// // Выведет значение 5, так как в массиве 5 элементов
// console.log(elements.length);

// var x = new Array(new Array(0, 34, 2), new Array(3, 4, 5));
// console.log(x[0][1]); // Выведет 34

// // Можно их сразу не присваивать
// var symbols = new Array(new Array(), new Array());
// symbols[0][1] = 'A';

// x[0][1] = 1; // Вместо 34 теперь будет 1

// // Циклы
// // здесь блиэе к матлабу
// for (var i = 0; i < 10; i++)
// 	console.log(i);

// var i = 1; // Создание переменной
// while (i <= 10) { // Здесь только условие
//     console.log(i);
//     i++; // Увеличение переменной
// }

// var x = 13;
// do {
// 	x--;
// 	console.log(x);
// } while (x > 10);


// for(var i=10; i <=20; i++) {
//     if(i % 2 == 0)
//         continue;
//     if(i > 15) {
//         break;
//     }
//     console.log(i);
// }


// всплывающие она - со своими стилями - то нужно делать на стороне
//alert("Погода норм");
// далее всплывающие окна нужно будет делать со своими стилями
// var data = confirm("Ну че по погоде?")
// console.log(data)
// if (data) {
//     alert("Там норм")
// }
// // для каждого стиля свои окна

// prompt("Сколько вам лет ", 22)

// var person;
// if(confirm("Вы точно пидр?")) {
//     person = prompt("Введите что вы пидр");
//     alert("Привет " + person);
// } else {
//     alert("Вы всё равно пидрр");
// }

function test() {
	console.log("Вывод чего-либо в консоль");
}

// function test(word) {
// 	console.log(word);
// }

// function test(some_number) {
// 	some_number *= 2;
// 	return some_number;
// }

test();

// события и обработчик события

var counter = 0;

function onClickButton(element) {
    counter ++;
    element.innerHTML = "Вы нажали на кнопку " + counter;
    console.log(counter);
}