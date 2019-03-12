# docker-pwn

Docker setup for hosting pwnables

1) Install docker, ./prepare_docker.sh

2) Change name of challenge in docker-compose.yml, ctf_name => ctf_whatever

3) Change port to whatever in ctf.xinetd

4) Add a 'flag' file with the flag in it

5) Add the challenge binary as 'chall'

6) ./start_chall.sh
