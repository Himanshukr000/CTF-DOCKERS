<?php
function randomName() {
    $names = array(
    'Faklutleezz',
    'Gladee',
    'Oruk',
    'Glirlen',
    'Indi',
    'Kethak',
    'Theewinbick',
    'Gnillozz',
    'Balkock',
	'Jelbu',
	'Fannuklil',
	'Kilbe',
	'Fixin'
);
 
$surnames = array(
    'Puddlenozzle',
    'Clockspark',
    'Wigglebus',
    'Shiftspindle',
    'Copperdock',
    'Sparklenozzle',
    'Temperhouse',
    'Bellowstrip',
    'Quietkettle',
    'Trickblock',
	'Pumpbrake'
);

$random_name = $names[mt_rand(0, sizeof($names) - 1)];
$random_surname = $surnames[mt_rand(0, sizeof($surnames) - 1)];

return $random_name . ' ' . $random_surname;
}

function getImage ($name) {
	$name = str_replace(' ', '_', $name);
	if (file_exists("avatars/" . $name) === false)
		return "avatars/noimage";
	else
		return "avatars/" . $name;
}

//error_reporting(0);
session_start();
if (!isset($_SESSION['name'])) {
	$_SESSION['name'] = randomName();
}
?>