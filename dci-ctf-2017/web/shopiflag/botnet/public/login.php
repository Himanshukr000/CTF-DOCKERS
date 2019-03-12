<?php
require_once('db-connect.php');

if (isset($_POST["login"])) {
    $username = isset($_POST["username"]) ? $_POST["username"] : "";
    $password = sha1(isset($_POST["password"]) ? $_POST["password"] : "");

    $stmt = $db->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
    $stmt->bindParam(1, $username, PDO::PARAM_STR);
    $stmt->bindParam(2, $password, PDO::PARAM_STR);
    $stmt->execute();

    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
    if (count($result) == 1) {
        $_SESSION["rank"] = $result[0]["permission"];
    }
}
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Admin - Login</title>
    </head>

    <body>
        <form method="POST" action="">
            <input type="text" name="username">
            <input type="password" name="password">
            <input type="submit" name="login"/>
        </form>
    </body>
</html>