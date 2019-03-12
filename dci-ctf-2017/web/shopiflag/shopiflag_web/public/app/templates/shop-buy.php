<!-- Top header  -->
<header class="w3-container w3-xlarge">
    <p class="w3-left">Shop</p>
</header>

<?php if ($this->data["msg"] != ""): ?>
<div class="w3-row">
    <div class="<?php echo $this->data['msgType']; ?> w3-col l12 s12"><?php echo $this->data["msg"]; ?></div>
</div>
<?php endif; ?>

<!-- Product grid -->
<div class="w3-row">
    <div class="w3-col l3 s6">
        <div class="w3-container">
            <img class="w3-border" src="/assets/images/flags/secret.png" style="width:100%">
            <form method="POST" action="">
            <p>Secret FLAG 1
                <input class="w3-right w3-button w3-red" type="submit" name="buy1" value="Buy"/><br>
                <b>1000 SC</b>
            </p>
            </form>
        </div>
        <div class="w3-container">
            <img class="w3-border" src="/assets/images/flags/dci.png" style="width:100%">
            <p>DCI - ÉTS<br><b>Out of order</b></p>
        </div>
    </div>

    <div class="w3-col l3 s6">
        <div class="w3-container">
            <img class="w3-border" src="/assets/images/flags/secret.png" style="width:100%">
            <form method="POST" action="">
            <p>Secret FLAG 2
                <input class="w3-right w3-button w3-red" type="submit" name="buy2" value="Buy"/><br>
                <b>999999 SC</b>
            </p>
            </form>
        </div>
        <div class="w3-container">
            <img class="w3-border" src="/assets/images/flags/alliance.png" style="width:100%">
            <p>Alliance - WoW<br><b>Out of order</b></p>
        </div>
    </div>


    <div class="w3-col l3 s6">
        <div class="w3-container">
            <img class="w3-border" src="/assets/images/flags/gondor.png" style="width:100%">
            <p>Gondor - LotR<br><b>Out of order</b></p>
        </div>
        <div class="w3-container">
            <img class="w3-border" src="/assets/images/flags/ufo.png" style="width:100%">
            <p>UFP - Star Trek<br><b>Out of order</b></p>
        </div>
    </div>

    <div class="w3-col l3 s6">
        <div class="w3-container">
            <img class="w3-border" src="/assets/images/flags/overwatch.png" style="width:100%">
            <p>Overwatch<br><b>Out of order</b></p>
        </div>
        <div class="w3-container">
            <img class="w3-border" src="/assets/images/flags/first_order.png" style="width:100%">
            <p>First Order - Star Wars<br><b>Out of order</b></p>
        </div>
    </div>
</div>