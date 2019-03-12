<?php
include ('engine.php');

$status = "";
$err = 0;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	if (isset($_FILES['image']['tmp_name'])) { //Image
		$uploaddir = "avatars/";
		$name = $_SESSION['name'];
		$name = str_replace(' ', '_', $name);
		
		$uploadfile = $uploaddir . $name;
		$ftype = exif_imagetype($_FILES['image']['tmp_name']);
		if ($ftype >= 1 && $ftype <= 18) {
			if (move_uploaded_file($_FILES['image']['tmp_name'], $uploadfile))
				$status = "Profile Picture changed.";
			else {
				$status = "What are you doing?";
				$err = 1;
			}
		} else {
			$status = "File is not an image.";
			$err = 1;
		}
	} else { //Name
		$newname = $_POST["name"];
		$newname = substr($newname, 0, 32);
		
		if(preg_match('/[^a-z_\- .0-9]/i', $newname)) {
			$status = "What a weird gnome name! Please choose a more normal one next time.";
			$err = 1;
		} else {
			$status = "Enjoy your new gnome name!";
			if (file_exists("avatars/" . str_replace(' ', '_', $_SESSION['name']))) {
				rename("avatars/" . str_replace(' ', '_', $_SESSION['name']), "avatars/" . str_replace(' ', '_', $newname));
			}
			$_SESSION['name'] = $newname;
		}
	}
}
include ('header.html');
?>

<body>
	<div style="margin-left:30px; margin-top:20px; font-size: 20px; margin-bottom:10px">
		<?php
			echo '<h2 align="center" ';
			if ($err == 0) {
				echo 'style="color:green;">';
			} else {
				echo 'style="color:red;">';
			}
			
			echo $status . "</h2>";
		?>
		
		<h2>Name</h2>
		<hr>
		<p style="font-family: sans-serif; margin-top:10px">
			Aww, do you really want to change your default gnome name?
		</p>
		
		<p style="font-family: sans-serif; font-weight:700; margin-top:10px; font-size: 24px">
			Current Name: <a style="color: black; opacity: 0.6; text-decoration: none;"><?php echo $_SESSION['name'] ?></a><br>
		</p>
		
		<form action="" method="POST" style="font-family: sans-serif; font-weight:700; margin-top:10px; font-size: 24px">
			New Name: <input type="text" maxlength="32" name="name"></input>
			<input type="submit" value="Change Name"/>
		</form>
			
		<br>
		<h2>Profile Image</h2>
		<hr>
		<img src="<?php echo getImage($_SESSION['name']); ?>" style="margin-top:20px; width:256px; height:256px;">
		
		<form action="" method="POST" enctype="multipart/form-data" style="margin-top:10px;">
			<input type="file" name="image" />
			<input type="submit" value="Change Profile Picture"/>
		</form>
	</div>
</body>