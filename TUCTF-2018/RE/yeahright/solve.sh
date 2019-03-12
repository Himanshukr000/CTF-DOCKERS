#!/bin/bash

function main() {
    out=$(echo "7h3_m057_53cr37357_p455w0rd_y0u_3v3r_54w" | nc 18.224.3.130 12345)
    if [[ $out == *"TUCTF{n07_my_fl46_n07_my_pr0bl3m}"* ]]; then
	return 1
    fi
}

main
