<?php

class HomeView extends View
{
    public function show($templates) {
        $templates = array("main" => "home.php", "content" => "base.php");
        parent::show($templates);
    }
}