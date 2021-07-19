// setInterval(my_func, 1e3);
// // название, количество мс
// var counter = 0;
// function my_func() {
//     // действительно 1000
//     counter++;
//     console.log("Counter: " + counter);
// }

// var counter = 0;

// setInterval(function() {
//     counter++;
//     console.log("Прошло секунд: " + counter);
// }, 1.5e3);

var id = setInterval(my_func, 1e3);

var counter = 0;

function my_func() {

    counter++;
    console.log("Counter: " + counter);

    if (counter == 3) {
        clearInterval(id);
        // дальше не выводится - очищается интервал
    }
}

// таймеры - один раз срабатывает и всё - больше никак не взаимодействуем

setTimeout(function () {
    console.log("Timer is working!");
}, 1000);

// когда нужно чтобы сработал код через какое-то время

// Будет вызвана функция someFunction через 1.5 секунды
setInterval("someFunction()", 1500);

function someFunction() {
	console.log("Функция срабатывает каждые 1,5 секунды");
}

// Ссылка на интервал записывается в переменную
var linkInterval = setInterval("someFunction()", 1500);

function someFunction() {
	console.log("Функция срабатывает каждые 1,5 секунды");
	// Для остановки используйте метод clearInterval
	clearInterval(linkInterval);
}

setTimeout("simple()", 1500);

function simple() {
	console.log("Функция будет вызвана лишь один раз через 1.5 секунды после старта программы");
}