# Unsecure Directories : Root Password exposed

A good way to discover some url in a website is to read the `robots.txt` file. This file is used to tell search engines which pages they should not index. If we go to `http://[ip]/robots.txt`, we can see:
```txt
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```
Let's first try to access the `/whatever` directory. If we go to `http://[ip]/whatever`, we can see a file named `htpasswd`. This file contains the root password of the server:
```txt
root:437394baff5aa33daa618be47b75cb49
```
If we go to `http://[ip]/admin` (which is a common admin path), we can see a login form. If we enter `root` as username and we use the decrypted (MD5) password `qwerty123@` (from the `htpasswd` file).

# How to prevent it
Don't expose sensitive files in the web server. The `robots.txt` file should not contain sensitive information. Generally, when we want to hidden path in the `robots.txt` file, it's because we don't want search engines to index them, not because we want to hide them from users (they can still access them).