window.addEventListener('load', function () {
	document.querySelector('.submit').onclick = function () {
		var input_username = document.querySelector(".userName").value;
		var input_password = document.querySelector(".passWord").value;
			
		var xhr = new XMLHttpRequest();
        xhr.open("POST", "/login");
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		// can't send parameters with md5 decrypt.
		// xhr.send("userName=" + input_username + "&passWord=" + md5(input_password));
		xhr.send("userName=" + input_username + "&passWord=" + input_password);
		xhr.onreadystatechange = function () {
			if (xhr.readyState == 4 && xhr.status == 200) {
				var res = JSON.parse(xhr.responseText);
				if (res.status == 'success') {
					alert("Login successful.");
					window.location.href = res.redirctUrl;
				}
				else {
					alert(res);
				}
			}
		}
	}
})