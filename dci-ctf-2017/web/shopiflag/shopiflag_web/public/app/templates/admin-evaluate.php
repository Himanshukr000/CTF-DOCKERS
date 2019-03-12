<!-- Top header  -->
<header class="w3-container w3-xlarge">
    <p class="w3-left">Evaluate users submission</p>
</header>

<div class="w3-row">
    <div class="w3-col s1">&nbsp;</div>
    <div class="w3-col l10 s10">
        <p>
            There are currentely no submissions awaiting to be evaluated. You can still see archived
            submissions if you know their id #:
        </p>
        <form method="POST" action="">
            <input class="w3-input w3-border"type="text" placeholder="Submission ID#" name="id" required style="display: initial; width: initial;">
            <input type="submit" class="w3-button w3-green" value="Search"/>
        </form>
        <?php if ($this->data["msg"] != ""): ?>
        <div class="w3-row">
            <div class="<?php echo $this->data['msgType']; ?> w3-col l12 s12"><?php echo $this->data["msg"]; ?></div>
        </div>
        <?php endif; ?>
    </div>
    <div class="w3-col s1">&nbsp;</div>
</div>

<div class="w3-row"><div class="w3-col s12">&nbsp;</div></div>

<div class="w3-row">
    <div class="w3-col s1">&nbsp;</div>
    <div class="w3-col l10 s10">
        <table class="w3-table w3-striped w3-white">
            <tr>
                <td>Image</td>
                <td>Region</td>
                <td>Price</td>
            </tr>
            <?php if (count($this->data["archive"]) == 1): ?>
            <tr>
                <td><img src="http://<?php echo ADMIN_SERVER_EXTERNAL . "/" . $this->data["archive"][0]["image_url"]; ?>" width="100" height="50"/></td>
                <td><?php echo $this->data["archive"][0]["region"]; ?></td>
                <td><?php echo $this->data["archive"][0]["price"]; ?> SC</td>
            </tr>
            <?php endif; ?>
        </table>
    </div>
    <div class="w3-col s1">&nbsp;</div>
</div>

<div class="w3-row"><div class="w3-col s12">&nbsp;</div></div>