<?php

class Page
{
    private $content;

    public function __construct($content) {
        $this->content = $content;
    }

    public function show() {
        echo $content;
    }
}