# Header manipulation

At the bottom of the page there is a link to `http://[ip]/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`. In this page, we can see in the source code (with inspector) :
```html
<!-- some code -->

<!--
You must come from : "https://www.nsa.gov/".
-->

<!-- some other code -->

<!--
...
Let's use this browser : "ft_bornToSec". It will help you a lot.
...
-->
```

This indicates that the page expects a specific referrer header to be set (`https://www.nsa.gov/`) and a specific user agent header to be set (`ft_bornToSec`). If we try accessing the page with these headers using curl:
```bash
curl -e https://www.nsa.gov/ -A "ft_bornToSec" "http://[ip]/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
```
We will see the content of the page.