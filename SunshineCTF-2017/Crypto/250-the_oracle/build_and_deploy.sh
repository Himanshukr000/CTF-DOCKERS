docker build -t the_oracle .
docker run -t -p 40002:40002 --name the_oracle --detach --restart=unless-stopped the_oracle
