<?php
require_once('db-connect.php');

if (!isset($_SESSION["rank"]) || $_SESSION["rank"] < 3)
{
    die();
}

$reason = "";

$stmt = $db->prepare("SELECT * FROM promotion_requests LIMIT 1");
$stmt->execute();

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
if (count($result) == 1)
{
    $reason = $result[0]["reason"];
    $stmt = $db->prepare("DELETE FROM promotion_requests WHERE id = ?");
    $stmt->bindParam(1, $result[0]["id"], PDO::PARAM_INT);
    $stmt->execute();
}
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Admin Email Webservice</title>
    </head>
    <body>
        <!-- Top header  -->
        <header class="w3-container w3-xlarge">
            <p class="w3-left">Admin</p>
        </header>

        <div class="w3-row-padding">
            <div class="w3-col s3">&nbsp;</div>
            <div class="w3-col s6">
                <?php echo $reason; ?>
            </div>
            <div class="w3-col s3">&nbsp;</div>
        </div>
        <div class="w3-row"><div class="w3-col s12">&nbsp;</div></div>
    </body>
</html>