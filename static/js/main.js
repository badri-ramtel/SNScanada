document.querySelectorAll('.nav-link').forEach 
(link => {
    // console.log(link.href, window.location.href)
    if(link.href === window.location.href){
        link.setAttribute('aria-current', 'page')
    }
})


// phone number validation
// const toastTrigger = document.getElementById('liveToastBtn')
// const toastLiveExample = document.getElementById('liveToast')

// if (toastTrigger) {
//   const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
//   toastTrigger.addEventListener('click', () => {
//     toastBootstrap.show()
//   })
// }

function myFunction() {
    alert("Thank you for Subscription");
  }
