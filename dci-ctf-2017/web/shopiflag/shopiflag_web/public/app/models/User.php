<?php

class User
{
    private $id;
    private $permission;
    private $name;
    private $about;

    const NO_USER          = 0;
    const GUEST            = 1;
    const MODERATOR        = 2;
    const SENIOR_MODERATOR = 3;
    const ADMIN            = 4;
    const CONNECTED        = array(1,2,3,4);

    public function __construct() {
        $this->id = isset($_SESSION['userid']) ? $_SESSION['userid'] : -1;
        $this->permission = isset($_SESSION['permission']) ? $_SESSION['permission'] : self::NO_USER;
        $this->name = isset($_SESSION['username']) ? $_SESSION['username'] : "";
        $this->about = isset($_SESSION['about']) ? $_SESSION['about'] : "";
    }

    public function hasPermission($permissions) {
        foreach ($permissions as $perm) {
            if ($perm == $this->permission) {
                return true;
            }
        }
        return false;
    }
}

