window.addEventListener('load', function () {


    var phone_box = document.querySelector(".phone_box");
			
    var res = localStorage.getItem('search');
    
   
    
      
    if (res != '<h1 style="font-size:20px;">No result</h1>') {

       
          var ar = res.split(","); 
          var product = '<ul>';

          // if (ar.length > 4) {
          //   for (let b = 3; b < ar.length; b++) { 
          //     ar[2] += ar[b];
          //   }
          // }


          console.log(ar);
          console.log(ar[3]);
           console.log(ar[3].substring(17, ar[3].length-1));

          product = "<li><div class='small_box'><img src='" + ar[4].substring(18, ar[4].length-3) + " ' alt=''><p>" + ar[1].substring(23, ar[1].length - 1) + "</p><div class='price'>$" + ar[2].substring(9) + "<span>$" + (parseInt( ar[2].substring(9)) + 100) + "</span><div class='sold'><span class='sold_percen'>Sold " + ar[3].substring(10) + "%</span><span class='bar'><div></div></span><span class='sold_percen'>" + (100 - parseInt(ar[3].substring(10))) + " left</span></div><button class='buy_product'><a href='javascript:;'>Buy Now!</a></button></div></li>"
          
          
        product += "</ul>";
        phone_box.innerHTML=product;
    } else { 
        phone_box.innerHTML = res;
    }
           
});