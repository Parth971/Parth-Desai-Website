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



    $('#contact-form').on('submit', function(event){
      event.preventDefault();
      let csrfmiddlewaretoken = $("input[name*='csrfmiddlewaretoken']").val();
      
      console.log("form submitted!");
      
      $.ajax({
        url : "/",
        type : "POST",
        data : { 
          name : $('#contact_name').val(),
          phone : $('#contact_phone').val(),
          email : $('#contact_email').val(),
          message : $('#contact_message').val(),
          csrfmiddlewaretoken: csrfmiddlewaretoken
        },
        success : function(json) {
            $('#contact_name').val('');
            $('#contact_phone').val('');
            $('#contact_email').val('');
            $('#contact_message').val(''); 
            console.log(json);
            console.log("success");
        },

        // handle a non-successful response
        error : function(xhr, errmsg, err) {
            $('#results').html(`<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: ${xhr.responseText} <a onclick="$('#results').html('');" class='close'>&times;</a></div>`); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
      });
  });

  
    
});