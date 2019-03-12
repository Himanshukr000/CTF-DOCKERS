<?php
    $admin_status = $_POST["is_admin"];
    if(isset($admin_status)) {
        if($admin_status == true) {
            print file_get_contents("flag.txt");
        }
    }
?>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" />
<div class="container">
    <h1>Login</h1>
    <form action="index.php" method="post">
        Username: <input type="text" name="username" value="admin" /> <br />
        Password: <input type="password" name="password" value="admin" /> <br />
        <input type="hidden" name="is_admin" value="0" />
        <input type="submit" name="" value="submit" />
    </form>
</div>
