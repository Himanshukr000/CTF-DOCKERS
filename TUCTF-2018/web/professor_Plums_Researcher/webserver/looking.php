<?php

$location_cookie_name = 'Location';
$found_boddy_cookie_name = 'Found_Boddy';
$location = 'billiard room';

if (!isset($_COOKIE[$location_cookie_name]) || !isset($_COOKIE[$found_boddy_cookie_name])){
	header('Location: search.html');
}
else{
	#strtolower was added after the competition to account for post requests straight to this webpage
	if (strtolower(base64_decode($_COOKIE[$location_cookie_name])) != $location){
		echo '<title>No luck :/</title>';
		echo '<link href="file.css" rel="stylesheet" type="text/css">';
		echo "<h1><center>Nice try but he's not there</center></h1>";
		echo '<p>Maybe try somewhere else in the mansion?</p>';
	}
	else{
		if($_COOKIE[$found_boddy_cookie_name] == 0){
			echo "<title>Where'd he go?</title>";
			echo '<link href="file.css" rel="stylesheet" type="text/css">';
			echo "<h1><center>Nice try but you can't find him</center></h1>";
			echo "<p>Maybe try looking again?</p>";
		}
		else{
			echo "<title>Success!</title>";
			echo '<link href="file.css" rel="stylesheet" type="text/css">';
			echo '<h1><center>Congrats! You found him</center></h1>';
			echo '<p>TUCTF{1_4ccu53_pr0f3550r_plum_w17h_7h3_c00k13_1n_7h3_b1ll14rd_r00m}</p>';
		}
	}
}

?>
