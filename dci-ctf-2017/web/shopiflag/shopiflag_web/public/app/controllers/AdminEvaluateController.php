<?php

class AdminEvaluateController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->querySubmission($data);

        return $data;
    }

    public function querySubmission($data) {
        $db = db_connect(MYSQL_DEFAULT_USERNAME, MYSQL_DEFAULT_PASSWORD);
        $data["title"]   = "Shopiflag - Admin Evaluate";
        $data["msg"]     = "";
        $data["msgType"] = "error";
        $data["archive"] = array();

        if ($data["user"]->hasPermission(array(User::NO_USER, User::GUEST))) {
            header('Location: /');
            exit();
        }

        if (isset($_POST["id"])) {
            $stmt = $db->prepare("SELECT * FROM flag_submissions WHERE id = ?");
            $stmt->bindParam(1, $_POST["id"], PDO::PARAM_INT);
            $stmt->execute();

            $data["archive"] = $stmt->fetchAll(PDO::FETCH_ASSOC);
            if (count($data["archive"]) != 1) {
                $data["msg"] = "No archived submission exists with this ID #.";
            }
        }

        return $data;
    }
}