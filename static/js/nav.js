$(document).ready(function () {
    let navItem = $('.nav-item .nav-link');
    console.log(navItem);
    navItem.on('click', (event) => {
        let target = $(event.currentTarget);
        
        for (let i=0; i < navItem.length; i++) {
            $(navItem[i]).removeClass('active');
        }

        target.addClass('active');
    })
});