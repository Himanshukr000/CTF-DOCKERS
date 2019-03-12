<!-- Top header  -->
<header class="w3-container w3-xlarge">
    <p class="w3-left">Evaluate flag submision (deprececated)</p>
</header>

<div class="w3-row">
    <div class="w3-col s1">&nbsp;</div>
    <div class="w3-col l10 s10">
        <?php if ($this->data["region"] != ""): ?>
            <img src="<?php echo ADMIN_SERVER_EXTERNAL . "/" . $this->data["image"]; ?>" /></br>
            <div><?php echo $this->data["region"]; ?></div>
            <div><?php echo $this->data["price"]; ?> SC</div>
        <?php else: ?>
            <div>No new submission</div>
        <?php endif; ?>
    </div>
    <div class="w3-col s1">&nbsp;</div>
</div>

<div class="w3-row"><div class="w3-col s12">&nbsp;</div></div>