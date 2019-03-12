# Remove all conflicting data
DROP USER IF EXISTS shopiflag_sqli1;
DROP USER IF EXISTS shopiflag_sqli2;
DROP USER IF EXISTS shopiflag_realuser;
DROP USER IF EXISTS admin_db_user;
DROP DATABASE IF EXISTS shopiflag_ctf;

# Create the databse if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS shopiflag_ctf;

CREATE TABLE IF NOT EXISTS `shopiflag_ctf`.`secret` (
    `id` INT NOT NULL AUTO_INCREMENT ,
    `flag` VARCHAR(32) NOT NULL ,
    PRIMARY KEY (`id`)
);
INSERT INTO shopiflag_ctf . secret (flag) VALUES ("DCI{Seek_N_Hide_world_best_2017}");


CREATE TABLE IF NOT EXISTS `shopiflag_ctf`.`users` (
    `id` INT NOT NULL AUTO_INCREMENT ,
    `username` VARCHAR(22) NOT NULL ,
    `password` VARCHAR(255) NOT NULL ,
    `credit` INT UNSIGNED NOT NULL ,
    `about` TEXT NOT NULL ,
    `permission` INT UNSIGNED NOT NULL ,
    PRIMARY KEY (`id`)
);

# create John The Moderator (used for xss)
INSERT INTO shopiflag_ctf . users (id, username, password, credit, about, permission)
VALUES (5, 'John The Moderator', SHA1('Barely more friendly than John The Ripper'),
        0, 'Just a moderator', 2);
# create a user to make it harder to get the priciest flag
INSERT INTO shopiflag_ctf . users (id, username, password, credit, about, permission)
VALUES (6, "' UNION SELECT 999999#", SHA1('First hacker always get the best stuff'),
        0, 'You should not be reading this...', 1);
# admin used for the csrf challenge
INSERT INTO shopiflag_ctf . users (id, username, password, credit, about, permission)
VALUES (9, 'Josephine Knight', SHA1('493750297592304723042173105750247730734712037434'),
        0, 'I like stuff. But not all stuff.', 4);


CREATE TABLE IF NOT EXISTS `shopiflag_ctf`.`moderators` (
    `id` INT NOT NULL AUTO_INCREMENT ,
    `username` VARCHAR(22) NOT NULL ,
    `password` VARCHAR(255) NOT NULL ,
    `credit` INT UNSIGNED NOT NULL ,
    `about` TEXT NOT NULL ,
    `permission` INT UNSIGNED NOT NULL ,
    PRIMARY KEY (`id`)
);

# Random moderators
INSERT INTO shopiflag_ctf . moderators (username, password, credit, about, permission)
VALUES ('Juan Holland', SHA1('ksadfnsd0werwerewor324234342ddsdf'),
        0, 'Why are you even looking at this?', 2);
INSERT INTO shopiflag_ctf . moderators (username, password, credit, about, permission)
VALUES ('Loren Boone', SHA1('aaaaaa1bbbbbbbccccc2ccccddddd3deeee4eeee'),
        0, '', 2);
INSERT INTO shopiflag_ctf . moderators (username, password, credit, about, permission)
VALUES ('Drew Joseph', SHA1('ilikefoodyoulikefoodwealllikefood'),
        0, 'I wonder what my life would have been like if I had decided to get a real job.', 2);
INSERT INTO shopiflag_ctf . moderators (username, password, credit, about, permission)
VALUES ('Sylvester Hill', SHA1('ilikefoodyoulikefoodwealllikefood'),
        0, '<script>alert("learning how to hack plz help");</script>', 3);
INSERT INTO shopiflag_ctf . moderators (username, password, credit, about, permission)
VALUES ('Sabrina Medina', SHA1('whoisagooddog?Iam_asdasdasdcvdfm'),
        0, 'I lost all my friends because of my flag addiction.', 3);
INSERT INTO shopiflag_ctf . moderators (username, password, credit, about, permission)
VALUES ('John The Moderator', SHA1('Barely more friendly than John The Ripper'),
        0, 'Just a moderator', 2);
# Random admins
INSERT INTO shopiflag_ctf . moderators (username, password, credit, about, permission)
VALUES ('Joseph Lowe', SHA1('_!+=foobarevealicebob_I_like_crypto_!+='),
        0, 'I hate this website so much.', 4);
INSERT INTO shopiflag_ctf . moderators (username, password, credit, about, permission)
VALUES ('Judith Sanders', SHA1('I am the best admin in the whole world'),
        0, 'Don\'t you have anything better to do than reading this?', 4);
INSERT INTO shopiflag_ctf . moderators (username, password, credit, about, permission)
VALUES ('Josephine Knight', SHA1('493750297592304723042173105750247730734712037434'),
        0, 'I like stuff. But not all stuff.', 4);


CREATE TABLE IF NOT EXISTS `shopiflag_ctf`.`flag_submissions` (
    `id` INT NOT NULL ,
    `user_id` INT NOT NULL ,
    `image_url` VARCHAR(255) NOT NULL ,
    `region` VARCHAR(255) NOT NULL ,
    `price` INT UNSIGNED NOT NULL ,
    `status` VARCHAR(32) NOT NULL ,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `shopiflag_ctf`.`promotion_requests` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `reason` TEXT NOT NULL ,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `shopiflag_ctf`.`mails` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `to_id` INT NOT NULL ,
    `from_username` VARCHAR(22) NOT NULL ,
    `subject` VARCHAR(255) NOT NULL ,
    `content` VARCHAR(255) NOT NULL ,
    `sent_time` INT NOT NULL ,
    PRIMARY KEY (`id`)
);

# create John The Moderator mail with flag
INSERT INTO shopiflag_ctf . mails (to_id, from_username, subject, content, sent_time)
VALUES (5, "Mommy", "Hello?",
    "Hi sweety,</br>"
    "I found one of those flag you can't stop collecting: DCI{Grown-Ups_Steal_Cookies_Too}</br>"
    "I would really like if you called more often... Mom xox", 1498609375);

# This is the general user, should be used when there is no vulnerabilities.
CREATE USER 'shopiflag_realuser' IDENTIFIED BY 'W6nv34vWBTyin8PA';
GRANT SELECT, INSERT, UPDATE ON shopiflag_ctf . users TO 'shopiflag_realuser';
GRANT SELECT, INSERT, UPDATE ON shopiflag_ctf . flag_submissions TO 'shopiflag_realuser';
GRANT SELECT, INSERT ON shopiflag_ctf . mails TO 'shopiflag_realuser';
GRANT INSERT ON shopiflag_ctf . promotion_requests TO 'shopiflag_realuser';

# User used during the second order sql injection challenges
CREATE USER 'shopiflag_sqli1' IDENTIFIED BY 'Zm3F46SszbozABZl';
GRANT SELECT ON shopiflag_ctf . users TO 'shopiflag_sqli1';

# User used during the select tag sql injection challenge
CREATE USER 'shopiflag_sqli2' IDENTIFIED BY 'Op72Pka3ddBshZiI';
GRANT SELECT ON shopiflag_ctf . moderators TO 'shopiflag_sqli2';
GRANT SELECT ON shopiflag_ctf . secret TO 'shopiflag_sqli2';

# User used on the admin server. Assume these credentials will be discovered by users
CREATE USER 'admin_db_user' IDENTIFIED BY '2Dd82s2AcUzY4TxL';
GRANT SELECT ON shopiflag_ctf . users TO 'admin_db_user';
GRANT SELECT, DELETE ON shopiflag_ctf . promotion_requests TO 'admin_db_user';

FLUSH PRIVILEGES;