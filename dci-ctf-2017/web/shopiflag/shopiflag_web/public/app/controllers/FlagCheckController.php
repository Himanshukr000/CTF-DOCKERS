<?php

class FlagCheckController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->showFlag($data);

        return $data;
    }

    public function showFlag($data) {
        $db = db_connect(MYSQL_DEFAULT_USERNAME, MYSQL_DEFAULT_PASSWORD);
        $data["title"]   = "Shopiflag - Evaluate";
        $data["image"]   = "";
        $data["region"]  = "";
        $data["price"]   = "";

        $session_id = session_id();
        if ($session_id != MODERATOR_PHPSESSID) {
            header('Location: /');
            exit();
        }

        $stmt = $db->prepare("SELECT * FROM flag_submissions WHERE status = 'pending'");
        $stmt->execute();
        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

        if (count($result) > 0) {
            $id = $result[0]["id"];
            $data["image"]  = $result[0]["image_url"];
            $data["region"] = $result[0]["region"];
            $data["price"]  = $result[0]["price"];

            // Create email
            $reasons = array("You suck", "I don't like you", "That was the worst flag I've ever seen",
                             "I would prefer to become blind than see your flag again",
                             "Nobody would want to buy this crap", "You make me sick");

            $subject  = "Submission id #" . $result[0]["id"];
            $content  = "We regret to inform you that your submission has been rejected.</br>";
            $content .= "Reason: " . $reasons[rand(0, 5)] . ".";

            $from = 'John The Moderator';
            $now = time();

            $stmt = $db->prepare("INSERT INTO mails (to_id, from_username, subject, content, sent_time)
                                  VALUES (?, ?, ?, ?, ?)");
            $stmt->bindParam(1, $result[0]["user_id"], PDO::PARAM_INT);
            $stmt->bindParam(2, $from, PDO::PARAM_STR);
            $stmt->bindParam(3, $subject, PDO::PARAM_STR);
            $stmt->bindParam(4, $content, PDO::PARAM_STR);
            $stmt->bindParam(5, $now, PDO::PARAM_INT);
            $stmt->execute();

            $stmt = $db->prepare("UPDATE flag_submissions SET status = 'rejected' WHERE id = ?");
            $stmt->bindParam(1, $id, PDO::PARAM_INT);
            $stmt->execute();
        }

        return $data;
    }
}