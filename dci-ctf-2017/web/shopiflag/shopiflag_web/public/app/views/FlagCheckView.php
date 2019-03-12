<?php

class FlagCheckView extends View
{
    public function show($templates) {
        $templates = array("main" => "flag-check.php", "content" => "base.php");
        parent::show($templates);
    }
}