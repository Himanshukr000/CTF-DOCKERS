<?php

class VIPController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->handleVIP($data);

        return $data;
    }

    public function handleVIP($data) {
        $data["title"]   = "Shopiflag - VIP";
        $data["msg"]     = "";
        $_SESSION["vip"] = isset($_SESSION["vip"]) ? $_SESSION["vip"] : false;

        if (isset($_POST['password'])) {
            // IMPORTANT: CHANGE DEFAULT CREDENTIALS WHEN USING THIS CODE!
            if ($_POST['password'] === 'luckylock-default-password') {
                $_SESSION["vip"] = true;
            } else {
                $data["msg"] = "Stop trying to hack us. It's 100% impossible.";
            }
        }

        return $data;
    }
}