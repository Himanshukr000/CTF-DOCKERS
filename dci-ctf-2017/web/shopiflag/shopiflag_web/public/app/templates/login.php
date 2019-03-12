<!-- Top header  -->
<header class="w3-container w3-xlarge">
    <p class="w3-left">Login</p>
</header>

<div class="w3-row-padding">
    <div class="w3-col s1">&nbsp;</div>
    <div class="w3-col s10">
        <?php if ($this->data["msg"] != ""): ?>
        <div class="w3-row">
            <div class="<?php echo $this->data['msgType']; ?> w3-col l12 s12"><?php echo $this->data["msg"]; ?></div>
        </div>
        <?php endif; ?>
        <form method="POST" action="">
            <p><input class="w3-input w3-border" type="text" placeholder="Username" name="username" maxlength="22" required></p>
            <p><input class="w3-input w3-border" type="password" placeholder="Password" name="password"></p>
            <input type="submit" class="w3-button w3-block w3-green" name="login" value="Log in"/>
        </form>
    </div>
    <div class="w3-col s1">&nbsp;</div>
</div>
<div class="w3-row"><div class="w3-col s12">&nbsp;</div></div>