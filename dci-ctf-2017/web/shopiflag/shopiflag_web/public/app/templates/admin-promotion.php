<!-- Top header  -->
<header class="w3-container w3-xlarge">
    <p class="w3-left">Ask for a promotion</p>
</header>

<div class="w3-row">
    <div class="w3-col s1">&nbsp;</div>
    <div class="w3-col l10 s10">
        <p>
            You think you have what it takes to become a <b>Senior Moderator</b>? Send us a request explaining
            why you think you'd make a good candidate, and the admins might decide to promote you!
        </p>
        <?php if ($this->data["msg"] != ""): ?>
        <div class="w3-row">
            <div class="<?php echo $this->data['msgType']; ?> w3-col l12 s12"><?php echo $this->data["msg"]; ?></div>
        </div>
        <?php endif; ?>
        <form method="POST" action="">
            <p><textarea rows="10" class="w3-input w3-border" maxlength="1024" name="reason" placeholder="Tell us why you think you deserve a promotion."></textarea></p>
            <input type="submit" class="w3-button w3-green w3-block" value="Request promotion"/>
        </form>
    </div>
    <div class="w3-col s1">&nbsp;</div>
</div>

<div class="w3-row"><div class="w3-col s12">&nbsp;</div></div>