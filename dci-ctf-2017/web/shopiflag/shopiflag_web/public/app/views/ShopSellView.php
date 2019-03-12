<?php

class ShopSellView extends View
{
    public function show($templates) {
        $templates = array("main" => "shop-sell.php", "content" => "base.php");
        parent::show($templates);
    }
}