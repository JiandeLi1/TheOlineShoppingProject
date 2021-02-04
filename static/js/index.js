window.addEventListener('load', function () { 
    var arrow_l = document.querySelector('.arrow-l');
    var arrow_r = document.querySelector('.arrow-r');
    var focus = document.querySelector('.focus');
    focus.addEventListener('mouseenter', function () { 
        arrow_l.style.display = 'block';
        arrow_r.style.display = 'block';
        clearInterval(timer);
        timer = null;
    });
    focus.addEventListener('mouseleave', function () { 
        arrow_l.style.display = "none";
        arrow_r.style.display = "none";
        timer=setInterval(function () { 
        arrow_r.click();
        },2000)
    });

    function go_slow(obj,target,callback){
        clearInterval(obj.timer);
        obj.timer = setInterval(function () {
            var step = (target - obj.offsetLeft) / 10;
            step =step > 0 ? Math.ceil(step) : Math.floor(step);
            if (obj.offsetLeft == target){
                clearInterval(obj.timer);
                callback && callback();
                console.log('gg');
            }else{
                // console.log(Math.ceil((target - obj.offsetLeft) / 10));
                obj.style.left = obj.offsetLeft+ step +'px';
            }

        },15);

    }

    


    var ul = focus.querySelector('ul');
    var ol = focus.querySelector('ol');
    
    var focusWidth = focus.offsetWidth;
    
    var num = 0;
    var flag = true;
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
            num = index;
            go_slow(ul, -index * focusWidth);
           
        })
    }

    ol.children[0].className = 'current';
    var first = ul.children[0].cloneNode(true);
    ul.appendChild(first);
    var flag = true;
    arrow_r.addEventListener('click', function () { 
        if (flag) { 
            flag = false;
            if (num == ul.children.length-1) {
            ul.style.left = 0 + 'px';
            num = 0;
        }
        num++;
            go_slow(ul, -num * focusWidth, function () {
                flag = true;
            });
            
        for (let i = 0; i < ol.children.length; i++) { 
            ol.children[i].className = '';
        }
        
        if (num == ol.children.length)
        { ol.children[0].className = 'current'; }
        else {
            ol.children[num].className = 'current';
        }
        }
    })

    arrow_l.addEventListener('click', function () { 
        if (flag) {
            flag = false;
            if (num == 0) {
                ul.style.left = -(ul.children.length - 1) * focusWidth + 'px';
                num = ul.children.length - 1;
            }
            num--;
            go_slow(ul, -num * focusWidth, function () {
                flag = true;
            });
        
            for (let i = 0; i < ol.children.length; i++) {
                ol.children[i].className = '';
            }
            ol.children[num].className = 'currpiytrent';
        }
    })


    var timer = setInterval(function () { 
        arrow_r.click();
    }, 2000)
    



    var sliderbar=document.querySelector('.slider_bar');
    var main=document.querySelector('.main');
    // var body = document.querySelector('.body');
    var back=document.querySelector('.back');
    var mainTop= main.offsetTop;
    var sliderbarTop=sliderbar.offsetTop;
    // var bodyTop=body.offsetTop;
    function go_black(obj,target,callback){
        clearInterval(obj.timer);
        obj.timer = setInterval(function () {
            var step = (target - window.pageYOffset) / 10;
            step =step > 0 ? Math.ceil(step) : Math.floor(step);
            if (window.pageYOffset == target){
                clearInterval(obj.timer);
                callback && callback();
                console.log('gg');
            }else{
                // console.log(Math.ceil((target - obj.offsetLeft) / 10));
                // obj.style.left = obj.pageYOffset + step + 'px';
                window.scroll(0, window.pageYOffset + step);
            }

        },15);

    }
    document.addEventListener('scroll', function () {
          
            if (window.pageYOffset >= mainTop){
                sliderbar.style.position ='fixed';
                sliderbar.style.top= sliderbarTop - mainTop  +'px';

            }else{
                sliderbar.style.position = 'absolute';   
                sliderbar.style.top= sliderbarTop+'px'   
            }

        })


        document.addEventListener('scroll', function () {

                if (window.pageYOffset >= mainTop) {
                    back.style.display='block';

                } else {
                    
                    back.style.display = 'none';
                }

        })
    
    back.addEventListener('click', function () { 
        go_black(window,0);
    });



})