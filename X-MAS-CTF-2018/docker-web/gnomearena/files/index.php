<?php
include ('engine.php');
include ('header.html');
?>

<head>
<link href="https://fonts.googleapis.com/css?family=Acme" rel="stylesheet">
</head>

<style>
.rainbow {
	text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
	font-size:40px;
	animation: rainbow 6s infinite; 
}

@keyframes rainbow{
	0%{color: #FF4242;}	
	20%{color: #FFFF42;}	
	40%{color: #42FF42;}
	60%{color: #42A0FF;}
	80%{color: #FF42FF;}
	100%{color: #FF4242;}
}

div.alive {
	transform: scale(1);
	transition: transform .25s ease;
}

div.clickable {
	cursor:pointer;
	transition: transform .25s ease;
}
div.clickable:hover {
	transform: scale(1.05);
}

div.kill {
	transform: scale(0);
	transition: transform .25s ease;
}
div.kill:hover {
	transform: scale(0);
}

.obj {
	position: fixed;
	top: 50%;
    left: 50%;
}

#rock {
	background-image: url('img/rock.png');
	width:256px;
	height:256px;
}
.cont-right {
	transform: translate(-420px, 40px);
}

#paper {
	background-image: url('img/paper.png');
	width:256px;
	height:256px;
}
.cont-center {
	transform: translate(-128px, 40px);
}

#scissors {
	background-image: url('img/scissors.png');
	width:256px;
	height:256px;
}
.cont-left {
	#transform: translate(163px, 40px);
}

.centered {
    transform: translate(-50%, -50%);
}
</style>

<script>
//RPS thing
function startGame() {
	document.getElementById("startButton").classList.add("kill");
	document.getElementById("startText").classList.add("kill");
	setTimeout(spawnMenu, 200);
}

function delID(id) {
	var elem = document.getElementById(id);
	elem.parentNode.removeChild(elem);
}

function spawnMenu () {
	delID("start");
	document.getElementById("menu").className = "alive";
}

var ourchoice = 0;
var theirchoice = 0;

function chosen(type) {
	var rock = document.getElementById('rock');
	var paper = document.getElementById('paper');
	var scissors = document.getElementById('scissors');
	var txt = "You chose: <b>";
	
	ourchoice = type;
	if (type == 0) { //Rock
		rock.classList.add("kill");
		paper.setAttribute('onclick', "");
		scissors.setAttribute('onclick', "");
		
		txt += "Rock!";
	} else if (type == 1) { //Paper
		rock.setAttribute('onclick', "");
		paper.classList.add("kill");
		scissors.setAttribute('onclick', "");
		
		txt += "Paper!";
	} else if (type == 2) { //Scissors
		paper.setAttribute('onclick', "");
		scissors.classList.add("kill");
		rock.setAttribute('onclick', "");
		
		txt += "Scissors!";
	}
	
	txt += "</b>";
	
	var choicetext = document.createElement("h2");
	choicetext.innerHTML = txt;
	
	attr = document.createAttribute("align");
	attr.value = "center";
	choicetext.setAttributeNode(attr);
	
	style = document.createAttribute("style");
	choicetext.setAttributeNode(style);
	
	choicetext.setAttribute("style", "opacity: 0.6;");
	
	document.body.appendChild(choicetext);
	setTimeout(EnemyProcess, 200);
}

function EnemyProcess () {
	rock.classList.add("kill");
	paper.classList.add("kill");
	scissors.classList.add("kill");
	
	setTimeout(Enemy, 150);
}

function Enemy () {
	var enemytext = document.createElement("h2");
	enemytext.innerHTML = "Enemy Chose: <b>";
	var choice = Math.floor(Math.random() * 3);
	
	theirchoice = choice;
	if (choice == 0) {
		enemytext.innerHTML += "Rock!</b>";
	} else if (choice == 1) {
		enemytext.innerHTML += "Paper!</b>";
	} else if (choice == 2) {
		enemytext.innerHTML += "Scissors!</b>";
	}
	
	attr = document.createAttribute("align");
	attr.value = "center";
	attr2 = document.createAttribute("id");
	attr2.value = "center";
	style = document.createAttribute("style");
	enemytext.setAttributeNode(style);
	enemytext.setAttributeNode(attr);
	
	enemytext.setAttribute("style", "opacity: 0.8; margin-top:75px; font-size: 48px;");
	document.body.appendChild(enemytext);
	
	PrintResult();
}

function PrintResult () {
	var text = document.createElement("h2");
	attr = document.createAttribute("align");
	style = document.createAttribute("style");
	text.setAttributeNode(style);
	text.setAttributeNode(attr);
	text.setAttribute("style", "margin-top:25px; font-size: 48px;");
	
	attr.value = "center";
	var win = 0;
	
	var _0x3eec=["\x69\x6E\x6E\x65\x72\x48\x54\x4D\x4C","\x49\x74\x27\x73\x20\x61\x20\x74\x69\x65\x21","\x59\x6F\x75\x20\x77\x6F\x6E\x21","\x73\x74\x79\x6C\x65","\x63\x6F\x6C\x6F\x72\x3A\x20\x23\x33\x44\x45\x35\x33\x44\x3B\x20\x6D\x61\x72\x67\x69\x6E\x2D\x74\x6F\x70\x3A\x32\x35\x70\x78\x3B\x20\x66\x6F\x6E\x74\x2D\x73\x69\x7A\x65\x3A\x20\x34\x38\x70\x78\x3B","\x73\x65\x74\x41\x74\x74\x72\x69\x62\x75\x74\x65","\x59\x6F\x75\x20\x6C\x6F\x73\x74\x21","\x63\x6F\x6C\x6F\x72\x3A\x20\x23\x45\x35\x33\x42\x33\x42\x3B\x20\x3B\x6D\x61\x72\x67\x69\x6E\x2D\x74\x6F\x70\x3A\x32\x35\x70\x78\x3B\x20\x66\x6F\x6E\x74\x2D\x73\x69\x7A\x65\x3A\x20\x34\x38\x70\x78\x3B"];if(ourchoice== theirchoice){text[_0x3eec[0]]= _0x3eec[1]}else {if(ourchoice== 0){if(theirchoice== 1){win= 0}else {win= 1}}else {if(ourchoice== 1){if(theirchoice== 0){win= 1}else {win= 0}}else {if(theirchoice== 1){win= 1}else {win= 0}}};if(win== 1){text[_0x3eec[0]]= _0x3eec[2];text[_0x3eec[5]](_0x3eec[3],_0x3eec[4])}else {text[_0x3eec[0]]= _0x3eec[6];text[_0x3eec[5]](_0x3eec[3],_0x3eec[7])}}
	
	document.body.appendChild(text);
	
	document.getElementById("resetButton").className = "alive clickable";
}
</script>

<body>
	<div align="center">
		<h2 style="margin-top:32px; font-family: 'Acme'; font-size:50px">Welcome back to Gnome Arena,</h2>
		<h2 style="font-family: 'Acme'; font-size:36px"> <?php echo $_SESSION['name']?></h2>
		<div id="menu" class="kill" style="font-family: 'Acme'; font-size:36px; margin-top:40px">
			Choose your Weapon:
			<div style="margin-top:20px;">
				<div class="cont-right">
					<div class="obj clickable" id="rock" onclick="chosen(0)" style="color:white;">Rock</div>
				</div>
				
				<div class="cont-center">
					<div class="obj clickable" id="paper" onclick="chosen(1)">Paper</div>
				</div>
				
				<div class="cont-left">
					<div class="obj clickable" style="margin-top:83px; margin-left: 165px; color:white;" id="scissors" onclick="chosen(2)">Scissors</div>
				</div>
			</div>
		</div>
		
		<div id="start" class="obj centered" style="height: 256px;">
			<div id="startButton" class="alive clickable" style="width: 256px; height: 256px; background-image: url('img/RPS.png');" onclick="startGame();">
			</div>
			<h2 id="startText" class="rainbow" style="margin-top:42px; font-family: 'Acme'; font-size:42px">Play Rock Paper Scissors now!</h2>
		</div>
		
		<div class="obj centered" style="position:absolute; margin-top:200px;">
			<div id="resetButton" class="kill clickable" style="background-image: url('img/playagain.png');height:60; width:120;background-size: cover; background-repeat: no-repeat; background-position: center center;" onclick="location.reload();"></div>
		</div>
	</div>
</body>