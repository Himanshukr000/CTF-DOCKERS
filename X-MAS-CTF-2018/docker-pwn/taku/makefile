#Example build file for working with docker
challname=cyberdelia
all:
	arm-linux-gnueabi-gcc $(challname).c -fno-stack-protector -static -std=gnu99 -o chall
deploy:
	#strip chall
	#cp /lib/x86_64-linux-gnu/libc.so.6 bin/libc.so.6_$(shell md5sum /lib/x86_64-linux-gnu/libc.so.6 | cut -f1 -d ' ')
	cp chall bin/$(challname)_$(shell md5sum chall | cut -f1 -d ' ')
	tar czvf $(challname).tar.gz bin/*

	cp -r docker $(challname)_deploy
	cp flag $(challname)_deploy/flag
	cp chall $(challname)_deploy/chall
	tar czvf $(challname)_DEPLOY.tar.gz $(challname)_deploy
	rm -rf $(challname)_deploy
clean:
	rm bin/*
	rm $(challname).tar.gz
	rm $(challname)_DEPLOY.tar.gz