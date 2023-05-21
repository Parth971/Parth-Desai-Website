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
      });
  });