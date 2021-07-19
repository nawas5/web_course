
<?php
    session_start();

    $title = "Главная страница";
    require "blocks/header.php";
    include_once "blocks/header.php";
    include_once "blocks/header.php";
//    require - если подключен несуществующий файл - ошибка далее код не выполняется
//    include - если ошибка не сработает, далее код работает - продолжит работу
//    require_once include_once, если файл будет подключен ещё раз - повторно не будет подключен
//    для глобальных блоков лучше require
?>
<h1>Главная страница</h1>

<?php
//        $user_name = "Mosolok";
//        setcookie("user_name", $user_name, time() + 5);
//        print_r($_COOKIE);
//        echo $_COOKIE;
    $user_name = "Mosolok";
    $_SESSION['user_name'] = $user_name;

    echo $_SESSION['user_name'];


?>

