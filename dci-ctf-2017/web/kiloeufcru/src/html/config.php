<?php

$db = new PDO('sqlite:../data.db');

define('DEMO_KEY', $db->query('SELECT text FROM apikeys WHERE demo = 1')->fetch()['text']);

function sign($data) {
    return base64_encode($data) . '--' . sha1(DEMO_KEY . $data);
}

function check($msg) {
    list($b64, $sig) = explode('--', $msg);

    $data = base64_decode($b64);

    if($msg === sign($data)) {
        return $data;
    } else {
        return null;
    }
}

function filter($str) {
    return quoted_printable_encode($str);
}

function loadFacts($id) {
    global $db;

    if($id = check($id)) {
        $id = filter($id);
        $q =  $db->query("SELECT * FROM facts WHERE id = '" . $id . "'");

        if($q) {
            return $q->fetch();
        } else {
            return ['error' => 'database error'];
        }
    } else {
        return false;
    }
}

?>
