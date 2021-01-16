window.addEventListener('load', function () { 
    var arrow_l = document.querySelector('.arrow-l');
    var arrow_r = document.querySelector('.arrow-r');
    var focus = document.querySelector('.focus');
    focus.addEventListener('mouseenter', function () { 
        arrow_l.style.display = 'block';
        arrow_r.style.display = 'block';
    });
    focus.addEventListener('mouseleave', function () { 
        arrow_l.style.display = "none";
        arrow_r.style.display = "none";
    });

    function go_slow(obj,target,callback){
        clearInterval(obj.timer);
        obj.timer=setInterval(function(){
            if (obj.offsetLeft === target){
                clearInterval(obj.timer);
                if (callback) {
                    callback(obj);
                }
            }else{
                // console.log(Math.ceil((target - obj.offsetLeft) / 10));
                obj.style.left = obj.offsetLeft+ Math.ceil((target - obj.offsetLeft)/10)+'px';
            }

        },10);

    }

    


    var ul = focus.querySelector('ul');
    var ol = focus.querySelector('ol');
    
    var focusWidth = focus.offsetWidth;
    
    
    for (let i = 0; i < ul.children.length;i++) { 
        var li = document.createElement('li');
        li.setAttribute('index',i);
        ol.appendChild(li);
        

        li.addEventListener('click', function () { 
            for (let i = 0; i < ol.children.length; i++) { 
                ol.children[i].className = '';

            }

            this.className = 'current';
            var index = this.getAttribute('index');
            
            go_slow(ul, -index * focusWidth);
           
        })
    }

    ol.children[0].className = 'current';

    var num = 0;
    arrow_r.addEventListener('click', function () { 
        if (num==0) { ul.style.left = 0 + 'px';}
        num++;
        console.log(num);
        go_slow(ul, -num * focusWidth);
        
        console.log(ul.style.left);
        if (ul.style.left ==-1433+'px' ) {
            console.log(-num * focusWidth);
            console.log(num);
            
            num = 0;
            console.log(ul.style.left);
           
        }
       
        
    })

     arrow_l.addEventListener('click', function () { 
        num--;
        go_slow(ul, -num * focusWidth);
    })

})