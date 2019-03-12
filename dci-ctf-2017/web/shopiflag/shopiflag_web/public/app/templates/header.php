<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-bar-block w3-white w3-collapse w3-top" style="z-index:3;width:250px" id="mySidebar">
    <div class="w3-container w3-display-container w3-padding-16">
        <i onclick="w3_close()" class="fa fa-remove w3-hide-large w3-button w3-display-topright"></i>
        <h3 class="w3-wide"><b>SHOPIFLAG</b></h3>
    </div>
    <div class="w3-padding-64 w3-large w3-text-grey" style="font-weight:bold">
    <?php if (isset($_SESSION["userid"])): ?>
        <span class="w3-bar-item"><b>Welcome, <?php echo htmlspecialchars($_SESSION["username"]); ?>!</b></span>
    <?php endif; ?>
        <a href="/" class="w3-bar-item w3-button">Home</a>
    <?php if (isset($_SESSION["permission"]) && $_SESSION["permission"] >= 2): ?>
        <a onclick="myDashFunc()" href="javascript:void(0)" class="w3-button w3-block w3-left-align">
            Dashboard <i class="fa fa-caret-down"></i>
        </a>
        <div id="dash_items" class="w3-bar-block w3-hide w3-padding-large w3-medium">
            <a href="/admin/tasks" class="w3-bar-item w3-button">Tasks & privileges</a>
            <a href="/admin/evaluate" class="w3-bar-item w3-button">Evaluate submissions</a>
            <a href="/admin/colleagues" class="w3-bar-item w3-button">Colleagues</a>
            <a href="/admin/promotion" class="w3-bar-item w3-button">Ask for promotion</a>
        </div>
    <?php endif; ?>
        <a onclick="myShopFunc()" href="javascript:void(0)" class="w3-button w3-block w3-left-align">
            Shop <i class="fa fa-caret-down"></i>
        </a>
        <div id="shop_items" class="w3-bar-block w3-hide w3-padding-large w3-medium">
            <a href="/shop/buy" class="w3-bar-item w3-button">Buy</a>
            <a href="/shop/sell" class="w3-bar-item w3-button">Sell</a>
        </div>
    <?php if (!isset($_SESSION["userid"])): ?>
        <a href="/login" class="w3-bar-item w3-button">Login</a>
        <a href="/signup" class="w3-bar-item w3-button">Sign up</a>
    <?php else: ?>
        <a onclick="myAccFunc()" href="javascript:void(0)" class="w3-button w3-block w3-left-align">
            Account <i class="fa fa-caret-down"></i>
        </a>
        <div id="account_items" class="w3-bar-block w3-hide w3-padding-large w3-medium">
            <a href="/account/inbox" class="w3-bar-item w3-button">Inbox</a>
            <a href="/account/settings" class="w3-bar-item w3-button">Settings</a>
            <a href="/account/logout" class="w3-bar-item w3-button">Logout</a>
        </div>
    <?php endif; ?>
        <a href="/vip" class="w3-bar-item w3-button">VIP Area</a>
    </div>
</nav>

<!-- Top menu on small screens -->
<header class="w3-bar w3-top w3-hide-large w3-black w3-xlarge">
    <div class="w3-bar-item w3-padding-24 w3-wide">SHOPIFLAG</div>
    <a href="javascript:void(0)" class="w3-bar-item w3-button w3-padding-24 w3-right" onclick="w3_open()"><i class="fa fa-bars"></i></a>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:250px">

    <!-- Push down content on small screens -->
    <div class="w3-hide-large" style="margin-top:83px"></div>
