const lighthouse = require('lighthouse');
const chromeLauncher = require('lighthouse/chrome-launcher');
const CDP = require('chrome-remote-interface');

const flags = {
    chromeFlags: ["--headless", "--no-sandbox", "--disable-web-security"]
};

last_update = 0;
target = "http://web:80/admin/flag-check";

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
            console.log(params.request.url);
        });

        Page.frameStoppedLoading(() => {
            //console.log("finished")
            sleep(2000).then(() => {
                Page.navigate({url: target});
            });
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
            //console.log("start");
            Network.setCookie({url: "http://web:80/", name: "PHPSESSID", value: "gup2i7sa3a51115ge2n06dmf72"}).then(what => {
                Page.navigate({url: target});
            });
        });
    });
});