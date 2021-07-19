// function checkForm(el) {
//     console.log("Text");
//     return false;
// }
// как дождаться ответа функции
// получение данных из формы
document.getElementById('main-form').addEventListener("submit", checkForm);

function checkForm(event) {
    // передаем параметр как само событие - характеристики которые свойственны событи.
    event.preventDefault();
    // отключаем поведение страницы - перезагрузку
    var el = document.getElementById('main-form');
    // теперь мы перестаем использовать атрибуты

    // var name = document.getElementById('name').value;
    // console.log(name);

    var name = el.name.value;
    var pass = el.pass.value;
    var repass = el.repass.value;
    var state = el.state.value;
    var fail = "";

    if (name == "" || pass == "" || state =="") {
        fail = "Заполните все поля";
    } else if(name.length <= 1 || name.length > 50) {
        fail = "Введите корректное имя";
    } else if(pass != repass) {
        fail = "Пароли не совпадают";
    } else if(pass.split("&").length > 1) {
        fail = "Некорректный пароль";
    }

    if (fail != "") {
        document.getElementById('error').innerHTML = fail;
        console.log(false);
        // return false;
    } else {
        alert("Все данные корректно заполнены");
        window.location = 'file:///C:/Users/Mosolok/Documents/GitHub/javascript_course/js_course/index.html';
        // return false;
    }

    // return false;
    // переадресация на другую страничку

   
}
// внутрь функции передаем формочку по\тому можно упростить и обращаться через объекты формы
// через el.