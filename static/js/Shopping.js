window.addEventListener('load', function () {
    var buy = document.querySelector('.buy_product');
    //  var Car = document.querySelector(".shoppingCart");
    const AllData = [];

    
    buy.onclick = function () {
      count(true)
      console.log("gg");
      }
 
     
 
      function count(flag) {
        let count = localStorage.getItem('count')?JSON.parse(localStorage.getItem('count')).count:0;
        
        let countObj = {
            Name: "iphone",
            price: 1200,
            amount: 1
        }
        
          localStorage.setItem('count', JSON.stringify(countObj))
          console.log(localStorage.getItem('count'));
      }
        
    
    
    
    
});