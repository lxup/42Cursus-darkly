# Form Parameter Tampering

In the survey form (`/?page=survey`), the grade section is handled like this:
```html
<select name="valeur" onchange="javascript:this.form.submit();">
	<option value="1">1</option>
	<option value="2">2</option>
	<option value="3">3</option>
	<option value="4">4</option>
	<option value="5">5</option>
	<option value="6">6</option>
	<option value="7">7</option>
	<option value="8">8</option>
	<option value="9">9</option>
	<option value="10">10</option>
</select>
```
If there is no server-side validation, you can tamper with the `valeur` parameter to submit a grade higher than 10. For example, you can change the value to `100` or any other number greater than 10. Example:
```html
<select name="valeur" onchange="javascript:this.form.submit();">
	<!-- ... other options ... -->
	<option value="100">100</option>
</select>
```