<?php

class HomeController extends Controller
{
    public function processRequest() {
        $data = parent::processRequest();

        // process request here
        $data["title"] = "Shopiflag - Home";

        return $data;
    }
}