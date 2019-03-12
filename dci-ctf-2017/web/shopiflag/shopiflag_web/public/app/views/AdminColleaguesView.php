<?php

class AdminColleaguesView extends View
{
    public function show($templates) {
        $templates = array("main" => "admin-colleagues.php", "content" => "base.php");
        parent::show($templates);
    }
}