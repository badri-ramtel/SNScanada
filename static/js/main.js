// Animate On Scroll js
AOS.init();


// $(".exts").ddslick({
//   width:"100%",
//   imagePosition:"left",
// });


//Subcribe JS Start
$(document).ready(function() {
  $('#subscriptionForm').on('submit', function(e) {
      e.preventDefault();  // Prevent default form submission
      
      // Serialize form data
      var formData = $(this).serialize();

      //console.log(formData);
      
      // Send Ajax POST request
      $.ajax({
          type: 'POST',
          url: 'http://127.0.0.1:8000/subscribe/',
          //url: url,
          data: formData,
          success: function(response) {
              if (response.success) {
                  alert('Subscription successful!!!');
                  // Clear form fields if needed
                  $('#subscriptionForm')[0].reset();
              } else {
                  alert('Subscription failed: ' + response.errors);
              }
          },
          error: function(xhr, status, error) {
              alert('Subscription failed: ' + error);
          }
      });
  });
});