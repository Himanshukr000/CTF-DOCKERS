<?php
$servername = "database";
$username = "webserver";
$password = "PP6L43BZpGUi9zC5oaRTbKQT4XBm";
$dbname = "challenge";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("connection failed: " . $conn->connect_error);
}