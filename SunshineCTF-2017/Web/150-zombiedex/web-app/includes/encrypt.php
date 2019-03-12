<?php
function encrypt($username,$password){
    $arr = array("username" => $username,"password" => $password);
    return bin2hex(base64_encode(strrev(json_encode($arr))));
}
function decrypt($str){
    return json_decode(strrev(base64_decode(hex2bin($str))));
}
?>
