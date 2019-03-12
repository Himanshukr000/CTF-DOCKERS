<!-- Top header  -->
<header class="w3-container w3-xlarge">
    <p class="w3-left">Inbox</p>
</header>

<div class="w3-row-padding">
    <div class="w3-col s12 l12">
        <?php if (count($this->data["mails"]) > 0): ?>
            <table class="w3-table w3-striped w3-white">
                <?php foreach ($this->data["mails"] as $mail): ?>
                    <?php $this->data["date"]->setTimestamp($mail["sent_time"]); ?>
                    <tr>
                        <td colspan="3" class="mail-header"><?php echo $this->data["date"]->format('Y-m-d H:i:s'); ?></td>
                    </tr>
                    <tr>
                        <td><i class="fa fa-user w3-text-blue w3-large"></i></td>
                        <td>From:</td>
                        <td><?php echo $mail["from_username"]; ?></td>
                    </tr>
                    <tr>
                        <td><i class="fa fa-envelope-o w3-text-red w3-large"></i></td>
                        <td>Subject:</td>
                        <td><?php echo $mail["subject"]; ?></td>
                    </tr>
                    <tr>
                        <td colspan="3"><?php echo $mail["content"]; ?></td>
                    </tr>
                    <tr>
                        <td colspan="3"></td>
                    </tr>
                <?php endforeach; ?>
            </table>
        <?php else: ?>
            <?php if ($this->data["msg"] != ""): ?>
            <div class="w3-row">
                <div class="<?php echo $this->data['msgType']; ?> w3-col l12 s12"><?php echo $this->data["msg"]; ?></div>
            </div>
            <?php endif; ?>
            <p>You don't have any emails at the moment.</p>
        <?php endif; ?>
    </div>
</div>