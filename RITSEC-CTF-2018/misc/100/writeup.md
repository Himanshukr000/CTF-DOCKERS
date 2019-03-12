# MISC: Patch Patch

It's simple really. Patch patch.

## Step 1: Setup
Get on a Centos 7 VM and copy over `patch-patch.patch` and `patch-2.7.1-10.el7.centos.src.rpm`.
Update the repositories and install some common build tools.
```
yum update -y
yum install -y gcc rpmdevtools yum-utils
```

Now that we have everything we need, install all the build dependancies for patch
```
yum-builddep -y patch
```

Tell rpm where the new build directory is at
```
echo '%_topdir	%(echo $HOME)/rpms' > ~/.rpmmacros
```



## Patching

Unpack the source RPM
```
rpm -ivh patch-2.7.1-10.el7.centos.src.rpm
```


Now all the files for the build are in `~/rpms`. We can copy the patch file into the SOURCES with all the other patches.
```
cp ~/patch-patch.patch ~/rpms/SOURCES/
```

Edit the SPEC file to add in the new patch. `vim ~/rpms/SPECS/patch.spec`

We can see where the last patch was included into the package on line `13`. We will add our patch right after that
```
Patch5: patch-2.7.1-RITSEC.patch

Patch6: patch-patch.patch              # <---- Our new patch
```

And again after line `48`
```
%patch5 -p1 -b .ritsec

%patch6 -p1 -b .patchpatch
```


## Getting the Flag
After the patch is installed, all we need to do is build
```
cd ~/rpms
rpmbuild -bb SPECS/patch.spec
```


If the patch has been properly applied, the build will break and spit out the flag!