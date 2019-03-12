<?php

class AccountSettingsController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->handleNameChange($data);

        return $data;
    }

    public function handleNameChange($data) {
        $db = db_connect(MYSQL_DEFAULT_USERNAME, MYSQL_DEFAULT_PASSWORD);
        $data["title"]   = "Shopiflag - Account";
        $data["msg"]     = "";
        $data["msgType"] = "error";

        if (!$data["user"]->hasPermission(User::CONNECTED)) {
            header('Location: /');
            exit();
        }

        try {
            if (isset($_POST["newusername"]) && isset($_POST["change"])) {
                if ($_SESSION["permission"] != 1) {
                    $data["msg"] = "Only normal users are allowed to change their name.";
                } else if ($_POST["newusername"] == "") {
                    $data["msg"] = "New username is required.";
                } else {
                    $stmt = $db->prepare("SELECT * FROM users WHERE username = ?");
                    $stmt->bindParam(1, $_POST["newusername"], PDO::PARAM_STR);
                    $stmt->execute();

                    if ($stmt->rowCount() == 0) {
                        $stmt = $db->prepare("UPDATE users SET username = ? WHERE id = ?");
                        $stmt->bindParam(1, $_POST["newusername"], PDO::PARAM_STR);
                        $stmt->bindParam(2, $_SESSION["userid"], PDO::PARAM_INT);
                        $stmt->execute();

                        $stmt = $db->prepare("SELECT * FROM users WHERE id = ?");
                        $stmt->bindParam(1, $_SESSION["userid"], PDO::PARAM_INT);
                        $stmt->execute();
                        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
                        $_SESSION["username"]   = $result[0]["username"];

                        $data["msg"]     = "Modification successful.";
                        $data["msgType"] = "success";
                    } else {
                        $data["msg"] = "Username is already taken.";
                    }
                }
            }
        } catch (PDOException $e) {
            $data["msg"] = $e->getMessage();
        }

        return $data;
    }
}