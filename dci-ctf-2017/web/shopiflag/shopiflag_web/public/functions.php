<?php

function db_connect($user, $pwd) {
    //$servername = "db";
    $servername = "db";
    $dbname = "shopiflag_ctf";

    $db = new PDO("mysql:host=$servername;dbname=$dbname", $user, $pwd, 
                  array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET SESSION sql_mode=""'));
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Check connection
    if (!$db) {
        die("Connection failed: " . $db->connect_error);
    } 

    return $db; 
}