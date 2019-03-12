<?php

class AdminPromotionController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->queryColleagues($data);

        return $data;
    }

    public function queryColleagues($data) {
        $db = db_connect(MYSQL_DEFAULT_USERNAME, MYSQL_DEFAULT_PASSWORD);
        $data["title"]   = "Shopiflag - Admin tasks";
        $data["msg"]     = "";
        $data["msgType"] = "error";

        if ($data["user"]->hasPermission(array(User::NO_USER, User::GUEST))) {
            header('Location: /');
            exit();
        }

        if (isset($_POST["reason"])) {
            if ($_POST["reason"] != "") {
                if (!preg_match('/<.*?>/s', $_POST["reason"])) {
                    $data["msg"] = "Your request was sent. Good luck!";
                    $data["msgType"] = "success";

                    $stmt = $db->prepare("INSERT INTO promotion_requests (reason) VALUES (?)");
                    $stmt->bindParam(1, $_POST["reason"], PDO::PARAM_STR);
                    $stmt->execute();
                } else {
                    $data["msg"] .= "For security reasons, your text can't have any characters inside '<' and '>'</br>";
                    $data["msg"] .= "'> example 1 >' => OK!</br>";
                    $data["msg"] .= "'< example 2 <' => OK!</br>";
                    $data["msg"] .= "'> example 3 <' => OK!</br>";
                    $data["msg"] .= "'< example 3 >' => NOT OK!</br>";
                }
            } else {
                $data["msg"] = "You can't leave the textarea empty if you want a promotion, dummy.";
            }
        }

        return $data;
    }
}