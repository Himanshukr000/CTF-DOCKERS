<?php

class AdminColleaguesController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->queryColleagues($data);

        return $data;
    }

    public function queryColleagues($data) {
        $db = db_connect(MYSQL_SQL2_USERNAME, MYSQL_SQL2_PASSWORD);
        $data["title"]      = "Shopiflag - Admin Colleagues";
        $data["moderators"] = array();

        if ($data["user"]->hasPermission(array(User::NO_USER, User::GUEST))) {
            header('Location: /');
            exit();
        }

        $permission = isset($_POST["permission"]) ? $_POST["permission"] : 2; // by default, show moderators
        $sql = "SELECT * FROM moderators WHERE permission = $permission";
        $data["moderators"] = $db->query($sql)->fetchAll();

        return $data;
    }
}