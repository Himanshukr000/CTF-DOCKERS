const express = require('express');
const http = require('http');
const url = require('url');
const WebSocket = require('ws');
var net = require('net');

const app = express();

app.use(express.static('public'));

const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

var watcher;

function reconnectWatcher() {
    watcher = new net.Socket();

    watcher.connect(6379, '127.0.0.1', function() {
        watcher.write("client setname THE_DB_MASTER_IS_WATCHING_YOU_DCI{minoux_v18446744073709551615}\r\n");
    });

    watcher.on('close', function() {
        reconnectWatcher();
    });
}

reconnectWatcher();

wss.on('connection', function connection(ws, req) {
    const location = url.parse(req.url, true);

    var redis = new net.Socket();
    redis.connect(6379, '127.0.0.1');

    ws.on('message', function incoming(message) {
        console.log('received: %s', message);

        message = JSON.parse(message);

        if(message.room) {
            message.room = message.room.replace(/[^a-z0-9]/g, '');
        }

        if(message.type == 'publish') {
            redis.write(['zadd', 'rooms:' + message.room, +new Date, message.data].join(' ') + "\x0d\x0a");
        } else if(message.type == 'messages') {
            redis.write(['zrange', 'rooms:' + message.room, '0', '-1'].join(' ') + "\x0d\x0a");
        }
    });

    redis.on('data', function(data) {
        ws.send(data.toString());
    });

    redis.on('close', function() {
        ws.terminate();
    });

    ws.on('close', function() {
        redis.destroy();
    });
});

server.listen(8080, function listening() {
    console.log('Listening on %d', server.address().port);
});
