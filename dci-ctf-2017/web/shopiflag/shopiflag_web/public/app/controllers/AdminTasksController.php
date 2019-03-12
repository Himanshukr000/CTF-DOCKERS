<?php

class AdminTasksController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->queryFlag($data);

        return $data;
    }

    public function queryFlag($data) {
        // make page vulnerable to csrf
        header("Access-Control-Allow-Origin: ". ADMIN_SERVER_EXTERNAL);
        header("Access-Control-Allow-Credentials: true");

        $db = db_connect(MYSQL_DEFAULT_USERNAME, MYSQL_DEFAULT_PASSWORD);
        $data["title"]   = "Shopiflag - Admin tasks";
        $data["msg"]     = "";
        $data["msgType"] = "error";

        if ($data["user"]->hasPermission(array(User::NO_USER, User::GUEST))) {
            header('Location: /');
            exit();
        }

        if (isset($_POST["getflag"])) {
            $data["msg"] = "Only admins and Senior Moderators can access this flag.";

            if ($data["user"]->hasPermission(array(User::SENIOR_MODERATOR, User::ADMIN))) {
                $data["msg"] = "Here is your flag: " . "DCI{WeirdWayToAskForAPromotion!}";
                $data["msgType"] = "success";
            }
        }

        return $data;
    }
}