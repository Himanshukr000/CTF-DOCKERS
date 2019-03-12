<!-- Top header  -->
<header class="w3-container w3-xlarge">
    <p class="w3-left">Find who your colleagues are</p>
</header>

<div class="w3-row">
    <div class="w3-col s1">&nbsp;</div>
    <div class="w3-col l10 s10">
        <p>
            Ever wonder who are the other unpaid slaves working for us? Now is your chance to find out!
            Select which categories of employees you want to learn about and we will display them to you.
        </p>
        <form method="POST" action="">
            <select name="permission">
                <option value="2">Moderators</option>
                <option value="3">Senior Moderators</option>
                <option value="4">Admins</option>
            </select>
            <input type="submit" class="w3-button w3-green" value="Display"/>
        </form>
        <table class="w3-table w3-striped w3-white">
            <tr>
                <td>ID</td>
                <td>Username</td>
                <td>About</td>
            </tr>
            <?php foreach($this->data["moderators"] as $mod): ?>
                <tr>
                    <td><?php echo htmlspecialchars($mod["id"]); ?></td>
                    <td><?php echo htmlspecialchars($mod["username"]); ?></td>
                    <td><?php echo htmlspecialchars($mod["about"]); ?></td>
                </tr>
            <?php endforeach; ?>
        </table>
    </div>
    <div class="w3-col s1">&nbsp;</div>
</div>

<div class="w3-row"><div class="w3-col s12">&nbsp;</div></div>