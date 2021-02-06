window.addEventListener('load', function () {
    var cart = document.querySelector(".shoppingCart ul");

    // var li =document.createElement("li");
    // li.innerHTML += localStorage.getItem('count');
    // console.log(li);
    
    var arr = JSON.parse(localStorage.getItem('products'));
    var data = arr.filter((arr, index, self) =>
        index === self.findIndex((t) => (t.Name === arr.Name && t.price === arr.price)))
    localStorage.setItem('products', JSON.stringify(data));
    
    // var arr = data;
    // console.log(arr);
    // console.log(arr.price);
    // console.log(typeof(arr));

    
 
    data.forEach((item) => {
        console.log(data.length);
        var oDiv = document.createElement("div");
        oDiv.className = "row hid";
        oDiv.innerHTML += '<div class="check left"> <i class="i_check" id="i_check" onclick="i_check()" >√</i></div>';
        oDiv.innerHTML += '<div class="img left"><img src="' + item.img + '" width="80" height="80"></div>';
        oDiv.innerHTML += '<div class="name left"><span>' + item.Name + '</span></div>';
        oDiv.innerHTML += '<div class="price left"><span>' + item.price + '</span></div>';
        oDiv.innerHTML += ' <div class="item_count_i"><div class="num_count"><div class="count_d">-</div><div class="c_num">' + item.amount + '</div><div class="count_i">+</div></div> </div>'
        oDiv.innerHTML += '<div class="subtotal left sub_price"><span>' + item.price * item.amount + '</span></div>'
        oDiv.innerHTML += '<div class="ctrl left"><a href="javascript:;">×</a></div>';
        cart.appendChild(oDiv);
       
    })
    
    getAmount();
    //   window.addEventListener('storage', function (event) {
    //     console.log(JSON.parse(event.newValue).count);
    //      cart.textContent = JSON.parse(event.newValue).count
    //   })

    var i_btn = document.getElementsByClassName("count_i");
    for (let k = 0; k < i_btn.length; k++) {
        i_btn[k].onclick = function () {
            bt = this;
            at = this.parentElement.parentElement.nextElementSibling;
            pt = this.parentElement.parentElement.previousElementSibling;
            node = bt.parentNode.childNodes[1];
            console.log(node);
            num = node.innerText;
            num = parseInt(num);
            num++;
            node.innerText = num;
            price = pt.innerText;
            price = price.substring(0, price.length);
            at.innerText = price * num;
            arr.amount = num;
            console.log(arr.amount);
            let a = JSON.parse(localStorage.getItem("products"));
            console.log(k);
            a[k].amount = num;
            localStorage.setItem('products', JSON.stringify(a));
            getAmount();
        }
    }
    var d_btn = document.getElementsByClassName("count_d");
    for (let k = 0; k < i_btn.length; k++) {
        d_btn[k].onclick = function () {
            bt = this;
            at = this.parentElement.parentElement.nextElementSibling;
            pt = this.parentElement.parentElement.previousElementSibling;
            node = bt.parentNode.childNodes[1];
            num = node.innerText;
            num = parseInt(num);
            if (num > 1) {
                num--;
                arr.amount = num;
                let a = JSON.parse(localStorage.getItem("products"));
                a[k].amount = num;
                localStorage.setItem('products', JSON.stringify(a));
            }
            console.log(arr.amount);
            node.innerText = num;
            price = pt.innerText;
            price = price.substring(0, price.length);
            at.innerText = price * num;
                                
            getAmount();
        }
    }
    

    var delBtn = document.querySelectorAll('.ctrl a');
    // var cart_list=document.querySelectorAll('#list ul li');
    for (let i = 0; i < delBtn.length; i++) {
        delBtn[i].onclick = function () {
            var result = confirm("Delete?");
            // let b = cart_list.childNodes[i];
            
            //cart_list.removeChild(delBtn[i].parentElement);
            if (result) {
                let a = JSON.parse(localStorage.getItem("products"));
                let b = delBtn[i].parentElemen;
                a.splice(i, 1);
                localStorage.setItem('products', JSON.stringify(a));
                cart.removeChild(cart.childNodes[i]);
                getAmount();
            }
        }
    }
    

    // var index = false;
    //         function checkAll() {
    //             var choose = document.getElementsByClassName("shoppingCart")[0].getElementsByTagName("i");
    //             // console.log(choose);
    //             if (choose.length != 1) {
    //                 for (i = 1; i < choose.length; i++) {
    //                     if (!index) {
    //                         choose[0].classList.add("i_acity2")
    //                         choose[i].classList.add("i_acity");
    //                     } else {
    //                         choose[i].classList.remove("i_acity");
    //                         choose[0].classList.remove("i_acity2")
    //                     }
    //                 }
    //                 index = !index;
    //             }
    //             getAmount();
    // }
    

    // var check = oDiv.firstChild.getElementsByTagName("i")[0];
    //                     check.onclick = function() {
    //                         // console.log(check.className);
    //                         if (check.className == "i_check i_acity") {
    //                             check.classList.remove("i_acity");

    //                         } else {
    //                             check.classList.add("i_acity");
    //                         }
    //                         getAmount();
    // }
    

    function getAmount() {
        ns = document.getElementsByClassName('sub_price');
        sum = 0;
        if (ns.length == 0) {
            document.getElementById("price_num").innerText = 0;
            return true;
        }
        
        for (y = 0; y < ns.length; y++) {
            
            sum += parseInt(ns[y].innerText);
            console.log(sum);
            document.getElementById("price_num").innerText = sum;
        }

        console.log(document.getElementsByClassName('sub_price'));
        console.log(ns.length);
        
    }
            
    var pay = document.querySelector('#pay');
    pay.addEventListener('click', () => {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/checkout_page");
        xhr.send();
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                window.location.href = '/checkout_page';
            }
            else { 
                alert(xhr.responseText);
            }
        }
    })
    

        
});