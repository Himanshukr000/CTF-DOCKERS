<?php

class ShopBuyView extends View
{
    public function show($templates) {
        $templates = array("main" => "shop-buy.php", "content" => "base.php");
        parent::show($templates);
    }
}