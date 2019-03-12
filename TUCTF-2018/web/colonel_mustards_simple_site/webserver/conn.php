<?php
        $servername = "localhost";
        $username = "root";
        $password = "change the root password to something new";
        $db = "challenge";
	$FLAG = "TUCTF{1_4ccu53_c0l0n3l_mu574rd_w17h_7h3_r0p3_1n_7h3_l061n}";

        $conn = new mysqli($servername, $username, $password, $db);

        // Check connection
        if ($conn->connect_error) {
                die("Connection failed");
        }
?>
