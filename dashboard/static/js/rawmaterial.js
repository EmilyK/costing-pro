$(document).ready(function(){
 
    $('.add-more').on('click', function(ev){
      var prevP = $('#materials-template').html()
       $(this).before(prevP);
      return false;
    });
  });
