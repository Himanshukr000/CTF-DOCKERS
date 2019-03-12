<?php
session_start();

$servername = "db";
$dbname     = "shopiflag_ctf";
$user       = "admin_db_user";
$pwd        = "2Dd82s2AcUzY4TxL";

$db = new PDO("mysql:host=$servername;dbname=$dbname", $user, $pwd, 
              array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET SESSION sql_mode=""'));
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Check connection
if (!$db) {
    die("Connection failed: " . $db->connect_error);
} 