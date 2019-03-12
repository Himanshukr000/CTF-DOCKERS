<?
if(eregi("admin",$_GET[id])) {
  echo("<p>not allowed!</p>");
  exit();
}

$_GET[id] = urldecode($_GET[id]);
if($_GET[id] == "admin")
{
  echo "<p>Access granted!</p>";
  echo "<p>Key: b4cc845aa05ed9b0ce823cb04f253e27 </p>";
}
?>


<br><br>
Can you authenticate to this website?
<!-- source: index.phps -->
