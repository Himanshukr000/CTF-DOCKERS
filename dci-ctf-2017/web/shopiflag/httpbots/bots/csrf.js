const lighthouse = require('lighthouse');
const chromeLauncher = require('lighthouse/chrome-launcher');
const CDP = require('chrome-remote-interface');

const USERNAME = "Josephine Knight"
const PASSWORD = "493750297592304723042173105750247730734712037434"

const flags = {
    chromeFlags: ["--headless", "--no-sandbox", "--disable-web-security"]
};

StageEnum = {
    SHOPIFLAG_LOGIN     : 0,
    SHOPIFLAG_LOGGED_IN : 1,
    ADMIN_LOGIN         : 2,
    ADMIN_LOGGED_IN     : 3,
};

stage = StageEnum.SHOPIFLAG_LOGIN;
last_update = 0;

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

chromeLauncher.launch(flags).then(chrome => {
    flags.port = chrome.port;
    CDP({port: chrome.port}).then(client => {
        // extract domains 
        const {Network, Page, Runtime} = client;

        // setup handlers 
        Network.requestWillBeSent((params) => {
            //console.log(params.request.url);
        });

        Page.frameStoppedLoading(() => {
            //console.log("finished")
            if (stage === StageEnum.SHOPIFLAG_LOGIN)
            {
                stage = StageEnum.SHOPIFLAG_LOGGED_IN;
                const js = "document.getElementsByName('username')[0].value = '" + USERNAME  + "';"
                         + "document.getElementsByName('password')[0].value = '" + PASSWORD  + "';"
                         + "document.getElementsByName('login')[0].click();";
                Runtime.evaluate({expression: js});
            }
            else if (stage === StageEnum.SHOPIFLAG_LOGGED_IN)
            {
                stage = StageEnum.ADMIN_LOGIN;
                Page.navigate({url: 'http://admin-server:80/login.php'});
            }
            else if (stage === StageEnum.ADMIN_LOGIN)
            {
                stage = StageEnum.ADMIN_LOGGED_IN;
                const js = "document.getElementsByName('username')[0].value = '" + USERNAME  + "';"
                         + "document.getElementsByName('password')[0].value = '" + PASSWORD  + "';"
                         + "document.getElementsByName('login')[0].click();";
                Runtime.evaluate({expression: js});
            }
            else if (stage === StageEnum.ADMIN_LOGGED_IN)
            {
                sleep(2000).then(() => {
                    Page.navigate({url: 'http://admin-server:80/promotion.php'});
                });
            }
        });

        Page.frameStartedLoading(() => {
            //console.log("started loading")
            last_update = new Date().getTime();
            sleep(5000).then(() => {
                if (new Date().getTime() - last_update > 4000) {
                    client.close().then(() => {
                        chrome.kill().then(() => {
                            exit()
                        });
                    });
                }
            });
        });

        // enable events then start! 
        Promise.all([Network.enable(), Page.enable(), Runtime.enable()]).then(() => {
            stage = StageEnum.SHOPIFLAG_LOGIN;
            Page.navigate({url: 'http://shopiflag.ctf.dciets.com/login'});
        });
    });
});