<?php

abstract class View
{
    protected $content;
    protected $data;

    public function show($templates) {
        foreach ($templates as $key => $template) {
            ob_start();
            include('app/templates/'.$template);
            $this->data[$key] = ob_get_contents();
            ob_end_clean();  
        }

        echo $this->data['content'];
    }

    public function setData($data) {
        $this->data = $data;
    }
}