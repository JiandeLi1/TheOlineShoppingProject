window.addEventListener('load', function () { 
var cart = document.querySelector(".shoppingCart ul");
var arr = JSON.parse(localStorage.getItem('products'));
    
    arr.forEach(item => {
        
        var oDiv = document.createElement("div");
                        
                        oDiv.className = "row hid";
                        oDiv.innerHTML += '<div class="img left"><img src="' +item.img + '" width="80" height="80"></div>';
                        oDiv.innerHTML += '<div class="name left"><span>' + item.Name + '</span></div>';
                        oDiv.innerHTML += '<div class="price left"><span>' +  item.price + '</span></div>';
                        oDiv.innerHTML += "<div class='left' style='width:50px; text-align: center;margin:0 20px 0 0;'>" + item.amount + "</div>";
                        oDiv.innerHTML += '<div class="subtotal left sub_price" style="text-align:center; width:180px;"><span>' + item.price*item.amount + '</span></div>'
                        
    cart.appendChild(oDiv);
    });
    
    getAmount();
    //   window.addEventListener('storage', function (event) {
    //     console.log(JSON.parse(event.newValue).count);
    //      cart.textContent = JSON.parse(event.newValue).count
    //   })

   

    function getAmount() {
        ns = document.getElementsByClassName('sub_price');
        sum = 0;
        
        
        for (y = 0; y < ns.length; y++) {
            
            sum += parseInt(ns[y].innerText);
            console.log(sum);
            document.getElementById("price_num").innerText = sum;
        }

        console.log(document.getElementsByClassName('sub_price'));
        localStorage.removeItem('products');
        item_count.style.display = 'none';
         item_count.innerHTML = '';
        
    }
            
        
});