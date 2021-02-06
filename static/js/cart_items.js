window.addEventListener('load', () => { 
    var item_count = document.querySelector('.count');
    var counter = 0;
    var data = localStorage.getItem('products') ? JSON.parse(localStorage.getItem('products')) : [];
    data.forEach(item => counter += item.amount);
    
    if (counter > 0) {
        item_count.style.display = 'inline-block';
        item_count.innerHTML = counter;
    } else { 
         item_count.style.display = 'none';
         item_count.innerHTML = '';
    }
})