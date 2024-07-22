// Internation Telephone JS for contact
var phone_number = window.intlTelInput(document.querySelector("#contact"), {
    separateDialCode: true,
    preferredCountries: ["ca"],
    hiddenInput: "contact",
    utilsScript: "//cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.3/js/utils.js"
});

$("form").submit(function(){
  var full_number = phone_number.getNumber(intlTelInputUtils.numberFormat.E164);
  $("input[name='phone_number[full]']").val(full_number);
});


// Internation Telephone JS for parent contact
var phone_number = window.intlTelInput(document.querySelector("#pcontact"), {
    separateDialCode: true,
    preferredCountries: ["ca"],
    hiddenInput: "pcontact",
    utilsScript: "//cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.3/js/utils.js"
});

$("form").submit(function(){
  var full_number = phone_number.getNumber(intlTelInputUtils.numberFormat.E164);
  $("input[name='phone_number[full]']").val(full_number);
});