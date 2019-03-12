<?php

class AdminTasksView extends View
{
    public function show($templates) {
        $templates = array("main" => "admin-tasks.php", "content" => "base.php");
        parent::show($templates);
    }
}