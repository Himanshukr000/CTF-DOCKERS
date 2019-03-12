<?php

class ShopSellController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data = $this->handleSell($data);

        return $data;
    }

    public function handleSell($data) {
        $db = db_connect(MYSQL_DEFAULT_USERNAME, MYSQL_DEFAULT_PASSWORD);
        $data["title"]   = "Shopiflag - Sell";
        $data["msg"]     = "";
        $data["msgType"] = "";
        $save_path       = "";

        if (isset($_POST["submit"])) {
            if (!$data["user"]->hasPermission(array(User::GUEST))) {
                $data["msg"] .= "- You need to be logged in as a regular user to make a submission.</br>";
            }

            if (!isset($_POST["region"])) {
                $data["msg"] .= "- The region of your flag is required.</br>";
            }

            if (!isset($_POST["price"]) || !is_numeric($_POST["price"]) || $_POST["price"] <= 0) {
                $data["msg"] .= "- The price of your flag is required to be a valid positive number.</br>";
            }

            if (!isset($_FILES["flag"])) {
                $data["msg"] .= "- You need to upload an image for your flag.</br>";
            }

            // file upload is handled by admin server
            if (isset($_FILES["flag"])) {
                if ($data["msg"] == "") {
                    $data["msgType"] = "success";
                }

                // add .jpg for "extra security"
                $filename = $_FILES['flag']['name'] .".jpg";

                // sudo apt-get install php-curl
                $options = array(
                    CURLOPT_URL => ADMIN_SERVER_LOCAL . "/upload-file.php",
                    CURLOPT_RETURNTRANSFER => TRUE,
                    CURLOPT_POSTFIELDS => array(
                        'flag' => curl_file_create($_FILES['flag']['tmp_name'], 'image/jpeg', $filename),
                        'msg'  => $data["msg"]
                    ),
                );
                $ch = curl_init();
                curl_setopt_array($ch, $options);
                $response = curl_exec($ch);
                $response = json_decode($response, true);
                curl_close($ch);

                if ($response == "") {
                    die("This is NOT part of the CTF: Please send an email at dci@aeets.com about this error.");
                }

                if ($response["msgType"] != "success") {
                    $data["msg"]     = $response["msg"];
                    $data["msgType"] = "error";
                } else {
                    $save_path = $response["msg"];
                }
            }

            try {
                // submission successful
                if ($data["msgType"] == "success") {
                    // Make sure id is random-ish and unique
                    $id        = 0;
                    $rowsCount = 1;
                    do {
                        $id = mt_rand(0, 2147483647);
                        $stmt = $db->prepare("SELECT * FROM flag_submissions WHERE id = ?");
                        $stmt->bindParam(1, $id, PDO::PARAM_INT);
                        $stmt->execute();
                        $rowsCount = $stmt->rowCount();
                    } while($rowsCount > 0);

                    // insert submission in database
                    $stmt = $db->prepare("INSERT INTO flag_submissions (id, user_id, image_url, region, price, status)
                                          VALUES (?, ?, ?, ?, ?, 'pending')");
                    $stmt->bindParam(1, $id, PDO::PARAM_INT);
                    $stmt->bindParam(2, $_SESSION["userid"], PDO::PARAM_INT);
                    $stmt->bindParam(3, $save_path, PDO::PARAM_STR);
                    $stmt->bindParam(4, $_POST["region"], PDO::PARAM_STR);
                    $stmt->bindParam(5, $_POST["price"], PDO::PARAM_INT);
                    $stmt->execute();

                    $data["msg"]  = "Your flag was correctly sent! The submission id is " . $id . ".</br>";
                    $data["msg"] .= "Check your inbox to see if it was approved or not.";
                }
            } catch (PDOException $e) {
                $data['msg'] = $e->getMessage();
                $data["msgType"] = "error";
            }
        }

        return $data;
    }
}