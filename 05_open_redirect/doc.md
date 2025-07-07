# Open Redirect

In the footer, social media links are handle like this:
```html
<a href="index.php?page=redirect&amp;site=instagram" class="icon fa-instagram"></a>
```

It uses a redirection page to handle the links. This represents a security risk, as it allows for open redirects.

It can be exploited by changing the `site` parameter to a different URL. For example, if you change it to `site=https://evil.com`, it will redirect to that site instead of Instagram. Victims can think they are clicking on a legitimate link, because of the domain name `https://mygoodblog.com/index.php?page=redirect&site=https://evil.com`, but they will be redirected to a malicious site.