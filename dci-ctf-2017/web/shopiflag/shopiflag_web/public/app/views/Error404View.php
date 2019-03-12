<?php

class Error404View extends View
{
    public function show($templates) {
        $templates = array("main" => "404.php", "content" => "base.php");
        parent::show($templates);
    }
}