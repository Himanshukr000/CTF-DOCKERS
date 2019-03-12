<?php
   if ( isset( $_GET['file'] ) ) {
	   $file = $_GET['file'];
	   if( !file_exists($file) ) die("File not found");
	   if ($file === "english.html" || $file === "french.html"){
		   echo file_get_contents( $_GET['file'] );
	   }
	   else{
			// Force the download
			header("Content-Disposition: attachment; filename=" . basename($file));
			header("Content-Length: " . filesize($file));
			header("Content-Type: application/octet-stream;");
			readfile($file);
	   }

   }
   else{
	   echo file_get_contents("index.html");
   }
?>
