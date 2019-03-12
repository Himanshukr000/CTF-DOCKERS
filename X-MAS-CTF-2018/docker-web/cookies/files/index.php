<?php
	if (!isset($_COOKIE["adminpass"]))
		setcookie("adminpass", "MyLittleCookie!");
	
	if (!isset($_COOKIE["cookiez"]))
		setcookie("cookiez", "WlhsS2NGcERTVFpKYWtscFRFTktNR1ZZUW14SmFtOXBXak5XYkdNelVXbG1VVDA5");
?>

<style>
body {
  background-image: url('https://cdn.static-economist.com/sites/default/files/images/print-edition/20171223_STP001_0.jpg');
  background-size: cover;
}

h1 {
	font-family: 'Charm', cursive; margin-top: 20px; margin-left:40px; font-size: 50px
}

.wrong {
	color: #FF4242;
	text-shadow: 2px 2px #000000;
}

.right {
	color: #42FF42;
	text-shadow: 2px 2px #000000;
}
</style>

<head>
<link href="https://fonts.googleapis.com/css?family=Charm" rel="stylesheet">
</head>

<body>
<h1 style="text-shadow: 2px 2px #FFFFFF;">Santa loves cookies! Do you?</h1>
<img style="margin-top:-20px" src="http://pngimg.com/uploads/cookie/cookie_PNG13697.png">
</body>

<?php
    error_reporting(0);
	$pass = "12c900JCd92_$@)9)sDJ0C992124OPSDA";
    $cookie_name = "cookiez";
	
    if (isset($_COOKIE["cookiez"])) {
        $val = json_decode(base64_decode(base64_decode(base64_decode($_COOKIE["cookiez"]))));
		
        if ($val->type == 'admin') {
			echo "<h1 ";
			
			echo $_COOKIE["adminpass"];
			if (strcmp($_COOKIE["adminpass"], $pass) == 0) {
				echo " class='right'>";
				echo "Good job! Here's your flag:<br>X-MAS{S4n74_L0v35__C00kiesss_And_Juggl1ng!}";
			} else {
				echo " class='wrong'>";
				echo "You got the admin password wrong :c<br>";
			}
			
			echo "</h1";
		}
    }
?>
</h1>
