<?php
    print_r($_POST);
    $name = $_POST['username'];
    $email = $_POST['email'];
    $pass = $_POST['password'];

    // trim - удаление пробелов
    if (trim($name) == "") {
        echo "Вы не ввели имя пользователя";
    }
    // strlen - подсчитать колличество символов внутри строки
    // md5 - кеширование для пароля
    // foreach ($_POST as $key => $value) {
    //        echo $value; }
    // header('Location: тот файл куда хотим перекинуть пойзователя');
    // exit; - оператор после которого код не обрабатывается
//    данный метод - ключи - полностью ассоциативный
