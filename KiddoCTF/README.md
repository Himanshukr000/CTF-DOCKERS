# KiddoCTF - a Docker Linux-based intro to CTFs (Capture The Flag challenges)

## Introduction & Audience

This CTF is aimed at students ages 12-15 (Middle School). These challenges are meant as more of a pre-cursor for PicoCTF, EasyCTF, HSCTF, and the like.

Since this CTF is based on Docker, some assistance is required by a mentor or teacher to help the student get the Docker Linux container instance up and running.

To submit answers, have the students write it down on paper or on their computer using an app like notepad or notes.

Some of the challenges have extra practice commands to help the student learn more

Spoil Alert: The flags are all in the Dockerfile so don't let the student see that first!

## Usage
This assumes some level of familiarity with Docker and Git, otherwise, here's some links to help get you started:

* https://git-scm.com/book/en/v1/Getting-Started-Installing-Git (I recommend using Homebrew)
* https://docs.docker.com/engine/installation/

#### Build this Docker Image yourself
    git clone https://github.com/IPvFletch/KiddoCTF.git
    cd KiddoCTF
    docker build -t kiddoctf .
    docker run --rm -ti kiddoctf:latest

#### Run a Container [default: downloads from Docker Hub]
    docker run --rm -ti ipvfletch/kiddoctf:latest

## KiddoCTF Instructions [print out and provide to students]
Flags will look like this: FLAGX_12345

These commands will get you back where you started if you get lost in directories:

    cd ~
or

    cd /home/centos

Check your current dir:

    pwd
    ls -l

If you see ` ` marks, it means the command to run is `inside` those marks.
Do not type the ` ` characters when you run the command.

## Challenges

#### 01 linux i
* cd ~
* find a file that is the flag hidden in some directory
* use `ls -l` and cd <dirname>` to find the filename flag
* practice: try `ls -l /home`

#### 02 linux ii
* cd ~
* use `ls --help` to find the hidden .dir directory(s)
* `cat file` reveals the flag
* practice: try `cat /etc/passwd` or `cat /etc/shadow`

#### 03 linux iii
* run cat` or `strings` on /tmp/.flag3
* pipe the output (`|`) to grep, ex. `cat file | grep FLAG`
* practice: try `cat /var/log/yum.log` to see what apps have been erased/installed

#### 04 base64 encoded string
* Base64 decode the file /tmp/.flag4
* use `base64 --help`
* practice: try `echo YOURNAME | base64 | base64 -d`

#### 05 linux iv
* find flag on local port
* use nc to connect to google.com 80
* use curl to connect to google.com:80
* find the flag on localhost:80 to get the challenge
* you need to base64 decode this string to get the flag
* pipe the output to base64
* or echo it and pipe to base64

#### 06 linux v find a user id
* use `ps --help` to find the user of the `webserver` process
* using `id`, find the uid of user
* flag is the other user who belongs to that same group
* hint: look at /etc/group

#### 07 linux vi
* look in the ~www user's homedir to find the flag
* use `ls -l` to see dir/file permissions
* the owner/group are listed here

For example, this file is owned by user kfletcher and has group admin

    drwxr-xr-x 1 kfletcher admin 4096 Jul 27 16:20 KiddoCTF

The letters on the left also mean something
```
    d = directory or not
    r = read
    w = write
    x = exec/cd
    - = no permission
```

Together they look like:
```
    -wx > no Read
    r-x > no Write
    rw- > no eXecute
    r-- > no Write or eXecute
```

    -rw-r--r-- 1 root root 3812 Jul 27 16:31 flag.dmp
    drwxr-xr-x 2 root root 4096 Jul 26 01:40 flag_dir
    -rw-r--r-- 1 root root  177 Jul 26 01:12 oddfile

* the first 1 bit is the directory bit
* the next 3 bits are the Owner's permissions, rwx or not
* the next 3 bits are the Group's permissions, rwx, or not
* the last 3 bits are Everyone else's permissions, rwx or not

#### 08 networking
* find the routing table
* the flag is the default route for destination 0.0.0.0
* netstat --help

#### 09 visit a web service
* `curl localhost:8080`
* find an HTML comment tag which contains the flag
* https://www.w3schools.com/tags/

#### 10 web site
* `curl localhost:8080`
* look at the "cookies" being set by the server
* `curl --help` to find out which option turns on "Include protocol headers"
* Hint: The option you need is a single letter and rhymes with: Eye
* b64 decoder reveals flag

#### 11 run a python script
* run `python`
* paste the below script line by line and let it run
* find the `json` variable's `type` to reveal the flag
* To exit Python, run the function `exit()`
```
list = []
list.append('a')
list.append('b')
json = {'a': 'ayyy', 'b': 'be cool man'}
print json['a'] + ' ' + json['b']
print type(json)
print type(list)
print list[1]
print len(json)
```

#### 12 unknown filetype
* cd ~
* find out what kind of filetype `oddfile` is
* `head -1 oddfile`
* http://www.garykessler.net/library/file_sigs.html
* or `file <file>`
* `unzip` and `cat` it to reveal the flag

#### 13 nmap to find a [local] hidden port
* `nmap localhost`
* flag is the service name for the listener port beginning with 3

#### 14 analyze a tcpdump
* cd ~
* examine the TCP Dump (Packet Capture) and find the flag
* `tcpdump -r flag.dmp`
* use the `-n` flag to not resolve hostnames
* use `-A` to display the data trasnferred
* look for the flag data being sent > 216.58.218.142.80
* if you can't scroll back add `| more` to the very end of your tcpdump command
* press `[SPACEBAR]` to advance, or `q` to exit from `more`.

# End

### Optional Survey to get feedback

### Related Links
* https://github.com/EasyCTF/writeups-2014/blob/master/045-linux-basics-4.md
* https://jacobedelman.gitbooks.io/hsctf-3-practice-problems/content/

Author/Maintainer: @IPvFletch

