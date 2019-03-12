<?php
error_reporting(0);
session_start();
?>

<style>
.center {
	display: block;
	margin-left: auto;
	margin-right: auto;
	width: 50%;
}

body {
	background-image: url('img/BG.png');
	background-size: cover;
	line-height: 0.8;
}

h1 {
	font-family: 'Major Mono Display', monospace;
}

.upload-btn-wrapper {
	position: relative;
	overflow: hidden;
	display: inline-block;
}

.upload-btn-wrapper input[type=file] {
	font-size: 500px;
	position: absolute;
	width: 1024px;
	height: 512px;
	left: -50%;
	top: 0;
	opacity: 0;
}

a {
	color: #dddddd;
}
::-webkit-file-upload-button { cursor:pointer; }
</style>

<head>
<link href="https://fonts.googleapis.com/css?family=Major+Mono+Display" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Staatliches" rel="stylesheet">
</head>

<body>
	<h1 style="text-align: center; font-size:140px; margin-top:50px; color: #eeeeee">Welcome<h1>
	<h1 style="text-align: center; font-size:40px; margin-top:-50px; color: #eeeeee">to your highly secure <a style="color: white">peRsonAl</a> Vault</h1>
	<div class="center">
	<form class="center" action="/" method="post" enctype="multipart/form-data" style="width:512px">
		<div class="upload-btn-wrapper">
			<img src="img/vault.png" style="width:512px; height:512px; margin-top:-40px; cursor: pointer;"></img>
			<input style="cursor: pointer;" type="file" name="file">
		</div>
		<input class="center" type="submit" value="Securize Chosen File" name="submit">
	</form>
	</div>
	<div class="center">
	<h1 style="color:white; font-family: 'Staatliches', cursive;">
	<?php
		if(isset($_POST["submit"])) {
		
		if (filesize($_FILES["file"]["tmp_name"]) > 2048) {
			echo "[ERROR] The file uploaded is too large. The Vault accepts only files up to 2 KiloBytes.";
		} else if (filesize($_FILES["file"]["tmp_name"]) == 0) {
			echo "[ERROR] Uploaded file has a size of 0 Bytes.";
		} else {
			echo "[INFO] Filesize: " . filesize($_FILES["file"]["tmp_name"]) . " Bytes. <br>";
			$zip = new ZipArchive;
			$res = $zip->open($_FILES["file"]["tmp_name"]);
			$path = 'uploads/' . session_id();
			
			if ($res === TRUE) {
				echo '[INFO] Ultracompact File type detected.<br>[INFO] Begin Ultracompact File Processing...<br>';
				$numfiles = $zip->numFiles;
			
				for ($i = 0; $i < $numfiles; $i++) {
					$fname = $zip->getNameIndex($i);
					$contents = $zip->getFromIndex($i);
					
					if (strlen ($contents) > 2048) {
						echo "[WARN] File " . $fname . " is larger than 2KB. Skipping...<br>";
						continue;
					}
			
					$newfile = fopen("uploads/" . session_id() . "/" . $zip->getNameIndex($i), "w");
					if (!$newfile) {
						echo "[ERROR] Something Went Wrong.";
						die();
					}
					fwrite($newfile, $zip->getFromIndex($i));
				}
			
				$zip->close();
		
				echo '[OK] Operation Succeeded.<br>';
				echo '[INFO] Your files have been decompressed at: <a href="' . $path . '">/' . $path . '</a>';
			} else {
				echo '[INFO] Begin Normal File Processing...<br>';
				
				$name = basename($_FILES["file"]["name"]);
				if (preg_match('/^[A-Za-z0-9-]+/', $name)) {
					if (!is_dir($path))
						mkdir($path);
					move_uploaded_file ($_FILES["file"]["tmp_name"], $path . "/" . $name);
					echo '[INFO] File Stored Successfully<br>';
					echo '[INFO] File is stored at: <a href="' . $path . '/' . $name . '">/' . $path . '/' . $name . '</a>';
				} else {
					echo '[ERROR] Illegal Filename.';
				}
			}
		}
	}
	?>
	</h1>
	</div>
</body>