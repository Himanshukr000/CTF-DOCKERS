docker run --cpus=".1" --memory="120m" --name xnmas -p16000:2000 xnmas &
docker run --cpus=".1" --memory="100m" --name rabbit -p16003:2000 rabbit &
docker run --cpus=".1" --memory="100m" --name blackrabbit -p16004:2000 blackrabbit &
docker run --cpus=".2" --memory="200m" --name santaslist -p16001:2000 --restart always santaslist &
docker run --cpus=".2" --memory="200m" --name santaslist2 -p16002:2000 --restart always santaslist2 &
docker run --cpus=".1" --memory="120m" --name dilemma -p14001:2000 dilemma &
docker run --cpus=".1" --memory="120m" --name nimgame -p14002:2000 --restart always nimgame &
docker run --cpus=".1" --memory="120m" --name sequences -p14003:2000 sequences &
docker run --cpus=".1" --memory="80m" --name torvald -p14004:22 torvald &

cd /home/ctf/docker-pwn/fd/; ./start_chall.sh
cd /home/ctf/docker-pwn/wasm/; ./start_chall.sh
cd /home/ctf/docker-pwn/http_pwn/; ./start_chall.sh
cd /home/ctf/docker-pwn/randlib/; ./start_chall.sh
cd /home/ctf/docker-pwn/taku/; ./start_chall.sh
cd /home/ctf/docker-pwn/taku2/; ./start_chall.sh
cd /home/ctf/docker-pwn/greet/; ./start_chall.sh
cd /home/ctf/docker-pwn/notrop/; ./start_chall.sh

docker run --cpus=".1" --memory="100m" --name mechagnome mechagnome &
docker run --cpus=".2" --memory="360m" --name santalogin -p12003:80 santalogin &
docker run --cpus=".1" --memory="100m" --name monolith -p12000:80 monolith &
docker run --cpus=".5" --memory="1024m" --name minecraft -p14000:2000 -p25565:25565 minecraft &
docker run --cpus=".5" --memory="100m" --name monolith2 -p12006:80 monolith2 &
docker run --cpus=".1" --memory="100m" --name luckynumber -p12005:80 luckynumber &
docker run --cpus=".1" --memory="100m" --name wishlist -p12001:80 wishlist &
docker run --cpus=".1" --memory="100m" --name gnomearena -p12002:80 gnomearena &
docker run --cpus=".1" --memory="100m" --name gnomebuttons -p12004:80 gnomebuttons &
docker run --cpus=".1" --memory="120m" --name vault -p12007:80 vault &
docker run --cpus=".1" --memory="100m" --name cookies -p12008:80 cookies &
docker run --cpus=".1" --memory="120m" --name savechristmas -p18000:2000 savechristmas &