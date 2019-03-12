<?php

class SignupController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->handleSignup($data);

        return $data;
    }

    public function handleSignup($data) {
        $db = db_connect(MYSQL_DEFAULT_USERNAME, MYSQL_DEFAULT_PASSWORD);
        $data["title"]   = "Shopiflag - Signup";
        $data["msg"]     = "";
        $data["msgType"] = "error";

        if (!$data["user"]->hasPermission(array(User::NO_USER))) {
            header('Location: /');
            exit();
        }

        try {
            if (isset($_POST["username"]) && isset($_POST["signup"])) {
                if ($_POST["username"] != "") {
                    $username = $_POST["username"];
                    $password = sha1(isset($_POST["password"]) ? $_POST["password"] : "");
                    $about    = isset($_POST["about"]) ? $_POST["about"] : "";

                    $stmt = $db->prepare("SELECT * FROM users WHERE username = ?");
                    $stmt->bindParam(1, $username, PDO::PARAM_STR);
                    $stmt->execute();

                    if ($stmt->rowCount() == 0) {
                        $stmt = $db->prepare("INSERT INTO users (username, password, credit, about, permission)
                                              VALUES (?, ?, 0, ?, 1)");
                        $stmt->bindParam(1, $username, PDO::PARAM_STR);
                        $stmt->bindParam(2, $password, PDO::PARAM_STR);
                        $stmt->bindParam(3, $about, PDO::PARAM_STR);
                        $stmt->execute();
                        $data['msg']     = "Registration successful.";
                        $data['msgType'] = "success";
                    } else {
                        $data['msg'] = "Username is already taken.";
                    }
                } else {
                    $data['msg'] = "Username is required.";
                }
            }
        } catch (PDOException $e) {
            $data['msg'] = $e->getMessage();
        }

        return $data;
    }
}