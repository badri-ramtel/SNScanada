document.querySelectorAll('.nav-link').forEach 
(link => {
    // console.log(link.href, window.location.href)
    if(link.href === window.location.href){
        link.setAttribute('aria-current', 'page')
    }
})


// phone number validation
