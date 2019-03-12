<?php

class AccountLogoutController extends Controller
{
    public function processRequest() {
        unset($_SESSION["userid"]);
        unset($_SESSION["username"]);
        unset($_SESSION["permission"]);
        unset($_SESSION["vip"]);
        session_destroy();
        setcookie ("PHPSESSID", "", time() - 3600, '/');
        header('location: /');
        exit();
    }
}