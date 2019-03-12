<?php
//$flag = fopen("flag.php", "rb");
header('X-Flag: you wish it was that easy');

if (isset($_SERVER['HTTP_REFERER']))  {
    $filename = $_SERVER['HTTP_REFERER'];
    $filename = preg_replace('/[.]+\//', '', $filename);
    if (strpos($filename, 'flag.php') === 0) {
        echo "<html>not going to make it that easy for you</html>";
    } else {
        $file = fopen($filename, 'rb');
        $file_contents = stream_get_contents($file);
        echo $file_contents;
    }
} else {
    ?>
    <html>
        <iframe id="video" src="//www.youtube.com/embed/VcDy8HEg1QY?rel=0&autoplay=1" frameborder="0" allowfullscreen style="width:100%; height:100%;"></iframe>
    </html>
    <?php
}
?>
