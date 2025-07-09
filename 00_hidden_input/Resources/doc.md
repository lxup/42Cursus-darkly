# Hidden Input

Just go in the forgot password page (`/?page=recover`), inspect the page. U should see a hidden input field inside a form. Remove the `type="hidden"` fromt the input.

# How to prevent it
You should not use hidden input fields to store sensitive information. Instead, use server-side logic to handle the password recovery process. Client should only send the email address of the user who wants to recover their password. The server should then send a password reset link to that email address or the one from the webmaster.