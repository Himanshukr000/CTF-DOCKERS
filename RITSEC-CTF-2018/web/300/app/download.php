<?php
if ($_SERVER['REQUEST_METHOD'] == "POST") {
    $key = $_POST['key'];

    if (strpos($key, '.') !== false) {
        $key_parts = explode(".", $key);
        $hashed_key = md5(intval($key_parts[0])) . "." . $key_parts[1];

        $path = "uploads/" . md5($_SERVER['REMOTE_ADDR']) . "/" . $hashed_key;
        if (file_exists($path)) {
            header("Content-Disposition: attachment; filename=\"" . $key . "\"");
            die(file_get_contents($path));
        } else {
            $error = "File not found!";
        }
    } else {
        $error = "Invalid key!";
    }
}
?>

<html>
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <style>
            body {
                padding-top: 70px;
            }
            
            .fineprint {
                font-size: 2px;
                color: red;
            }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                    <a class="navbar-brand" href="/">Archivr</a>
                </div>
                <div id="navbar" class="collapse navbar-collapse">
                    <ul class="nav navbar-nav">
                        <li><a href="index.php?page=home">Home</a></li>
                        <li><a href="index.php?page=upload">Upload</a></li>
                        <li class="active"><a href="index.php?page=download">Download</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container">
<?php
if (isset($error)) {
?>
            <div class="alert alert-danger" role="alert">
                <?php echo $error; ?>
            </div>
<?php
}
?>
            <h3>File Download</h3>
            <form action="index.php?page=download" method="post" enctype="multipart/form-data">
                <div class="col-xs-4">
                    <div class="form-group">
                        <label for="upload">Enter retrieval key</label>
                        <input type="text" class="form-control" id="key" name="key" placeholder="1234567">
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
                </div>
            </form>
        </div>
    </body>
</html>
