window.addEventListener('load', () => {
  var buybtn = document.getElementsByClassName('buy_product');
  var i_photo = document.getElementsByClassName("i_photo");
  var i_name = document.getElementsByClassName("i_name");
  var i_price = document.getElementsByClassName("the_price");
  var i_amount = document.getElementsByClassName("i_amount");
    console.log(buybtn);
    console.log(i_photo);
    console.log(i_price);
    console.log(i_name)
    
    // function count(flag) {
    //   let count = localStorage.getItem('products')?JSON.parse(localStorage.getItem('products')).count:0;
      
      
      
    //     localStorage.setItem('count', JSON.stringify(countObj))
    //     console.log(localStorage.getItem('count'));
    // }
      
    setTimeout(function () { 
         for (let i = 0; i < buybtn.length; i++) {
            console.log(i_photo[i]);
            buybtn[i].addEventListener('click', () => {
                let p = localStorage.getItem('products') ? JSON.parse(localStorage.getItem('products')) : []
                 console.log(p);
               
          

                let Obj = {
                    Name: i_name[i].innerText,
                    price: i_price[i].innerText,
                    amount: 1,
                    img: i_photo[i].src
                }

                

                
                p.forEach((item) => {
                    if (Obj.Name == item.Name) {
                        return false;
                    }
                })
                p.push(Obj);

                localStorage.setItem('products', JSON.stringify(p))
                console.log(p);
            })
        }
    
    }, 1000);
    
   
       
      
})
