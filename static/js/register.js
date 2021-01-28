window.addEventListener('load', function () {
    var password = document.getElementById('passWord');
    var comf_pw = document.getElementById('comfirm_pw');
    var email = document.getElementById('email');
    var username = document.getElementById('username');
    var email_msg = document.querySelector('.email_msg');
    var username_msg = document.querySelector('.username_msg');
    var password_msg = document.querySelector('.password_msg');
    var comf_msg = document.querySelector('.comfirm_msg');
    var safe = document.querySelector('.safe');
    var Weak = safe.querySelector('.safe .weak');
    var middle = document.querySelector('.safe .mid');
    var Strong=document.querySelector('.safe .strong');
    var regEx_Uname = /^[A-Za-z0-9]{4,12}$/;
    var regEx_Email = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var email_error = "<i class='fas fa-times-circle'></i>  Email invalid";
    var username_error = "<i class='fas fa-times-circle'></i> Need 4-12 letters or numbers";
    var password_error = "<i class='fas fa-times-circle'></i>Need 6-12 characters";
   // var weak_level = /^[a-zA-Z0-9]{6,16}$/;
    var mid_level = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{6,16}$/;
    var strong_level= /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{10,16}$/;


    
    var check = function (obj,obj_msg,obj_error,regEx) { 
        if (obj.value != '') {
            if (regEx.test(obj.value)) {
                obj_msg.style.color = '#06cc3e';
                obj_msg.innerHTML = "<i class='fas fa-check-circle'></i>";
                
            } else {

                obj_msg.style.display = 'inline-block';
                obj_msg.style.color = '#c81523';
                obj_msg.innerHTML = obj_error;
                
            }
        }
        else {
            obj_msg.style.display = 'none';
        }
    }

    



   



    var check_comfirm = function () {
        if (comf_pw.value != '') {
            if (password.value == comf_pw.value) {
                comf_msg.style.color = '#06cc3e';
                comf_msg.innerHTML = "<i class='fas fa-check-circle'></i>Password matching";
                return true;
                
            } else {

                comf_msg.style.display = 'inline-block';
                comf_msg.style.color = '#c81523';
                comf_msg.innerHTML = "<i class='fas fa-times-circle'></i>Both pass word aren't match";
                return false;
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
               // flag=1;
            }else{
                eyes.className = "fas fa-eye-slash";
                obj.type = 'password';
                //flag = 0;
            }
        }

    

    eye.onclick= function () { 
        eyeOpen(password,eye);
    };

     eye2.addEventListener('click', function () { 
        eyeOpen(comf_pw,eye2);
     });
    
    
     password.addEventListener('keyup', function () { 
         var pv = password.value;
         if (pv != '') {
             if (pv.length >= 6) {
                safe.style.display = 'inline-block';
                password_msg.style.color = '#06cc3e';
                password_msg.innerHTML = "<i class='fas fa-check-circle'></i>";
               
                Weak.style.display = 'inline-block';
                  
                if (mid_level.test(pv)) {
                    middle.style.display = 'inline-block';
                } else {  middle.style.display = 'none';}
                if (strong_level.test(pv)) {
                    Strong.style.display = 'inline-block';
                } else { Strong.style.display='none'}
            } else {

                password_msg.style.display = 'inline-block';
                password_msg.style.color = '#c81523';
                password_msg.innerHTML = password_error;
                 safe.style.display = 'none';
                 Weak.style.display = 'none';
                middle.style.display = 'none';
                 Strong.style.display = 'none';
            }
        }
        else {
             password_msg.style.display = 'none';
             safe.style.display = 'none';
             Weak.style.display = 'none';
             middle.style.display = 'none';
             Strong.style.display = 'none';
        }
     });
    
    email.addEventListener('keyup', function () { 
        check(email,email_msg,email_error,regEx_Email);
    });

    username.addEventListener('keyup', function () { 
        check(username,username_msg,username_error,regEx_Uname);
    });

    password.addEventListener('keyup', function () { 
        check_comfirm();
    });
    comf_pw.addEventListener('keyup', function () { 
        check_comfirm();
    });

 document.querySelector('.submit').onclick = function() {
		var input_username = username.value;
        var input_password = password.value;
        var input_email = email.value;
     if (check_comfirm()) {
         var xhr = new XMLHttpRequest();
         xhr.open("POST", "/register");
         xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
         xhr.send("email=" + input_email + "&userName=" + input_username + "&passWord=" + md5(input_password));
         xhr.onreadystatechange = function () {
             if (xhr.readyState == 4 && xhr.status == 200) {
                var res = JSON.parse(xhr.responseText);
                if(res.status == 'success'){
                    alert("registration success!");
                    // Should be check it 'res.redirctUrl' exist first.
                    window.location.href = res.redirctUrl;
                }
                else {
                    alert("registration not success!");
                }
             }
         }
     }
     return false;
    }
    
})



                 
