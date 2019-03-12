<?php
include "header.php";
?>
<div class="container">
<div class="jumbotron text-center">
<h3>Check out our fleet's ship archives!</h3>
<p>Ship leaderboard:</p>
<ul class="list-group" style="width: 50%; margin: auto">
    <li class="list-group-item">???</li>
    <li class="list-group-item">The Javelin</li>
    <li class="list-group-item">LWSS Rampart</li>
    <li class="list-group-item">SS Roosevelt</li>
</ul>
<br>
<form action="/index.php" method="POST">
    Ship name:
    <input type="text" name="name" placeholder="The Javelin" />
    <input type="submit" value="Retrieve ship records" />
</form>
<?php
include "db.php";

// Check if POST
if (isset($_POST['name'])) {
    $result = $conn->query("SELECT * FROM spaceships WHERE name='" . $_POST['name'] . "';");

    if(!$result) {
        echo "Something went wrong with your record query! What are you trying to do???";
    } else {
        echo "<table class=\"table table-striped table-bordered\">";
        echo "<tr>";
        echo "<th>Ship Name</th>";
        echo "<th>Confirmed Kills</th>";
        echo "<th>Captain</th>";
        echo "</tr>";
        while($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row["name"] . "</td>";
            echo "<td>" . $row["kills"] . "</td>";
            echo "<td>" . $row["captain"] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    }

}
?>
</div>
</div>
<?php include "footer.php" ?>