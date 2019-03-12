<html>
<head>
Secure Web Login
</head>
<body>
<?php
if($_POST[user] && $_POST[pass]) {
  mysql_connect("localhost","php3","xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx");
  mysql_select_db("php3");

  $user = $_POST[user];
  $pass = md5($_POST[pass], True);
  $query = @mysql_fetch_array(mysql_query("select user from php3 where (user='$user') and (pw='$pass')"));

  if($query[user]=="admin") {
    echo "<p>Logged in! Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx </p>";
  }

  if($query[user] != "admin") {
    echo("<p>You are not admin!</p>");
  }
}

?>
<form method=post action=index.php>
<input type=text name=user value="Username">
<input type=password name=pass value="Password">
<input type=submit>
</form>
</body>
<a href="index.phps">Source</a>
</html>
