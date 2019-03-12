<?php

require_once "config.php";

$q = $_GET['q'];

if($facts = loadFacts($q)) {
    echo json_encode($facts);
} else {
    echo json_encode(['error' => 'Bad signature']);
}
