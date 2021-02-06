window.addEventListener('load', function () { 
    var search = document.querySelector('.search');
    var product = search.querySelector('input');
    var btn = search.querySelector('.submitbtn');
    console.log(product.value);
    
    btn.addEventListener('click', function () {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/searchProduct");
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send("itemName=" + product.value);
		xhr.onreadystatechange = function () {
			if (xhr.readyState == 4 && xhr.status == 200) {
                var res = xhr.responseText;
                
                if (res != null) {
                    var search = localStorage.getItem('search') ? localStorage.removeItem('search') : 0;
                
                    localStorage.setItem('search', res);
                    // localStorage.setItem('search', res);
                    console.log(localStorage.getItem('search'));
                    window.location.href = "/search";
				}
                else {
                    let search = localStorage.getItem('search') ? localStorage.removeItem('search') : 0;
                    var li = '<ul><li><h1>No result</h1></li></ul>';
                    localStorage.setItem('search', li)
                     window.location.href = "/search";
				}
            }
            else {
                    let search = localStorage.getItem('search') ? localStorage.removeItem('search') : 0;
                    var li = '<h1 style="font-size:20px;">No result</h1>';
                    localStorage.setItem('search', li)
                     window.location.href = "/search";
                }
        }
        return false;
    })



     document.addEventListener('keydown', function (e) { 
        if (e.key === "Enter") {
            btn.click();
        }
        else { 
            return false;
        }
    })

})
