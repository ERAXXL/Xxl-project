<?php

$login = filter_var(trim($_POST['login']),
FILTER_SANITIZE_STRING);


$password = filter_var(trim($_POST['password']),
FILTER_SANITIZE_STRING);

$password = md5($password."qwertyuiop123456");



$mysql = new mysqli('localhost','root','root','mangaka');
$result = $mysql -> query("SELECT * FROM `users` WHERE `login` = '$login' AND `password` = '$password'");
$user = $result->fetch_assoc();
if(count($user)==0) {
	echo 'Логин или пороль не верный';
	exit();
}

setcookie('user', $user['name'], time()+(3600*24), "/");

$mysql -> close();

header('Location: /');
?>