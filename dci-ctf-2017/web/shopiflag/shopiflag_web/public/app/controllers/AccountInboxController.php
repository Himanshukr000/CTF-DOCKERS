<?php

class AccountInboxController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->queryMails($data);

        return $data;
    }

    public function queryMails($data) {
        $db = db_connect(MYSQL_DEFAULT_USERNAME, MYSQL_DEFAULT_PASSWORD);
        $data["title"]   = "Shopiflag - Inbox";
        $data["msg"]     = "";
        $data["msgType"] = "error";
        $data["mails"]   = array();
        $data["date"]    = new DateTime();

        if (!$data["user"]->hasPermission(User::CONNECTED)) {
            header('Location: /');
            exit();
        }

        try {
            $stmt = $db->prepare("SELECT * FROM mails WHERE to_id = ?");
            $stmt->bindParam(1, $_SESSION["userid"], PDO::PARAM_INT);
            $stmt->execute();
            $data["mails"] = $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            $data["msg"] = $e->getMessage();
        }

        return $data;
    }
}