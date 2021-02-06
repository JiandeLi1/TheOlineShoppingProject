window.addEventListener('load', function () {

    var shipping = document.getElementById("shippingaddress");
    var c_box = document.getElementById("sameAddress");
    c_box.addEventListener('change', function (){
        if (this.checked == true) {
      
            shipping.style.display = "none";
      

        } else {
            shipping.style.display = "block";
        }
    });

    var data = JSON.parse(localStorage.getItem('products'));
    var totle = document.querySelector("#totle");
    var sum = 0;
    console.log(data);
    var cart = document.querySelector("#shoppingcart_section ul");
    data.forEach(item => {
        var li = document.createElement("li");
    li.innerHTML="<div style='padding:0 5px;'><div style='font-size:15px; font-weight:600;'>"+item.Name+" <span style='float: right;'>item sum:"+ item.price*item.amount+"</span></div> <span >amount:"+item.amount+"<span><hr style='width:290px'></div>";
    cart.appendChild(li);
    sum+=parseInt(item.price * item.amount); 
    
    });
    totle.innerHTML = sum;
    
    var username = document.querySelector('.user-input');
    var pay = document.querySelector('#check-out');
    pay.addEventListener('click', () => {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/thankyou");
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhr.send("userName=" + username.value );
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                window.location.href = '/thankyou';
            }
            else { 
                return;
            }
        }
    })

    


});