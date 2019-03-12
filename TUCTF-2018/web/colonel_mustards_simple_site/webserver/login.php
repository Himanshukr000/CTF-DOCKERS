<?php
	include("conn.php");
   	session_start();

  	$username = $_POST["username"];
  	$password = $_POST["password"];
  	$query = "SELECT 1 FROM users WHERE user='$username' AND password='$password'";

	$result = mysqli_query($conn, $query);
    	$row = mysqli_fetch_array($result, MYSQLI_NUM);

    	if ($row) {
               	echo '<link href="login.css" rel="stylesheet" type="text/css">';
		echo '<title>Perfect!</title>';
               	echo "<h1>$FLAG</h1>";
	}
	else {
		echo '<link href="login.css" rel="stylesheet" type="text/css">';
      		echo "<h1>Login failed.</h1>";
    	}
?>