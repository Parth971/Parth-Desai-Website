$(function() {
    $('#fancy_I_wrapper ul li').hover(function() {
      $('#letter_I').css('border-top', '6px solid black');
      $('#letter_I').css('border-bottom', '6px solid black');
      $('#letter_I .line').css('border', '3px solid black');

      },
      function() {
        $('#letter_I').css('border-top', '6px solid rgba(49, 49, 49, 0.664)');
        $('#letter_I').css('border-bottom', '6px solid rgba(49, 49, 49, 0.664)');
        $('#letter_I .line').css('border', '3px solid rgba(49, 49, 49, 0.664)');
      }
    );
    
    let hash = window.location.hash;
    if (hash != ""){
      let navItem = $('.nav-item .nav-link');
      for (let i=0; i < navItem.length; i++) {
          $(navItem[i]).removeClass('active');
      }
      if (hash === "#contact"){
        $($('.nav-link')[4]).addClass('active');
      }
      else if (hash === "#about"){
        $($('.nav-link')[1]).addClass('active');
      }
    }
    else {
      $($('.nav-link')[0]).addClass('active');
    }
    
});