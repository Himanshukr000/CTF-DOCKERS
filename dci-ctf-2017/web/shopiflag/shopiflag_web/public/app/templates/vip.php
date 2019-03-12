<!DOCTYPE html>
<html>
    <head>
        <title>Shopiflag - VIP</title>
        <?php include 'head.php' ?>;
        <link rel="stylesheet" href="/assets/css/luckylock.css">
    </head>

    <body class="w3-content" style="max-width:1200px">
        <?php include 'header.php'; ?>

        <!-- Top header  -->
        <header class="w3-container w3-xlarge">
            <p class="w3-left">VIP area</p>
        </header>


        <div class="w3-row">
            <?php if (isset($_SESSION["vip"]) && $_SESSION["vip"]): ?>

                <div class="w3-row">
                    <div class="success w3-col l12 s12">
                        Welcome to the VIP area! Here is a free flag for you: DCI{wE_lIkE_uSiNg_root:root_ToO}
                    </div>
                </div>

                <div class="w3-col l3 s6">
                    <div class="w3-container">
                        <img class="w3-border" src="/assets/images/flags/hogwarts.png" style="width:100%">
                        <p>Hogwarts - HP<br><b>Out of order</b></p>
                    </div>
                    <div class="w3-container">
                        <img class="w3-border" src="/assets/images/flags/firefly.png" style="width:100%">
                        <p>Independents - Firefly<br><b>Out of order</b></p>
                    </div>
                </div>

                <div class="w3-col l3 s6">
                    <div class="w3-container">
                        <img class="w3-border" src="/assets/images/flags/noxus.png" style="width:100%">
                        <p>Noxus - LoL<br><b>Out of order</b></p>
                    </div>
                    <div class="w3-container">
                        <img class="w3-border" src="/assets/images/flags/shield.png" style="width:100%">
                        <p>Agents of SHIELD - Marvel<br><b>Out of order</b></p>
                    </div>
                </div>

                <div class="w3-col l3 s6">
                    <div class="w3-container">
                        <img class="w3-border" src="/assets/images/flags/stark.png" style="width:100%">
                        <p>House Stark - GoT<br><b>Out of order</b></p>
                    </div>
                    <div class="w3-container">
                        <img class="w3-border" src="/assets/images/flags/masseffect.png" style="width:100%">
                        <p>Systems Alliance - Mass Effect<br><b>Out of order</b></p>
                    </div>
                </div>

                <div class="w3-col l3 s6">
                    <div class="w3-container">
                        <img class="w3-border" src="/assets/images/flags/zerg.png" style="width:100%">
                        <p>Zerg - Starcraft<br><b>Out of order</b></p>
                    </div>
                </div>

            <?php else: ?>

                <p>
                    This area is restricted. Only VIP members are allowed here. If you paid for a VIP membership,
                    just enter the password we sent you in order to access the private area.
                </p>

                <div id="luckylock-form">
                    <h6>
                        This form is protected by <b>LuckyLock</b>, the safest anti-hacking authenticator on
                        the internet! We literally can't get hacked.
                    </h6>
                    <?php if ($this->data["msg"] != ""): ?>
                        <ul id="errors" class="">
                            <li id="info"><?php echo $this->data["msg"]; ?></li>
                        </ul>
                    <?php endif; ?>
                    <form method="POST" action="">
                        <p><input type="password" placeholder="Password" name="password"></p>
                        <p><input type="submit" value="Enter"/></p>
                    </form>
                </div>

            <?php endif; ?>
            </div>
            <div class="w3-col s1">&nbsp;</div>
        </div>

        <?php include 'footer.php'; ?>
    </body>
</html>