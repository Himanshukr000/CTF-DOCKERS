<?php

spl_autoload_register(function ($class) {
    $folders = array("app/", "app/controllers/", "app/views/", "app/models/");
    foreach ($folders as $folder) {
        if (is_readable($folder . $class . ".php")) {
            require_once $folder . $class . '.php';
            break;
        }
    }
});