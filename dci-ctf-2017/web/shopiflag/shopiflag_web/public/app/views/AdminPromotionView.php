<?php

class AdminPromotionView extends View
{
    public function show($templates) {
        $templates = array("main" => "admin-promotion.php", "content" => "base.php");
        parent::show($templates);
    }
}