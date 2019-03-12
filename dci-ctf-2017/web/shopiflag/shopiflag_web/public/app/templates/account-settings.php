<!-- Top header  -->
<header class="w3-container w3-xlarge">
  <p class="w3-left">Account Settings</p>
</header>

<div class="w3=row">
    <div class="w3-col s12 l12 w3-container">
        <p><b>Personal information:</b></p>
    </div>
</div>
<div class="w3-row-padding">
    <div class="w3-col s12 l12">
        <table class="w3-table w3-striped w3-white">
            <tr>
                <td><i class="fa fa-user w3-text-blue w3-large"></i></td>
                <td>ID #</td>
                <td><?php echo $_SESSION["userid"]; ?></td>
            </tr>
            <tr>
                <td><i class="fa fa-tags w3-text-red w3-large"></i></td>
                <td>Username</td>
                <td><?php echo htmlspecialchars($_SESSION["username"]); ?></td>
            </tr>
            <tr>
                <td><i class="fa fa-usd w3-text-orange w3-large"></i></td>
                <td>Credit</td>
                <td>0 SC</td>
            </tr>
            <tr>
                <td><i class="fa fa-comment w3-text-green w3-large"></i></td>
                <td>About you</td>
                <td><textarea rows="10" class="w3-input w3-border" maxlength="1024" disabled><?php echo htmlspecialchars($_SESSION["about"]); ?></textarea></td>
            </tr>
        </table>
    </div>
</div>

<hr>

<div class="w3=row">
    <div class="w3-col s12 l12 w3-container">
        <p><b>Change your username:</b></p>
    </div>
</div>
<div class="w3-row-padding">
    <div class="w3-col s1 l1">&nbsp;</div>
    <div class="w3-col s10 l10">
        <?php if ($this->data["msg"] != ""): ?>
        <div class="w3-row">
            <div class="<?php echo $this->data['msgType']; ?> w3-col l12 s12"><?php echo $this->data["msg"]; ?></div>
        </div>
        <?php endif; ?>
        <form method="POST" action="">
            <p><input class="w3-input w3-border" type="text" placeholder="Username" name="newusername" maxlength="22" required></p>
            <p><input type="submit" class="w3-button w3-block w3-green" name="change" value="Change"/></p>
        </form>
    </div>
    <div class="w3-col s1 l1">&nbsp;</div>
</div>