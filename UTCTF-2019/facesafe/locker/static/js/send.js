$(document).ready(function(){
  $("#image-upload").change(function () {
      console.log("Sending image over...");
      // Read the input image
      var reader = new FileReader();
      reader.readAsDataURL(document.querySelector('#image-upload').files[0]);
      reader.onload = function() {
          var b64 = reader.result;
          // Send it over to the server
          var fd = new FormData();
          fd.append('image', document.querySelector('#image-upload').files[0]);
          $.ajax({
            url: '/api/check',
            data: fd,
            type: 'POST',
            processData: false,
            contentType: false,
            success: function(result) {
              result = JSON.parse(result);
              console.log(result);
              $("#greeting").html("FaceSafe identified you as " + result["user"] + ". Welcome, " + result["user"] + "!");
              $("#secret").html(result["secret"]);
              $("#authenticated-secret").css("visibility", "visible");
            }
          });
      }
  });
});