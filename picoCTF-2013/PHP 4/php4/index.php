<html>
<head>
Secure Web Login II
</head>
<body>

<?php
if($_POST[user] && $_POST[pass]) {
  mysql_connect("localhost","php3","2d35dfb59b64af079f8e75e2e5e4dc8d");
  mysql_select_db("php3");

  $user = $_POST[user];
  $pass = md5($_POST[pass]);
  $query = @mysql_fetch_array(mysql_query("select pw from php3 where user='$user'"));

  if (($query[pw]) && (!strcasecmp($pass, $query[pw]))) {
    echo "<p>Logged in! Key: 50c90a07790d4d0ab7fc7f695cb61d0e </p>";
  }
  else {
    echo("<p>Log in failure!</p>");
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

