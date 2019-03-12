<?php
include_once "includes/encrypt.php";
$username = $_POST["username"];
$password = $_POST["password"];
$error = "";
if(isset($username) && isset($password)) {
    if($username != "" && $password != "") {
        if(ctype_alnum($username) && ctype_alnum($password)) {
            setcookie("ID", encrypt($username, $password));
        }
        else {
            #non alpha_num 
            $error="alpha_num";
        }   
    }
    else {
        #need both params 
        $error="empty_params";
    }
    
    if($error == "") {
        header("Location: ./main_page.php");
    }
    else {
        header("Location: ./index.php?error=" . $error);
    }
}
else {
    header("Location: ./index.php");
}

?>
