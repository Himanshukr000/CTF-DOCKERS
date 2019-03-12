<?php

class AccountSettingsView extends View
{
    public function show($templates) {
        $templates = array("main" => "account-settings.php", "content" => "base.php");
        parent::show($templates);
    }
}