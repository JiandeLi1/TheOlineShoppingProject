window.addEventListener('load', function () {


		var phone_box = document.querySelector(".phone_box");
			
		var xhr = new XMLHttpRequest();
      xhr.open("GET", "/allProducts");
		// xhr.setRequestHeader("Content-type", "application/json");
		xhr.send();
		xhr.onreadystatechange = function () {
			if (xhr.readyState == 4 && xhr.status == 200) {
        var res = xhr.responseText;
        // var res = JSON.stringify(res);
        var endIndex = res.length-3;
        var sub = res.substring(31,endIndex);
        var arr = sub.split("},");
        var product = '<ul>';
        console.log(res);
        console.log(sub);
         console.log(arr);

        var str = '';
				// if (res.status == 'success') {
        for (let i = 0; i < arr.length; i++){
          var ar = arr[i].split(","); 
          var a = ar[0].split(":"); 
          var c = '';

          // if (ar.length > 4) {
          //   for (let b = 3; b < ar.length; b++) { 
          //     ar[2] += ar[b];
          //   }
          // }


          console.log(ar);
          console.log(ar[3]);
           console.log(ar[3].substring(17, ar[3].length-1));

          c = "<li><div class='small_box'><img src='" + ar[3].substring(18, ar[3].length-1) + " ' alt=''><p>" + ar[0].substring(15, ar[0].length - 1) + "</p><div class='price'>$" + ar[1].substring(9) + "<span>$" + (parseInt( ar[1].substring(9)) + 100) + "</span><div class='sold'><span class='sold_percen'>Sold " + ar[2].substring(10) + "%</span><span class='bar'><div></div></span><span class='sold_percen'>" + (100 - parseInt(ar[2].substring(10))) + " left</span></div><button class='buy_product'><a href='javascript:;'>Buy Now!</a></button></div></li>"
          product += c;
          }
        product += "</ul>";
         console.log(product);
        phone_box.innerHTML=product;
					
				// }
				// else {
				// 	alert(res);
				// }
			}
		}
      
        // $.ajax({
        //   type:"post",
        //   url:"/getProduct",
        //   dataType:"json",
        //   success:function(res){
        //   var str = "<ul>";
        //   $.each(res.fake_product, function(idx,val) {
        //     str +="<li><div class='small_box'><img src='{{ url_for"+res[idx].itemImageUrl+" }}' alt=''><p>"+res[idx]+"</p><div class='price'>"+res[idx].price+"<span>$1100</span><div class='sold'><span class='sold_percen'>Sold "+res[idx].amount+"%</span><span class='bar'><div></div></span><span class='sold_percen'>"+100-parseInt(res[idx].amount)+"</span></div><button class='buy_product'><a href='javascript:;'>Buy Now!</a></button></div></li>"
        //   });
        //   str += "</ul>";
        //   $('.phone_box').append(str);
        //   },error:function(){
        //   alert(error)
        //   }
        // });
  
      
  
  
  // <li>
  //                       <div class="small_box">
  //                           <img src="{{ url_for('static',filename='upload/IP12.png') }}" alt="">
  //                           <p>&#9818;Apple iPhone 12&#9818;</p>
  //                           <div class="price">
  //                             $1200 <span>$1100</span>
  //                             <div class="sold">
  //                                <span class="sold_percen">Sold 85%</span> 
  //                                <span class="bar"><div></div></span> 
  //                                <span class="sold_percen">25 left</span>
  //                             </div>
  //                             <button class="buy_product">
  //                                 <a href="javascript:;">Buy Now!</a>
  //                             </button>
  //                       </div>
  //                   </li>






    // var buy = document.querySelector('.buy_product');
    // //  var Car = document.querySelector(".shoppingCart");
    // const AllData = [];

    
    // buy.onclick = function () {
    //   count(true)
    //   console.log("gg");
    //   }
 
     
 
      // function count(flag) {
      //   let count = localStorage.getItem('count')?JSON.parse(localStorage.getItem('count')).count:0;
        
      //   let countObj = {
      //       Name: "iphone",
      //       price: 1200,
      //       amount: 1
      //   }
        
      //     localStorage.setItem('count', JSON.stringify(countObj))
      //     console.log(localStorage.getItem('count'));
      // }
        
  let aaa = 'hh';


  var clock = document.querySelector('.clock');

  clock.onclick=function(){ 
    aaa = 'ABCD';
    console.log(aaa);
  };

  exports = {aaa}
    
    
    
});