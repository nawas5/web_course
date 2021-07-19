<?php
$title = "Про нас";
require "blocks/header.php";
?>
<div class="container mt-2">
    <h1><?=$title?></h1>
<!--если ничего нет обработка данных на этой же страничке-->
<!-- для формочки post-->
<!--    <form action="check_post.php" method="post">-->
    <form action="check_get.php" method="get">
        <input type="text" name="username" placeholder="Введите имя" class="form-control"><br>
        <input type="email" name="email" placeholder="Введите email" class="form-control"><br>
        <input type="password" name="password" placeholder="Введите пароль" class="form-control"><br>
        <textarea name="message" placeholder="Введите сообщение" class="form-control"></textarea><br>
        <input type="submit" value="Отправить" class="btn btn-success">
    </form>
</div>
