<?php

class Router
{
    private $module;

    public function __construct($url) {

        // remove GET parameters from request before evaluating
        $pos = strpos($url, "?");
        if ($pos) {
            $url = substr($url, 0, $pos);
        }
        $url = strtolower($url);

        switch ($url)
        {
            case "/":
            case "/home":
                $this->module = "Home";             break;

            case "/login":
                $this->module = "Login";            break;

            case "/signup":
                $this->module = "Signup";           break;

            case "/account/inbox":
                $this->module = "AccountInbox";     break;

            case "/account/settings":
                $this->module = "AccountSettings";  break;

            case "/account/logout":
                $this->module = "AccountLogout";    break;

            case "/shop/sell":
                $this->module = "ShopSell";         break;

            case "/shop/buy":
                $this->module = "ShopBuy";          break;

            case "/vip":
                $this->module = "VIP";              break;

            case "/admin/tasks":
                $this->module = "AdminTasks";       break;

            case "/admin/evaluate":
                $this->module = "AdminEvaluate";    break;

            case "/admin/colleagues":
                $this->module = "AdminColleagues";  break;

            case "/admin/promotion":
                $this->module = "AdminPromotion";   break;

            // for xss bot
            case "/admin/flag-check":
                $this->module = "FlagCheck";        break;

            default:
                $this->module = "Error404";         break;
        }
    }

    public function getModule() {
        return $this->module;
    }
}