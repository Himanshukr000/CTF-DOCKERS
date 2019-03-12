<?php

$location_cookie_name = 'Location';
$found_boddy_cookie_name = 'Found_Boddy';

if (isset($_POST['Submit'])){
	if (!empty($_POST['Location'])){
                setcookie($found_boddy_cookie_name, 0, time() + (86400 * 30), '/');
		setcookie($location_cookie_name, base64_encode(strtolower($_POST['Location'])), time() + (86400 * 30), '/');
                header('Location: looking.php');
        }
        else{
		header('Location: tryagain.html');
        }
}
else{
	header('Location: looking.php');
}

?>
