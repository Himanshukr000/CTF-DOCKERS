<?php

class AdminEvaluateView extends View
{
    public function show($templates) {
        $templates = array("main" => "admin-evaluate.php", "content" => "base.php");
        parent::show($templates);
    }
}