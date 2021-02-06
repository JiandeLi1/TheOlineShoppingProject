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
				let user = localStorage.getItem('user') ? localStorage.removeItem('user') :input_username;
				localStorage.setItem('user', input_username);
						
				var res = JSON.parse(xhr.responseText);
				if (res.status == 'success') {
					// document.cookie = "userName" + input_username;
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