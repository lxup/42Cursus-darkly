# Unsecure Directories : Files exposed

Based on the `robots.txt` file, we can see that the `/.hidden` directory is disallowed for search engines. This often indicates that it contains sensitive files or directories that should not be publicly accessible. If we go to `http://[ip]/.hidden`, we can see a directory listing with several directories, all containing README files.

We gonna use a Python script to crawl through the directories and find the flag. The script will start from the `/.hidden` directory and recursively explore all subdirectories, looking for files that might contain the flag.

# How to prevent it
Same as the previous snippet, don't expose sensitive files in the web server.