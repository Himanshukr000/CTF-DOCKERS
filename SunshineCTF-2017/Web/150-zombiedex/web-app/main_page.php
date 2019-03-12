<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" />
<div class="container">
    <?php
    error_reporting(E_ALL);
    include_once "includes/encrypt.php";
    $cookie = $_COOKIE["ID"];
    if(isset($cookie)) {
        $arr = decrypt($cookie);
        $username = $arr->{'username'};
        $password = $arr->{'password'};
        print "<h1>Welcome $username !! </h1>";
    }
    else {
        header("Location: index.php?error=login");
    }
    
    ?>
    <form action=main_page.php method="post">
        <input type="submit" name="get_flag" value="Click Here to get your Flag" />
    </form>
    
    <?php
    if(isset($_POST["get_flag"])) {
        include_once "includes/creds.php";
        include_once "includes/encrypt.php";
        
        $link = mysqli_connect($mysql_db_ip, $mysql_db_username, $mysql_db_password);
        mysqli_select_db($link,"CTFdb");
        $statement = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
        $res = mysqli_query($link, $statement);

        if(mysqli_num_rows($res) > 0) {
            print file_get_contents("flag.txt");
        }
        else {
            print "Did you actually think that was going to work?";
        }
    }
    
    ?>
    
</div>
