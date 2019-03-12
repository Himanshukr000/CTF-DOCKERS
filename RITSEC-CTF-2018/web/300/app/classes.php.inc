<?php

class DirLister {
    function __construct($dir) {
        $this->dir = $dir;
        $this->files = array_values(preg_grep('/^([^.])/', scandir($dir)));
    }

    function getOldestFile() {
        $min = array('fname' => "", 'mtime' => -1);
        foreach ($this->files as $file) {
            $fmtime = filemtime($this->dir . "/" . $file);
            if ($min['mtime'] == -1 || $fmtime < $min['mtime']) {
                $min['fname'] = $file;
                $min['mtime'] = $fmtime;
            }
        }
        return $min['fname'];
    }

    function getCount() {
        return count($this->files);
    }

    function __wakeup() {
        echo print_r($this->files);
    }
}

?>
