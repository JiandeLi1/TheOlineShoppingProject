window.addEventListener('load', function () {
    var password = document.getElementById('passWord');
    var comf_pw = document.getElementById('comfirm_pw');
    var comf_msg = document.querySelector('.comfirm_msg');
   



    var check = function () {
        if (comf_pw.value != '') {
            if (password.value == comf_pw.value) {
                comf_msg.style.color = '#06cc3e';
                comf_msg.innerHTML = "<i class='fas fa-check-circle'></i>Password matching";
                
            } else {

                comf_msg.style.display = 'inline-block';
                comf_msg.style.color = '#c81523';
                comf_msg.innerHTML = "<i class='fas fa-times-circle'></i>Both pass word aren't match";
                
            }
        }
        else {
            comf_msg.style.display = 'none';
        }
    }

        var eye = document.querySelector('#eye');
        var eye2 = document.querySelector('#eye2');
        
    var eyeOpen = function (obj, eyes) {
            if (eyes.className=='fas fa-eye-slash'){
                eyes.className="fas fa-eye";
                obj.type = 'text';
                flag=1;
            }else{
                eyes.className = "fas fa-eye-slash";
                obj.type = 'password';
                flag = 0;
            }
        }

    

    eye.onclick= function () { 
        eyeOpen(password,eye);
    };

     eye2.addEventListener('click', function () { 
        eyeOpen(comf_pw,eye2);
    });

    comf_pw.addEventListener('keyup', function () { 
        check();
    });
})



                 
