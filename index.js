var mobileNav = () => {
    var getBurger = document.querySelector(".burger-logo");
    // console.log(getBurger);
    var navlinks = document.querySelector(".main-ul");
    // console.log(navlinks);
    getBurger.addEventListener('click', () => {
        navlinks.classList.toggle('activate-nav-mobile');
        getBurger.classList.toggle('cross');
    })
}

mobileNav();