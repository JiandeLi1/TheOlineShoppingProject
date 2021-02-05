window.addEventListener('load', function () {


    var phone_box = document.querySelector(".phone_box");
			
    var res = localStorage.getItem('search');
    
   
    
      
    if (res != '<h1 style="font-size:20px;">No result</h1>') {

        // var ar = res.split(",");
        // var a = ar[0].split(":");
        // var product = '';
        // console.log(ar);

        // if (ar.length > 3) {
        //     for (let b = 3; b < ar.length; b++) {
        //         ar[2] += ar[b];
        //     }
        // }


          

        // product = "<ul><li><div class='small_box'><img src='" + ar[2].substring(18, ar[2].length - 1) + " ' alt=''><p>" + a[0].substring(1) + "</p><div class='price'>$" + a[2].substring(1) + "<span>$" + (parseInt(a[2].substring(1)) + 100) + "</span><div class='sold'><span class='sold_percen'>Sold " + ar[1].substring(10) + "%</span><span class='bar'><div></div></span><span class='sold_percen'>" + (100 - parseInt(ar[1].substring(10))) + " left</span></div><button class='buy_product'><a href='javascript:;'>Buy Now!</a></button></div></li></ul>"
        
        /*
        The search api should return list of product that match the search key words.
        We have to display all of the products that backend return.
        */
        var items = JSON.parse(res)
        var products = '<ul>';
        
        items.forEach((item) => {
            let itemName = item.itemName;
            let price = item.price;
            let amount = item.amount;
            let itemImageUrl = item.itemImageUrl;
            products+= "<li><div class='small_box'><img src='" + itemImageUrl + " ' alt=''><p>" + itemName + "</p><div class='price'>$" + price + "<span>$" + (price + 100.00) + "</span><div class='sold'><span class='sold_percen'>Sold " + amount + "%</span><span class='bar'><div></div></span><span class='sold_percen'>" + (100 - amount) + " left</span></div><button class='buy_product'><a href='javascript:;'>Buy Now!</a></button></div></li>"
        });
        products+= "</ul>";

        phone_box.innerHTML = products;
    } else { 
        phone_box.innerHTML = res;
    }
           
});