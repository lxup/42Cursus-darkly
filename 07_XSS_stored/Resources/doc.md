# Stored XSS

In the feedback form (`/?page=feedback`), there is two input, one for the name and one for the message. We can possibly inject a script in the message input. As the message is displayed to everyone, we could inject a script that will be executed in the browser of anyone who views the feedback page.

Every form submission need to be validated server-side to prevent this kind of attack.