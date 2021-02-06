window.addEventListener('load', () => { 

    var show_id = document.querySelector('.show_id');
    var logout = document.querySelector('.logout');
    var log = document.querySelector('.log');


    
    if (localStorage.getItem('user')) {
        show_id.innerHTML = 'Hi! '+localStorage.getItem('user');
        log.style.display = 'none';
        logout.style.display = 'inline-block';
    } 


    logout.addEventListener('click', () => { 
         
        localStorage.removeItem('user');
        show_id.innerHTML = 'Welcome!&nbsp; &nbsp;'
        logout.style.display = 'none';
        log.style.display = 'inline-block';
    })
})