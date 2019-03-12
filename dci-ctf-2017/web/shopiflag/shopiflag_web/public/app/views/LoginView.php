<?php

class LoginView extends View
{
    public function show($templates) {
        $templates = array("main" => "login.php", "content" => "base.php");
        parent::show($templates);
    }
}