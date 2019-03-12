#!/bin/bash

function main() {
    out=$(echo "everybodyrockyourbody" | nc 18.220.56.147 12345)
    if [[ $out == *"TUCTF{5w337_dr34m5_4r3_m4d3_0f_7h353}"* ]]; then
	return 1
    fi
}

main
