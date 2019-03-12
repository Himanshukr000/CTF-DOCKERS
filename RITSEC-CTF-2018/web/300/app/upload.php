<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if ($_FILES['upload']['size'] > 5000) { //max 5KB
        die("File too large!");
    }
    $filename = $_FILES['upload']['name'];


    $upload_time = time();
    $upload_dir = "uploads/" . md5($_SERVER['REMOTE_ADDR']) . "/";

    $ext = "";
    if (strpos($filename, '.') !== false) {
        $f_ext = explode(".", $filename)[1];
        if (ctype_alnum($f_ext) && stripos($f_ext, "php") === false && stripos($f_ext, "pht") === false) {
            $ext = "." . $f_ext;
        } else {
            $ext = ".dat";
        }
    } else {
        $ext = ".dat";
    }

    $upload_path = $upload_dir . md5($upload_time) . $ext;
    mkdir($upload_dir, 0770, true);

    //Enforce maximum of 10 files
    $dir = new DirLister($upload_dir);
    if ($dir->getCount() >= 10) {
        unlink($upload_dir . $dir->getOldestFile());
    }

    move_uploaded_file($_FILES['upload']['tmp_name'], $upload_path);
    $key = $upload_time . $ext;
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
                        <li class="active"><a href="index.php?page=upload">Upload</a></li>
                        <li><a href="index.php?page=download">Download</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container">
<?php
if (isset($key)) {
?>
            <div class="alert alert-success" role="alert">
                File uploaded! Retrieval key: <strong><?php echo $key; ?></strong>
            </div>
<?php
}
?>
            <h3>File Upload</h3>
            <form action="index.php?page=upload" method="post" enctype="multipart/form-data">
                <div class="col-xs-4">
                    <div class="form-group">
                        <label for="upload">Select a &lt;5KB file</label>
                        <input type="file" class="form-control-file" id="upload" name="upload">
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary">Upload</button>
                    </div>
                </div>
            </form>
        </div>
    </body>
</html>
