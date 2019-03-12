<style>
body {background-color: white;}

.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
</style>

<body>
<h1 align="center" style="margin-top:20px">Santa's Archives</h1>
<p align="center">Santa loves hiding his secrets on the page numbered as his lucky number :)</p>
<img src="book.png" class="center" style="width:400px;height:234px"></img>

<div align="center">

<form action="/" method="get" style="display:inline-block;">
    <button type="submit" value="1" name="page">Page 1</button>
</form>

<form action="/" method="get" style="display:inline-block;">
    <button type="submit" value="2" name="page">Page 2</button>
</form>

<form action="/" method="get" style="display:inline-block;">
    <button type="submit" value="3" name="page">Page 3</button>
</form>

</div>

</body>
<p align="center">
<?php
if (!isset($_GET['page'])) {
	die();
}

function GetStr($num) {
	$str = md5("SANTA" . $num . "TEST"). md5("test" . $num . "teggst") . md5("reading" . $num . "SRCcode") . md5("is" . $num . "fun");
	return $str;
}

$page = $_GET['page'];
if ($page == "1327") {
    echo "X-MAS{W00pS_S0m30n3_73l1_S4n7a_h1s_c00k1eS_Ar3_BuRn1ng}";
}
else {
    echo GetStr($page);
}
?>
</p>
