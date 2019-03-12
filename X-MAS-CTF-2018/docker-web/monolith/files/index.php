<?php
error_reporting(0);
session_start();
$interacted = false;
$guessed = 0;

if (!isset($_SESSION['streak'])) #Set New Streak
	$_SESSION['streak'] = 0;

if (isset($_GET['guess'])) {
	if ($_GET['guess'] != "") {
		$interacted = true;
		$guess = intval($_GET['guess']);
		
		function isPrime($n) {
			for($i=2; $i<=1+$n**.5; $i++) {
				if($n%$i==0) {
					return 0;
				}
			}
			return 1;
		}

		function lcg($x1, $a1, $c1, $m1){
			return ($x1 * $a1 + $c1) % $m1;
		}

		#sav
		if (!isset($_SESSION['ok'])) { //New Session
			$m = rand(pow(2,15),pow(2,16)-1);

			while(!isPrime($m))
				$m++;

			$_SESSION['m'] = $m;
			$_SESSION['a'] = rand(1,$m-1);
			$_SESSION['c'] = rand(1,$m-1);
			$_SESSION['x'] = rand(1,$m-1);
			
			$_SESSION['ok'] = true;
		}

		#Get Situation
		$x = $_SESSION['x'];
		$a = $_SESSION['a'];
		$c = $_SESSION['c'];
		$m = $_SESSION['m'];
		
		$x = lcg($x, $a, $c, $m); #Generate Next Number

		$guessed = -1;
		
		if ($guess == $x) {
			$_SESSION['streak'] += 1;
			$guessed = 1;
		} else
			$_SESSION['streak'] = 0;
		
		$_SESSION['x'] = $x;
	}
}

$streak = $_SESSION['streak'];
?>

<style>
	{ margin: 0; padding: 0; }

	html { 
		background: url('monolith.png') no-repeat center center fixed; 
		-webkit-background-size: cover;
		-moz-background-size: cover;
		-o-background-size: cover;
	}
	
	.center {
		position: absolute;
		width: 700px;
		z-index: 0;
		top: 50%;
		left: 50%;
		margin: -100px 0 0 -350px;
	}
	
	.scale {
		transform: scale(2);
	}
	
	.SubmitButton {
		background-repeat:	no-repeat;
		#border:			none;
	}
	
	.text {
		color:white;
		font-family: 'Bungee', cursive;
		text-shadow: 1px 1px #000000;
	}
</style>

<head>
<link href="https://fonts.googleapis.com/css?family=Bungee" rel="stylesheet">
</head>

<body class="scale center" align="center">
	<form>
		<p class="text" align="center" style="line-height: 0.8;">MONOLITH ACCESS POINT</p>

		<div align="center">
		<input type="text" id="guess" name="guess" maxlength="16" size="16" style="text-align:center; line-height: 0.8;" autocomplete="off">
		<input class="SubmitButton" type="submit" value="Submit">
		</div>

		<p class="text" align="center" style="line-height: 1;">
			
		<?php
			if ($interacted) echo "You Guessed: " . $guess . '<br>';
			if ($interacted) echo "The Monolith desired:<br>" . $x . "<br><br><br>";
				
			echo '<p class="text" align="center" ';
			if ($guessed == -1)
				echo 'style="line-height: 1;color:#ff6666"';
			else if ($guessed == 1)
				echo 'style="line-height: 1;color:#66ff66"';
			echo ">";
					
			if ($guessed == -1)
				echo 'Wrong guess!<br>';
			else if ($guessed == 1)
				echo 'Correct guess!<br>';
					
			echo "Streak: " . $streak;
					
			echo "</p>";
				
			echo '<p class="text" style="line-height: 1.4;" align="center">';
			if ($streak >= 20) {
				echo "Congratulations! Here's your flag:<br>";
				echo "X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}";
			}
			echo "</p>";
		?>
		</p>
	</form>
</body>