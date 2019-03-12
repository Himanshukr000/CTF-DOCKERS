<?php

class AccountInboxView extends View
{
    public function show($templates) {
        $templates = array("main" => "account-inbox.php", "content" => "base.php");
        parent::show($templates);
    }
}