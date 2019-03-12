<?php
require_once('config.php');
require_once('functions.php');
require_once('autoload.php');

// Specifically for the xss challenge
if (session_id() === MODERATOR_PHPSESSID) {
    $_SESSION["userid"]     = 5;
    $_SESSION["username"]   = "John The Moderator";
    $_SESSION["permission"] = 2;
    $_SESSION["about"]      = "Just a moderator.";
}

// make page vulnerable to csrf
header("Access-Control-Allow-Origin: ". ADMIN_SERVER_EXTERNAL);
header("Access-Control-Allow-Credentials: true");

$app = new Application($_SERVER['REQUEST_URI']);
$app->execute();