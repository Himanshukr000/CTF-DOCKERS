<?php
//error_reporting(0);
//$conn = new mysqli("localhost:3306/run/mysqld/mysqld.sock", "root", "HTsPAccessKey");

//if ($conn->connect_error)
	//die("Connection failed: " . $conn->connect_error);

//$conn->query("USE wishes");

session_start();

if (!isset($_SESSION['wishes'])) {
	$_SESSION['wishes'] = array();
}

libxml_disable_entity_loader(false);
$dataPOST = trim(file_get_contents('php://input'));
$xmlData = simplexml_load_string($dataPOST, 'SimpleXMLElement', LIBXML_NOENT);

if ($xmlData != "") {
	$_SESSION['wishes'][] = (string) $xmlData;
	//$sql = "INSERT INTO wishes (IP, timestamp, message) VALUES ('" . $_SERVER['REMOTE_ADDR'] . "', '" . time() . "', '" . mysqli_real_escape_string($conn, (string) $xmlData) . "')";
	//if ($conn->query($sql) === TRUE) {
	//	echo "New record created successfully ";
	//} else {
	//	echo "Error! ";
	//}
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	echo "Your wish: " . $xmlData;
	die();
}

//$wishes = $conn->query("SELECT *, message FROM wishes ORDER BY timestamp DESC");
?>

<head>
<link href="https://fonts.googleapis.com/css?family=Mountains+of+Christmas" rel="stylesheet">
</head>

<style>
.text {
	font-family: 'Mountains of Christmas', cursive;
}

textarea {
	resize: none;
box-shadow:
	0 0 0 2px #FFFFFF,
	0 0 0 4px #FF0000;
-moz-box-shadow:
	0 0 0 4px #FFFFFF,
	0 0 0 2px #FF0000;
-webkit-shadow:
	0 0 0 4px #FFFFFF,
	0 0 0 2px #FF0000;
}

button {
	background-color: Transparent;
	background-repeat: no-repeat;
	border: none;
	cursor: pointer;
	overflow: hidden;
	outline:none;
	background: url("paper_airplane.png");
	background-size:cover;
	height:64px;
	width:64px;
	opacity:0.6;
}

li {
	font-size: 24px;
	word-wrap: break-word;
}
</style>

<script>
function lol () {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (xhttp.readyState == 4 && xhttp.status == 200) {
			document.location.reload();
		}
	};
	
	var xml = "<message>" + document.getElementById("textarea").value + "</message>";
	xhttp.open("POST", "/", true);
	xhttp.setRequestHeader('Content-Type', 'application/xml');
	xhttp.send(xml);
};
</script>

<body background="paper.jpg" style = "margin-left:25px; margin-top:25px;">
	<p class="text" style="font-size: 60px">Our Christmas Wishlist!</p>
	<textarea id="textarea" rows="6" cols="50" placeholder="I wish for a pony..." class="text" style="font-size: 30px"></textarea>
	<button style="position:relative; bottom:90px; left:20px;" onclick="lol();"></button>
	
	<div style="margin-top:24px;">
		<?php
			foreach($_SESSION['wishes'] as $msg) {
				echo '<li>' . $msg . '</li><hr>';
			}
		?>
	</div>
</body>
