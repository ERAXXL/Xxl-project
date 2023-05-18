<?php

$login = filter_var(trim($_POST['login']),
FILTER_SANITIZE_STRING);
$email = filter_var(trim($_POST['email']),
FILTER_SANITIZE_STRING);
$password = filter_var(trim($_POST['password']),
FILTER_SANITIZE_STRING);

if (mb_strlen($login) <5 || mb_strlen($login) >90) {
	echo "Логин недопустимо";
	exit();
}else if (mb_strlen($email) <3 || mb_strlen($email) > 50) {
	echo "Имя недопустимо";
	exit();
}else if (mb_strlen($password) < 8 || mb_strlen($password) > 10) {
	echo "Пороль недопустимо";
	exit();
}

$password = md5($password."qwertyuiop123456");


$mysql = new mysqli('localhost','root','root','mangaka');
$mysql ->query ("INSERT INTO `users` (`login`, `password`, `email`)
VALUES ('$login', '$password', '$email')");

$mysql -> close();

header('Location: /');
?>