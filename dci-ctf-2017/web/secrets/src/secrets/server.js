var puppeteer = require('puppeteer');
var net = require('net');
var express = require('express');
var path = require('path');
var url = require("url");
var session = require('express-session');
var csrf = require('csurf');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var flag = "DCI{ce_css_est_puissant}";

var parseForm = bodyParser.urlencoded({ extended: false });

var app = express();

app.use(cookieParser());

var visit = function() {
    return new Promise(function(resolve) {
        console.log('Error: Browser not started');
        resolve("Support is not ready to handle requests");
    });
};

var sleep = function(ms) {
    return new Promise(function(resolve) {
        setTimeout(resolve, ms);
    });
};

var csrfProtection = csrf({ cookie: true });

app.use(session({
    name: 'session',
    secret: '7d6367bed5274e0238474a47e228eff0b9075df4c3407d09ea4b98626ae23257830bb210659c2e04bf5b2e62558581abf5611f95f5eba0f7e0488fa4c5c44a80'
}));

app.set('view engine', 'pug');

app.use(function(req, res, next) {
    console.log(req.method + " " + req.originalUrl);
    next();
});

app.use('/', express.static(path.join(__dirname, 'public'), { etag: true, maxage: '48h' }));

app.get('/', csrfProtection, function (req, res) {
    res.render('index', { secret: req.session.secret, search: req.query.search, csrfToken: req.csrfToken() });
});

app.post('/', parseForm, csrfProtection, function (req, res) {
    console.log(req.body);

    if(req.session.secret != flag) {
        req.session.secret = req.body.secret;
    }

    res.redirect('/');
});

app.get('/support', function(req, res) {
    res.render('support');
});

app.post('/support', parseForm, async function(req, res) {
    var problemUrl = req.body.url;
    var parsedUrl = url.parse(problemUrl);
    var message = '';

    message = await visit(problemUrl);

    res.render('support', { message: message });
});

app.listen(3000, function() {
    console.log('server ready');
});

puppeteer.launch({ timeout: 10000, args: ['--no-sandbox'] }).then(async function(browser) {
    console.log('browser ready');

    var page = await browser.newPage();

    await page.goto('http://secrets.ctf.dciets.com/');
    await page.evaluate(function() {
        document.querySelector('input[name=secret]').value = flag;
        document.querySelector('form').submit();
    });

    await sleep(5000);

    await page.close();

    visit = function(url) {
        console.log(['visit', url]);

        return new Promise(async function(resolve) {
            var page = await browser.newPage();
            var success = await page.goto(url).then(() => true, () => false);

            var secret = await page.evaluate(function() {
              return document.querySelector('input[type=password]').value;
            });

            console.log(['secret', secret]);

            setTimeout(function() {
                resolve("Thank you");
            }, 2000);
        });
    };
}, function(err) {
    console.log(err);
});
