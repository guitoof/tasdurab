
function getCookie(c_name) {
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 };

 function displayError(message){
   var errorHTML = '<div class="alert alert-danger alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>';
   errorHTML = errorHTML + message;
   errorHTML = errorHTML + '</div>';
   return errorHTML;
 }

$(function(){

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    $('#submit-product-create').click(function(e){
        e.preventDefault();
        var form = $('#create-product-form');
        var url = form.attr('action');
        var data = form.serializeArray();
        $.post( url, data, function( response ) {
          $('#createProductModal').modal('hide');
          window.location.reload();
        }).fail(function(error){
          // Display the form errors to the user
          alert(error.responseText);
          var errors = JSON.parse(error.responseText);
          $.each(errors, function(key, value){
            $('#input-' + key).before(displayError(value));
          })

        });
    });

});
