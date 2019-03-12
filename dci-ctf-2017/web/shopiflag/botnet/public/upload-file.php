<?php

$response = array("msg" => "Missing data.", "msgType" => "error");

if (!file_exists('uploads')) {
    mkdir('uploads', 0777, true); // make sure upload directory exists
}

try {
    if (isset($_FILES["flag"]) && isset($_POST["msg"]))
    {
        $response["msg"] = $_POST["msg"];

        $target_dir = "uploads/";
        $target_file = $target_dir . basename($_FILES["flag"]["tmp_name"]) . '_' . basename($_FILES["flag"]["name"]);
        $check = getimagesize($_FILES["flag"]["tmp_name"]); 

        if ($check == FALSE) {
            $response["msg"] .= "- The uploaded file needs to be an image.";
        } else if (!isset($check[0]) || $check[0] != 600 || !isset($check[1]) || $check[1] != 300) {
            $response["msg"] .= "- The image needs to be 600px wide and 300px high.";
        }

        if ($response["msg"] == "") {
            // before uploading, only keep the first 255 charcters otherwise it breaks file_upload
            $target_file = substr($target_file, 0, 30);
            move_uploaded_file($_FILES["flag"]["tmp_name"], $target_file);
            $response["msg"]     = $target_file;
            $response["msgType"] = "success";
        }
    }
} catch (Exception $e) {
    $response['msg'] = $e->getMessage();
    $response["msgType"] = "error";
}

echo json_encode($response);