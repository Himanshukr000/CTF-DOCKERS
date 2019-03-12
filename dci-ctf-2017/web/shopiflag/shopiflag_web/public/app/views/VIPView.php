<?php

class VIPView extends View
{
    public function show($templates) {
        $templates = array("content" => "vip.php");
        parent::show($templates);
    }
}