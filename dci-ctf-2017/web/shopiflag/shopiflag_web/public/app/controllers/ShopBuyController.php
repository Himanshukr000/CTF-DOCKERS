<?php

class ShopBuyController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->handleBuy($data);

        return $data;
    }

    public function handleBuy($data) {
        $db = db_connect(MYSQL_SQL1_USERNAME, MYSQL_SQL1_PASSWORD);
        $data["title"]   = "Shopiflag - Buy";
        $data["msg"]     = "";
        $data["msgType"] = "error";

        try {
            if (isset($_POST["buy1"]) || isset($_POST["buy2"])) {

                $flag  = isset($_POST["buy1"]) ? 'DCI{_Flags_are_better_than_Ca$h}' :
                                                 'DCI{Wo0w_are_you_the_Bill_Gates}';
                $price = isset($_POST["buy1"]) ? 999 : 999999;

                if (isset($_SESSION["userid"])) {
                    $username = $_SESSION["username"];
                    $sql = "SELECT credit FROM users WHERE username = '$username'";
                    $credit = $db->query($sql)->fetch()["credit"];

                    if ($credit >= $price) {
                        $data["msg"] = 'Thank you for your purchase. Here is your flag: '. $flag;
                        $data["msgType"] = "success";
                    } else {
                        $data["msg"] = "Sorry " . $username . ", you don't have enough credit (".$credit.") to buy this flag.";
                    }
                } else {
                    $data["msg"] = "You need to be logged in to make a purchase.";
                }
            }
        } catch (PDOException $e) {
            $data["msg"] = $e->getMessage();
        }

        return $data;
    }
}