<?php
  	$username = $_POST["username"];
  	$password = $_POST["password"];

    	if ($username == 'admin' && $password == 'admin') {
               	echo '<link href="login.css" rel="stylesheet" type="text/css">';
		echo '<title>Lovely</title>';
               	echo "<h1>TUCTF{1_4ccu53_mr._6r33n_w17h_7h3_b4d_p455w0rd_1n_7h3_l061n}</h1>";
	}
	else {
		echo '<link href="login.css" rel="stylesheet" type="text/css">';
      		echo "<h1>Rats! No luck.</h1>";
    	}
?>