
// burger-logo, main-ul and .active-nav-mobile classes are defined in the css file


const mobileNav = () => {
    const getBurger = document.querySelector(".burger-logo") // get the burger-logo class from the css file
    // console.log(getBurger);
    const navlinks = document.querySelector(".main-ul"); // get the main-ul class from the css file
    // console.log(navlinks);


    // The below code makes the class .active-nav-mobile to be visible on the mobile screen
    getBurger.addEventListener('click', () => {
        navlinks.classList.toggle('activate-nav-mobile');
        getBurger.classList.toggle('cross');
    })
}

mobileNav();
