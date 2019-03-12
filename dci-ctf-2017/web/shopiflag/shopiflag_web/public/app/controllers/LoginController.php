<?php

class LoginController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->handleLogin($data);

        return $data;
    }

    public function handleLogin($data) {
        $db = db_connect(MYSQL_DEFAULT_USERNAME, MYSQL_DEFAULT_PASSWORD);
        $data["title"]   = "Shopiflag - Login";
        $data["msg"]     = "";
        $data["msgType"] = "error";

        if (!$data["user"]->hasPermission(array(User::NO_USER))) {
            header('Location: /');
            exit();
        }

        try {
            if (isset($_POST["login"])) {
                $username = isset($_POST["username"]) ? $_POST["username"] : "";
                $password = sha1(isset($_POST["password"]) ? $_POST["password"] : "");

                $stmt = $db->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
                $stmt->bindParam(1, $username, PDO::PARAM_STR);
                $stmt->bindParam(2, $password, PDO::PARAM_STR);
                $stmt->execute();

                $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
                if (count($result) == 1) {
                    $_SESSION["userid"]   = $result[0]["id"];
                    $_SESSION["username"] = $result[0]["username"];
                    $_SESSION["permission"] = $result[0]["permission"];
                    $_SESSION["about"] = $result[0]["about"];
                    header('Location: /account/settings');
                    exit();
                } else {
                    $data['msg'] = "Wrong credentials.";
                }
            }
        } catch (PDOException $e) {
            $data['msg'] = $e->getMessage();
        }

        return $data;
    }
}