<?php

class Error404Controller extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data["title"] = "Shopiflag - 404";

        return $data;
    }
}