document.querySelector('.submit').onclick = function() {
			var input_username = document.querySelector(".userName").value;
			var input_password = document.querySelector(".passWord").value;
			
			var xhr = new XMLHttpRequest();	
			xhr.open("POST", "/login");
			xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
			xhr.send("username="+input_username+"&password="+md5(input_password));
			xhr.onreadystatechange = function() {
				if(xhr.readyState==4 && xhr.status==200) {
					// 登录成功则跳转
					var res = JSON.parse(xhr.responseText);
					if(res!=="{'status' : 'user not found.'}") {
						window.location.href ="./index";
					}
					else {
						alert(res);
					}
				}
			}
		}