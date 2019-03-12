<!-- Top header  -->
<header class="w3-container w3-xlarge">
    <p class="w3-left">Sell</p>
</header>

<div class="w3-row">
    <div class="w3-col s2">&nbsp;</div>
    <div class="w3-col l8 s8">
        <p>Are you interested in selling your own flags? We can help you!</p>
        <p>
            Sellin a flag on Shopiflag is very easy. All you have to do is upload the image of your flag,
            the name of the region it represents, the price you want to sell it at and click the submit
            button! Our team of moderators (who works tirelessly 24h/7) will make sure your flag is
            appropriate before it is made available to the public.
        </p>
        <p>
            To be approved, your flag needs to respect some rules:
            <ul>
                <li>You need to be logged in when you send us your submission</li>
                <li>The uploaded file needs to be an image</li>
                <li>The image needs to be 600px wide and 300px high</li>
                <li>The price needs to be a positive number</li>
            </ul>
        </p>
    </div>
    <div class="w3-col s2">&nbsp;</div>
</div>

<div class="w3-row-padding">
    <div class="w3-col s1">&nbsp;</div>
    <div class="w3-col s10">
        <?php if ($this->data["msg"] != ""): ?>
        <div class="w3-row">
            <div class="<?php echo $this->data['msgType']; ?> w3-col l12 s12"><?php echo $this->data["msg"]; ?></div>
        </div>
        <?php endif; ?>
        <form method="POST" action="" enctype="multipart/form-data">
            <p><input class="w3-input w3-border" type="file" name="flag" required></p>
            <p><input class="w3-input w3-border" type="text" placeholder="Region" name="region" maxlength="255" required></p>
            <p><input class="w3-input w3-border" type="text" placeholder="Price" name="price" maxlength="9" required></p>
            <input type="submit" class="w3-button w3-block w3-green" name="submit" value="Submit"/>
        </form>
    </div>
    <div class="w3-col s1">&nbsp;</div>
</div>
<div class="w3-row"><div class="w3-col s12">&nbsp;</div></div>