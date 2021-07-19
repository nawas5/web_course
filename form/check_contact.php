<?php
    session_start();

    unset($_SESSION['username']);
    unset($_SESSION['email']);
    unset($_SESSION['subject']);
    unset($_SESSION['message']);

    unset($_SESSION['error_username']);
    unset($_SESSION['error_email']);
    unset($_SESSION['error_subject']);
    unset($_SESSION['error_message']);

    function redirect() {
        header('Location: contact.php');
        exit;
    }

    $error_username = "";
    $error_email = "";
    $error_subject = "";
    $error_message = "";

    $_SESSION['username'] = $error_username;
    $_SESSION['email'] = $error_email;
    $_SESSION['subject'] = $error_subject;
    $_SESSION['message'] = $error_message;

    $username = htmlspecialchars(trim($_POST['username'])); // из этой строки полностью удаляет все html файы
    $from = htmlspecialchars(trim($_POST['email']));
    $subject = htmlspecialchars(trim($_POST['subject']));
    $message = htmlspecialchars(trim($_POST['message']));

    $_SESSION['username'] = $username;
    $_SESSION['email'] = $from;
    $_SESSION['subject'] = $subject;
    $_SESSION['message'] = $message;

    // при отправлении формы переходит на страничку - данные чтобы отображались и не стирались

    if(strlen($username) <= 1) {
        $_SESSION['error_username'] = "Введите корректное имя";
        redirect(); }
    else if(strlen($from) < 10 || strpos($from,"@") == false) {
        $_SESSION['error_email'] = "Введите корректный email";
        redirect(); }
    else if(strlen($subject) <= 5) {
        $_SESSION['error_subject'] = "Тема сообщения меньше 5 символов";
        redirect(); }
    else if(strlen($message) <= 15) {
        $_SESSION['error_message'] = "Сообщение меньше 15 символов";
        redirect(); }
    else {
        $subject = "=?utf-8?B?".base64_encode($subject)."?=";
        $headers = "From: $from\r\nReply-to: $from\r\nContent-type:text/plan; charset=urf-8\r\n";
        mail("natasha.masalckova@yandex.ru",$subject,$message,$headers);
        $_SESSION['success_mail'] = "Вы успешно отпрвили письмо";
        redirect();
    }

