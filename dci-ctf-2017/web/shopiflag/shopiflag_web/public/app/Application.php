<?php

class Application
{
    private $controller;
    private $view;

    public function __construct($url) {
        $router = new Router($url);
        $module = $router->getModule();

        $controllerName = $module . "Controller";
        $viewName = $module . "View";
        $this->controller = new $controllerName();
        $this->view = new $viewName();
    }

    public function execute() {
        $data = $this->controller->processRequest();
        $this->view->setData($data);
        $this->view->show(array());
    }
}