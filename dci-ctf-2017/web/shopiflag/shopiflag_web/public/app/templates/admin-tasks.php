<!-- Top header  -->
<header class="w3-container w3-xlarge">
    <p class="w3-left">Moderators Dashboard</p>
</header>

<div class="w3-row">
    <div class="w3-col s1">&nbsp;</div>
    <div class="w3-col l10 s10">
        <p>
            As one of our many moderators, you have many abilities that normal users don't.
            We trust you to use these privileges to do your job well. As Wayne Gretzky said,
            "<b>With great power comes great responsibility</b>". Your responsibilities, as
            a moderator, are to make sure the website runs without any problems. More precisely,
            here are your tasks:
            <ul>
                <li>Evaluate users submission and either accept or reject them</li>
                <li>Remain suspicious of any hacking activities</li>
                <li>Ask for the admin help only if absolutely necessary</li>
                <li>Always be respectful with all our users</li>
            </ul>
            You can use the various services offered to you on this dashboard in order to accomplish your tasks.
        </p>
    </div>
    <div class="w3-col s1">&nbsp;</div>
</div>

<hr>

<div class="w3-row">
    <div class="w3-col s1">&nbsp;</div>
    <div class="w3-col l10 s10">
        <p>
            Also, Senior Moderators and Admins have the privilege of earning one new flag every month.
            If you have this privlege, click on the button below to get your free flag!
        </p>
        <?php if ($this->data["msg"] != ""): ?>
        <div class="w3-row">
            <div class="<?php echo $this->data['msgType']; ?> w3-col l12 s12"><?php echo $this->data["msg"]; ?></div>
        </div>
        <?php endif; ?>
        <form method="POST" action="">
            <input type="submit" class="w3-button w3-green" name="getflag" value="Get flag"/>
        </form>
    </div>
    <div class="w3-col s1">&nbsp;</div>
</div>

<div class="w3-row"><div class="w3-col s12">&nbsp;</div></div>