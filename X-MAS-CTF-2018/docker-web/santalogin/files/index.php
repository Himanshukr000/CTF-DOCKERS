<?php
//error_reporting(0);

$conn = new mysqli("localhost:3306/run/mysqld/mysqld.sock", "alex", "pass");

if ($conn->connect_error)
	die("Connection failed: " . $conn->connect_error);

$conn->query("USE db");

$err = 1;

$ua = $_SERVER['HTTP_USER_AGENT'];
$sql = "SELECT * FROM uas WHERE ua='" . $ua . "'";
$res = $conn->query($sql);

if (mysqli_num_rows($res) > 0) {
	$err = 0;
}
?>

<head>
<link href="https://fonts.googleapis.com/css?family=Charmonman:700" rel="stylesheet">
</head>

<style>
#snowflakeContainer {
	position: absolute;
	left: 0px;
	top: 0px;
}

.snowflake {
	padding-left: 15px;
	font-family: Cambria, Georgia, serif;
	font-size: 14px;
	line-height: 24px;
	position: fixed;
	color: #FFFFFF;
	user-select: none;
	z-index: 10000;
}

.snowflake:hover {
	cursor: default;
}

.text {
	font-family: 'Charmonman', cursive;
	font-size: 60px;
	color: white;
}

.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
</style>

<div id="snowflakeContainer">
	<p class="snowflake">*</p>
</div>

<body style="background-color:black">
	<!--Bells and Whistles-->
	<script src="flsnowcompress.js"></script>
	<audio autoplay>
		<source src="christmas.mp3" type="audio/mpeg">
	</audio>
	
	<img class="center" style="width:200; height:323; margin-top:100px" src="santa.png"></img>
	<p class="text" align="center">Santa's No-Password Login!</p>
	<p class="text" align="center" style="margin-top:-60px; font-size: 32px; opacity: 0.8;">You don't seem to be using an official Computer from Santa's Laboratory!</p>
	<p class="text" align="center" style="margin-top:-40px; font-size: 26px; opacity: 0.8;
		<?php
			if ($err == 1) {
				echo 'color: red;">';
				echo "Access Denied!";
			} else {
				echo 'color: green;">';
				echo "Welcome!";
			}
		?>
	</p>
</body>

<?php
$conn->close();
?>
