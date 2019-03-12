<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" />
<?php
/* #if theu have already logged in they go straight to main page */
/* $cookie = $_COOKIE["ID"]; */
/* if(isset($cookie)){ */
/*     header("Location: main_page.php"); */
/* } */
?>
<div class="container" >

    <h1>Login</h1>
    <?php
    $err = $_GET["error"];
    if(isset($err)) {
        if($err == "alpha_num") {
            print '<h3><font color="red">Username and Password must be alphanumeric</font></h3>';
        }
        if($err == "empty_params") {
            print '<h3><font color="red">Username or password have been left blank</font></h3>';
        }
        if($err == "login") {
            print '<h3><font color="red">You must be logged in to view the main page</font></h3>';
        }
    }
    ?>
    <form action="login.php" method="post">
    Username: <input type="text" name="username" value="" /><br/>
    Password: <input type="password" name="password" value="" /><br/>
    <input type="submit" value="submit" />
    </form>
    <div style="padding-top: 20%; padding-left: 75%;">
        <img src="imgs/cutezombie1.png" alt="Cute zombie" />
    </div>
</div>
    
