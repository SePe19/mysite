DROP TABLE IF EXISTS users;
CREATE TABLE users(
    user_id                     TEXT UNIQUE NOT NULL,
    user_name                   TEXT UNIQUE NOT NULL,
    user_first_name             TEXT NOT NULL,
    user_last_name              TEXT DEFAULT "",
    user_email                  TEXT UNIQUE NOT NULL,
    user_password               TEXT NOT NULL,
    user_verified               INT DEFAULT 0,
    user_verification_token     TEXT NOT NULL,
    user_avatar                 TEXT DEFAULT "default.jpg",
    user_cover                  TEXT DEFAULT "default-cover.png",
    user_created_at             TEXT NOT NULL,
    user_total_tweets           TEXT DEFAULT 0,
    user_total_following        INT DEFAULT 0,
    user_total_followers        INT DEFAULT 0,
    PRIMARY KEY(user_id)
) WITHOUT ROWID;

-- INSERT INTO users VALUES("user_id", "user_name", "user_first_name", "user_last_name", "user_email", "user_password", "user_verified", "user_avatar.jpg", "user_cover.jpg", "user_created_at", "user_total_tweets", "user_total_following", "user_total_followers");
INSERT INTO users VALUES("a9890d6a78a344ec87401cdb85e38a14", "ladygaga", "Lady", "Gaga", "gaga@gakgak.dk", "123", "1", "a9890d6a78a344ec87401cdb85e38a12", "046d38ab9a094b8fb4993d9e2f2131b6.jpg", "b7add1c2b384480bacfdc615c8a3e5aa.jpg", "1204326000", "9936", "116300", "84800000");
INSERT INTO users VALUES("ebb0d9d74d6c4825b3e1a1bcd73ff49a", "elonmusk", "Elon", "Musk", "elon@mail.dk", "123", "0", "a9890d6a78a344ec87401cdb85e38a19", "0df4ab53a8b14dd0925f6f2d1689c2c6.jpg", "47939906fea84cd28d7c56ac30d63a02.jpg", "1243883319", "23300", "182", "130700000");
INSERT INTO users VALUES("7860393a03dc4c1e872dcdd2cbf946ab", "RSprachrohr", "Rammstein", "", "rsp@mail.dk", "123", "1", "a9890d6a78a344ec87401cdb85e38a17", "0d9b9dd5bde54e338b6335ea0b8eb265.jpg", "c5fbc4cc1aa94940a67c07c873d86352.jpg", "1280689719", "313", "0", "536300");

UPDATE users
SET user_name = "ladygakgak"
WHERE user_name = "ladygaga";

CREATE INDEX idx_users_user_first_name ON users(user_first_name);
CREATE INDEX idx_users_user_last_name ON users(user_last_name);
CREATE INDEX idx_users_user_avatar ON users(user_avatar);
CREATE INDEX idx_users_user_cover ON users(user_cover);

SELECT name FROM sqlite_master WHERE type = 'index';
SELECT name FROM sqlite_master WHERE type = 'trigger';

DELETE FROM users WHERE user_email = "frederik.hbraad@gmail.com";
DELETE FROM users WHERE user_email = "mrsepe19@gmail.com";
DELETE FROM users WHERE user_email = "seb19@live.dk";


-- ##############################
-- TWEETS
DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
    tweet_id                    TEXT UNIQUE NOT NULL,
    tweet_message               TEXT NOT NULL,
    tweet_image                 TEXT,
    tweet_created_at            TEXT NOT NULL,
    tweet_user_fk               TEXT NOT NULL,
    tweet_total_comments        TEXT DEFAULT 0,
    tweet_total_retweets        TEXT DEFAULT 0,
    tweet_total_likes           TEXT DEFAULT 0,
    tweet_total_views           TEXT DEFAULT 0,
    PRIMARY KEY(tweet_id)
)WITHOUT ROWID;

-- Lady Gaga
-- INSERT INTO tweets VALUES("tweet_id", "tweet_message", "tweet_image.jpg", "tweet_created_at", "tweet_user_fk", "tweet_total_comments", "tweet_total_retweets", "tweet_total_likes", "tweet_total_views");
INSERT INTO tweets VALUES("7d36ea9c18344874843823487d22c16c", "V MAGAZINE: CHROMATICA BALL DIARIES BY HEDI SLIMANE COVER 1", "76266667f54942d490a1ec2809d9ac2d.jpg", "1663084920", "a9890d6a78a344ec87401cdb85e38a14", "1730", "9033", "45400", "");
INSERT INTO tweets VALUES("28106db01fdc496b8f8881e1d943a201", "V MAGAZINE: CHROMATICA BALL DIARIES BY HEDI SLIMANE COVER 2", "67ed34300fa640c38cfc5d01d4d8cca3.jpg", "1663099320", "a9890d6a78a344ec87401cdb85e38a14", "1733", "9034", "45500", "");
INSERT INTO tweets VALUES("678b621fafbd4492ba9238454dd7c44c", "V MAGAZINE: CHROMATICA BALL DIARIES BY HEDI SLIMANE COVER 3", "a64b696daf5a408289ce85e46f9fc8f2.jpg", "1663423260", "a9890d6a78a344ec87401cdb85e38a14", "622", "3850", "28600", "");
INSERT INTO tweets VALUES("2ad7f04da0c2424588ed67b9b8e723fe", "V MAGAZINE: CHROMATICA BALL DIARIES BY HEDI SLIMANE COVER 4", "4b74287a2f83437d84b7c7a5e10dec7e.jpg", "1663437600", "a9890d6a78a344ec87401cdb85e38a14", "897", "4178", "31900", "");
INSERT INTO tweets VALUES("ea8b05752c1e41a6888b32bb018cca5f", "Folie à Deux 🃏", "46b856c87fa149208960c92430f29336.jpg", "1676888455", "a9890d6a78a344ec87401cdb85e38a14", "6379", "71300", "31900", "161000000");
INSERT INTO tweets VALUES("978f1366cacb44dd8b63205720ccadc5", "CHROMATICA BALL TOUR MERCH AVAILABLE NOW ⚔️💓 http://shop.ladygaga.com", "9befbd1fe2384bef98809599a3519d13.jpg", "1669187160", "a9890d6a78a344ec87401cdb85e38a14", "1478", "3438", "16700", "");
INSERT INTO tweets VALUES("6ff7ca63bec0476699fe1c33dd2554b7", "I am so honored to be nominated for 2 Grammys for “Hold My Hand” and the Top Gun: Maverick Sountrack with my fellow composers.  It’s a real dream to be included in this celebration of music with a song and musical theme so close to my heart thank you ❤️", "", "1700075160", "a9890d6a78a344ec87401cdb85e38a14", "2570", "7112", "50000", "");
INSERT INTO tweets VALUES("c15dcee2f0134df497fe0e14b81248da", "I love you little monsters, forever xoxo, Mother Monster #WeLoveYouGaga #ChromaticaBallMiami I’m sorry I used my best judgment, it wasn’t safe.", "", "1695028860", "a9890d6a78a344ec87401cdb85e38a14", "2700", "5863", "50400", "");
INSERT INTO tweets VALUES("23167c94fd8047f49a6b849b3929fca1", "Joker: Folie à Deux 10.04.24", "dc64f45b25144a479d2013ef2f324a49.jpg", "1691172060", "a9890d6a78a344ec87401cdb85e38a14", "6586", "81800", "232600", "6800000");
INSERT INTO tweets VALUES("2e081c561ce84092aeb7a945fb8d2571", "", "ace24fd7594c4b9da451592cff2a5b0b.jpg", "1690808220", "a9890d6a78a344ec87401cdb85e38a14", "1443", "4787", "52500", "");
INSERT INTO tweets VALUES("a39f6685b73c49cb874e6d8965ee1663", "That’s a wrap ❤️‍🔥 🎬🃏 X, Harleen", "5b3ebbafe0ce45f2ba29d180d9b1bd17.jpg", "1680748020", "a9890d6a78a344ec87401cdb85e38a14", "4544", "47500", "325600", "");
INSERT INTO tweets VALUES("e5fe564feed0433bb22aa31f3ba692c4", "#Oscars 2023 🖤 @tiffanyandco @hauslabs", "45bafefb34eb445eab7fbdb7861bb9ca.jpg", "1678734420", "a9890d6a78a344ec87401cdb85e38a14", "1871", "10000", "72300", "");

-- Elon Musk
-- INSERT INTO tweets VALUES("tweet_id", "tweet_message", "tweet_image.jpg", "tweet_created_at", "tweet_user_fk", "tweet_total_comments", "tweet_total_retweets", "tweet_total_likes", "tweet_total_views");
INSERT INTO tweets VALUES("2e081c561ce84092aeb7a945fb8d2572", "Happens a lot", "f91f7b704a424cc3911a220a3fc7dbc2.jpg", "1684439520", "ebb0d9d74d6c4825b3e1a1bcd73ff49a", "12600", "33600", "369200", "40600000");
INSERT INTO tweets VALUES("8dc3a37ea5fd4c06863c39f7dd215304", "", "7fcb75004227485e813ee1561b7b04ac.jpg", "1684524900", "ebb0d9d74d6c4825b3e1a1bcd73ff49a", "6814", "17700", "185100", "14400000");
INSERT INTO tweets VALUES("c06bdc69243c43689025a0ea7ea73cca", "AI ♾", "4dac54db24f6417094ac53072b42e5fb.jpg", "1684519440", "ebb0d9d74d6c4825b3e1a1bcd73ff49a", "9439", "19900", "202500", "28600000");
INSERT INTO tweets VALUES("c1da48ada6144cd1a0fd9660bad3f854", "", "ab734a0d10e14a5ba30b89fb1274afbd.jpg", "1684626720", "ebb0d9d74d6c4825b3e1a1bcd73ff49a", "5083", "22000", "188500", "10000000");
INSERT INTO tweets VALUES("b3e683223785472c858ae5f31e32de79", "", "f7a1f41d9f344663863e3df3f1080c04.jpg", "1684623000", "ebb0d9d74d6c4825b3e1a1bcd73ff49a", "16500", "41000", "376400", "28600000");
INSERT INTO tweets VALUES("4c4b673d9614444c919168a7baee3220", "Why is sleep so hard!? Perhaps we will never know.", "4608126c04674e658477a399f7e2c8e5.jpg", "1684433220", "ebb0d9d74d6c4825b3e1a1bcd73ff49a", "20300", "38000", "349300", "33600000");
INSERT INTO tweets VALUES("0191c434e1c7410bae095cf4e2eecacf", "Both quality & quantity of high quality posts of all kinds (short text, long essays, pictures, audio & video) have improved dramatically. Thank you for contributing your voice to humanity’s digital public square!", "", "1684867920", "ebb0d9d74d6c4825b3e1a1bcd73ff49a", "11100", "15300", "134400", "13300000");
INSERT INTO tweets VALUES("ffe992b678ca4bc1a21ff98db6968a7a", "All those moments, will be lost in time like tears in rain …", "", "1684792500", "ebb0d9d74d6c4825b3e1a1bcd73ff49a", "25300", "39300", "288200", "38700000");
INSERT INTO tweets VALUES("01c3b686650844d988cddc4146262760", "I have spaceships", "", "1684521780", "ebb0d9d74d6c4825b3e1a1bcd73ff49a", "59900", "45600", "392500", "49200000");
INSERT INTO tweets VALUES("3303e6d237ae495bb8fa2c0eb5f4208c", "I hope this platform increasingly brings you joy & elucidation", "", "1684459860", "ebb0d9d74d6c4825b3e1a1bcd73ff49a", "26600", "21000", "226800", "27400000");

-- Rammstein
-- INSERT INTO tweets VALUES("tweet_id", "tweet_message", "tweet_image.jpg", "tweet_created_at", "tweet_user_fk", "tweet_total_comments", "tweet_total_retweets", "tweet_total_likes", "tweet_total_views");
INSERT INTO tweets VALUES("9d9ed99e94b54f759390a5ff436b8979", "26 years on, a behind-the-scenes look on the set of 'Du hast'. Watch the restored 4K version here: http://sehnsucht.rammstein.com Photos by Frank Lothar Lange.", "2d25147a07294d96a815cbd581450003.jpg", "1684256442", "7860393a03dc4c1e872dcdd2cbf946ab", "16", "444", "2725", "106500");
INSERT INTO tweets VALUES("839168aec88648e2bb9c3abf80de1059", "Blind ticket holders are invited to touch and discover the stage! Reach out to us at community@rammstein-management.de with: - An official document from a certified medical professional, verifying your loss of sight. - A photo of your ticket, with your name and the concert date.", "7b47b749e3ce48edab540d8dd71aefec.jpg", "1684329342", "7860393a03dc4c1e872dcdd2cbf946ab", "3", "100", "1017", "37500");
INSERT INTO tweets VALUES("8cef5c5f04d243e18c6c5a39a5926a5d", "The hottest night of the year in Tallinn – aitäh! © Rob Lewis Photography & @jenskochphoto", "5cf10238cs8224e2f9f4d964d0f94a1f4.jpg", "1658497062", "7860393a03dc4c1e872dcdd2cbf946ab", "11", "247", "2581", "");
INSERT INTO tweets VALUES("ba3c61501bba48afa673a99f6e0e0977", "Mercie, Ostende! What a way to end the Europe Stadium Tour 2022! Erik Weiss Photography & @jenskochphoto", "430fe2081ed94a59ad0e015e81a00aa9.jpg", "1659718800", "7860393a03dc4c1e872dcdd2cbf946ab", "54", "419", "3203", "");
INSERT INTO tweets VALUES("d3a84f8e415e4b2893e15af51a54ee6b", "Das Warten hat ein Ende, let the Rammstein Europe Stadium Tour 2023 begin! Thank you, Vilnius. Photos: Paul Harries & Jens Koch", "522c57c5056b4247ba19b7ab3bf36202.jpg", "1684870560", "7860393a03dc4c1e872dcdd2cbf946ab", "49", "411", "2887", "85000");
INSERT INTO tweets VALUES("d0829fe67a7f4182b10f8638a28dc45b", "Rammstein Charity is back with awards from the band's latest album 'Zeit' and their self-titled record from 2019. All proceeds will go to various charities selected by the band. The auctions start on December 12, 12:00 CET at https://rammstein.charity! Photo © @jenskochphoto", "be5bb8800f8c43d2bbc47b3425d03e06.jpg", "1670587200", "7860393a03dc4c1e872dcdd2cbf946ab", "20", "221", "2107", "");
INSERT INTO tweets VALUES("8d116da49745488890be8a20850ea8af", "Uno, dos, tres unforgettable nights of fire, fun and feelings in Foro Sol – a fitting finale for the North America Stadium Tour 2022! ¡Gracias México! © Frédéric Batier, Olaf Heine & @jenskochphoto", "7c52823850c341eea20fba01ad87d909.jpg", "1664989200", "7860393a03dc4c1e872dcdd2cbf946ab", "210", "1695", "9533", "");
INSERT INTO tweets VALUES("db0024a8763e44d3b2ea0d58e2e645e6", "Rammstein fans know how to make the servers glow! Tickets have sold at such speed that 6 new shows can now be announced: Odense, Munich, Berlin, Vienna and Brussels! Tickets available at http://rammstein.com/tickets!", "8a88af3be6a44261b0b1d324ad23e65a.jpg", "1662641880", "7860393a03dc4c1e872dcdd2cbf946ab", "75", "223", "2287", "");
INSERT INTO tweets VALUES("6ee0642bf348459aaaafd6fa31a80fba", "Home to the Giants, Jets and Germans – thank you New York City!  © @jenskochphoto", "e0255d3f258642f2b5b6dc3be8ccacf0.jpg", "1662579060", "7860393a03dc4c1e872dcdd2cbf946ab", "36", "218", "2265", "");
INSERT INTO tweets VALUES("9e7974cd30f24a0488d89a6f1b47b2bd", "Two fiery nights in Los Angeles to say: Danke, Adieu, auf Wiedersehen, USA! © Olaf Heine, Paul Harries & Jens Koch", "425160ffb44449eda3712452fa2d0355.jpg", "1664135400", "7860393a03dc4c1e872dcdd2cbf946ab", "94", "408", "3764", "");



CREATE INDEX idx_tweets_tweet_image ON tweets(tweet_image);




-- ##############################
-- TRENDS
DROP TABLE IF EXISTS trends;
CREATE TABLE trends(
    trend_id                    TEXT,
    trend_category              TEXT DEFAULT 0,
    trend_title                 TEXT NOT NULL,
    trend_total_tweets          TEXT DEFAULT 0,
    PRIMARY KEY(trend_id)
) WITHOUT ROWID;

-- Trend 1
INSERT INTO trends VALUES("d3ea0d1356f442cb9e053bb6bd11fc5d", "Trending", "Eurovision#2023", "3933");
INSERT INTO trends VALUES("4e28250936994e3aa3b44f9766b772a2", "Trending", "ChatGPT", "98300");
INSERT INTO trends VALUES("e82d45d90d3a43cfb43b3d5d09c42baf", "Entertainment · Trending", "#Oscars", "22800");
INSERT INTO trends VALUES("5d9ab494d3c541b39047f9672689ef06", "Entertainment · Trending", "Women Talking", "13100");
INSERT INTO trends VALUES("dd637547eb0e4ea5b2385f5894c72e06", "Trending in Denmark", "Danish", "6388");


-- #############################
-- FOLLOWERS
DROP TABLE IF EXISTS followers;
CREATE TABLE followers(
  follower_id       TEXT NOT NULL,
  followee_id       TEXT NOT NULL,
  UNIQUE(follower_id, followee_id)
);

INSERT INTO followers VALUES("fe108d67442d4d2386bbcb872dd4a975", "ebb0d9d74d6c4825b3e1a1bcd73ff49a");
INSERT INTO followers VALUES("fe108d67442d4d2386bbcb872dd4a975", "a9890d6a78a344ec87401cdb85e38a14");

DELETE FROM followers WHERE follower_id = "fe108d67442d4d2386bbcb872dd4a975" AND followee_id = "a9890d6a78a344ec87401cdb85e38a14";


DROP TRIGGER IF EXISTS increment_user_total_followers;
CREATE TRIGGER increment_user_total_followers AFTER INSERT ON followers
BEGIN
  UPDATE users 
  SET user_total_followers =  user_total_followers + 1 
  WHERE user_id = NEW.followee_id;
END;

DROP TRIGGER IF EXISTS decrement_user_total_followers;
CREATE TRIGGER decrement_user_total_followers AFTER DELETE ON followers
BEGIN
  UPDATE users 
  SET user_total_followers =  user_total_followers - 1 
  WHERE user_id = OLD.followee_id;
END;

DROP TRIGGER IF EXISTS increment_user_total_following;
CREATE TRIGGER increment_user_total_following AFTER INSERT ON followers
BEGIN
  UPDATE users 
  SET user_total_following =  user_total_following + 1 
  WHERE user_id = NEW.follower_id;
END;

DROP TRIGGER IF EXISTS decrement_user_total_following;
CREATE TRIGGER decrement_user_total_following AFTER DELETE ON followers
BEGIN
  UPDATE users 
  SET user_total_following =  user_total_following - 1 
  WHERE user_id = OLD.follower_id;
END;
--7860393a03dc4c1e872dcdd2cbf946ab - rammstein
--ebb0d9d74d6c4825b3e1a1bcd73ff49a - elonmusk
--a9890d6a78a344ec87401cdb85e38a14 - ladygaga


-- ##############################
-- JOIN TABLES USERS & TWEETS
SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk;

DROP VIEW IF EXISTS users_and_tweets;
CREATE VIEW users_and_tweets AS 
SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk;

SELECT * FROM users_and_tweets WHERE user_name="ladygaga";
SELECT tweet_image FROM users_and_tweets WHERE tweet_image != "" AND user_name="ladygaga" LIMIT 6;

-- #############################
-- TRIGGERS
DROP TRIGGER IF EXISTS increment_user_total_tweets;
CREATE TRIGGER increment_user_total_tweets AFTER INSERT ON tweets
BEGIN
  UPDATE users 
  SET user_total_tweets =  user_total_tweets + 1 
  WHERE user_id = NEW.tweet_user_fk;
END;

DROP TRIGGER IF EXISTS decrement_user_total_tweets;
CREATE TRIGGER decrement_user_total_tweets AFTER DELETE ON tweets
BEGIN
  UPDATE users 
  SET user_total_tweets =  user_total_tweets - 1 
  WHERE user_id = OLD.tweet_user_fk;
END;