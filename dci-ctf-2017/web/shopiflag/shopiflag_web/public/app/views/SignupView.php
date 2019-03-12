<?php

class SignupView extends View
{
    public function show($templates) {
        $templates = array("main" => "signup.php", "content" => "base.php");
        parent::show($templates);
    }
}