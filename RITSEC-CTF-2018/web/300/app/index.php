<?php
include("classes.php.inc");
include((isset($_GET['page']) && is_string($_GET['page']) ? $_GET['page'] : "home") . ".php");
?>
