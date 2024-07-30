// Internation Telephone JS for contact
var phone_number = window.intlTelInput(document.querySelector("#contact"), {
    separateDialCode: true,
    preferredCountries: ["ca"],
    hiddenInput: "contact",
    utilsScript: "//cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.3/js/utils.js"
});

$("form").submit(function(){
  var full_number = phone_number.getNumber(intlTelInputUtils.numberFormat.E164);
  var dialCode = phone_number.getSelectedCountryData().dialCode;

  // Remove the dial code from the full number
  var numberWithoutDialCode = full_number.replace('+' + dialCode, '');

  // Define the symbol to insert between the dial code and the phone number
  var symbol = '-'; // Change this to any symbol you want

  // Combine dial code, symbol, and phone number
  var formattedNumber = '+' + dialCode + symbol + numberWithoutDialCode;

  $("input[name='contact']").val(formattedNumber);

});


// Internation Telephone JS for parent contact
var phone_numbers = window.intlTelInput(document.querySelector("#pcontact"), {
    separateDialCode: true,
    preferredCountries: ["ca"],
    hiddenInput: "pcontact",
    utilsScript: "//cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.3/js/utils.js"
});

$("form").submit(function(){
  var full_numbers = phone_numbers.getNumber(intlTelInputUtils.numberFormat.E164);
  var dialCode = phone_numbers.getSelectedCountryData().dialCode;

  // Remove the dial code from the full number
  var numberWithoutDialCode = full_numbers.replace('+' + dialCode, '');

  // Define the symbol to insert between the dial code and the phone number
  var symbol = '-'; // Change this to any symbol you want

  // Combine dial code, symbol, and phone number
  var formattedNumber = '+' + dialCode + symbol + numberWithoutDialCode;
 
  $("input[name='pcontact[full]']").val(formattedNumber);
});


// // 
// var dialCode = phone_number.getSelectedCountryData().dialCode;
// var full_number = phone_number.getNumber(intlTelInputUtils.numberFormat.E164);

// // Remove the dial code from the full number
// var numberWithoutDialCode = full_number.replace('+' + dialCode, '');

// // Define the symbol to insert between the dial code and the phone number
// var symbol = '-'; // Change this to any symbol you want

// // Combine dial code, symbol, and phone number
// var formattedNumber = '+' + dialCode + symbol + numberWithoutDialCode;

// console.log(formattedNumber);

// $("input[name='contact']").val(formattedNumber);

// console.log($("input[name='contact']").val(formattedNumber));

// this.submit();