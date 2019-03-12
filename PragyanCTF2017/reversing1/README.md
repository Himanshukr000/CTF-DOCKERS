# Reversing Question 1
We are given the [mi6.exe](mi6.exe) binary. And the following cipher.
```
26 25 30 28 22 25 20 23 21 29 22 24 26 23 21 26 27 20 28 22 25 23 30 29 23 28 24 20
21 26 25 20 23 27 23 29 25 22 23 26 27 29 24 23 30 21 25 24 26 20 24 22 21 30 26 20
25 24 21 23 27 29 26 22 20 21 23 22 30 26 29 26 28 27 22 20 27 29 26 30 28 27 26 23
29 21 22 25 27 24 21 29 25 24 20 25 23 22 30 28 27 29 25 20 24 21 23 20 23 21 29 26
```

After running the file we see it is a bourne again shell script. However, there is also a lot of binary data in the file. After running strings we see the following string.
```
#!/bin/bash
export TMPDIR=`mktemp -d /tmp/selfextract.XXXXXX`
ARCHIVE=`awk '/^__ARCHIVE_BELOW__/ {print NR + 1; exit 0; }' $0`
tail -n+$ARCHIVE $0 | tar -xz -C $TMPDIR
CDIR=`pwd`
cd $TMPDIR
./installer reverse_1.rb false
cd $CDIR
rm -rf $TMPDIR
exit 0

```
Looks like the script creates a directory, extracts an embeded tar file and then runs ./installer with a ruby script as a parameter. I used binwalk to extract the payload.tar file and looked at installer.

```
#!/bin/bash
set -e

# Figure out where this script is located.
SELFDIR="`dirname \"$0\"`"
SELFDIR="`cd \"$SELFDIR\" && pwd`"
cd $SELFDIR/lib/app/

## GEMFILE
if [ -f "$SELFDIR/lib/vendor/Gemfile" ]
then
  # Tell Bundler where the Gemfile and gems are.
  export BUNDLE_GEMFILE="$SELFDIR/lib/vendor/Gemfile"
  unset BUNDLE_IGNORE_CONFIG

  # Run the actual app using the bundled Ruby interpreter, with Bundler activated.
  if $2; then
    export RAILS_ENV=production
    exec "$SELFDIR/lib/ruby/bin/ruby" -rbundler/setup "bin/rails" server
  else
    exec "$SELFDIR/lib/ruby/bin/ruby" -rbundler/setup "$1"
  fi
else
  exec "$SELFDIR/lib/ruby/bin/ruby" "$1"
fi
```

Looks like the interesting file is the first argument to installer reverse_1.rb. After executing the ruby script I saw the prompt that I was looking for. [This](reverse_1.rb) is the script.

After looking up some basic ruby. I decided to add some print statements to see what was going on. I realized our input was converted to uppercase and then each character was xor'ed with 61 and then split into a sum made up of values from 20 to 30.
So given the cipher text we do not know how many numbers makes up one letter. I created a small [script](solve.py) that would let me guess the values in the flag.

The final flag was: pragyanctf{flagsarecool}
