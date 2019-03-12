<?php

class Controller
{
    public function processRequest() {
        $user = new User();
        return array("user" => $user);
    }
}