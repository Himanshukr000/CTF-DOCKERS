#!/bin/bash
FILES=./bots/*

kill -9 $(pidof chromium-browser)

# wait for web services to be ready
sleep 30;

while sleep 1; do
    for f in $FILES
    do
        if ! pgrep -x -f "nodejs $f" > /dev/null
        then
            echo "starting $f" 
            nodejs $f &
        fi
    done;
done;