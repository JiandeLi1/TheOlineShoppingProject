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

    var data = JSON.parse(localStorage.getItem('count'));
    var arr = data;
    var cart = document.querySelector("#shoppingcart_section ul");
    var li = document.createElement("li");
    li.innerHTML="<div style='padding:0 5px;'><div>"+arr.Name+" <span style='float: right;'>item sum:"+ arr.price*arr.amount+"</span></div> <span>amount:"+arr.amount+"<span><hr style='width:290px'></div>";
    cart.appendChild(li);
    var totle = document.querySelector("#totle");
    totle.innerHTML = arr.price * arr.amount;

    


});