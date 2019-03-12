#! /bin/bash
cd /home/ctf
sudo -u ctf socat tcp-l:10004,reuseaddr,fork exec:./random_exe_name,pty
