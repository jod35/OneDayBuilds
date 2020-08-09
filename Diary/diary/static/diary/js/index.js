const mobileNavOpenButton=document.querySelector('.menu-open-btn');
const mobileNavCloseButton=document.querySelector('.menu-close-btn');
const mobileNav=document.querySelector('.mobile-nav');
const mobileNavItems=document.querySelector('.mobile-nav-items');


mobileNavOpenButton.addEventListener('click',displayMobileMenu);

function displayMobileMenu(){
    mobileNavOpenButton.style.display="none";
    mobileNavCloseButton.style.display="block";
    mobileNav.style.display="block";
    mobileNavItems.style.display="block";
    mobileNav.style.width="100vw";
    mobileNav.style.height="60vh";
}

mobileNavCloseButton.addEventListener('click',hideMobileNav);


function hideMobileNav(){
    mobileNavOpenButton.style.display="block";
    mobileNavCloseButton.style.display="none";
    mobileNav.style.height="0vh";
    mobileNavItems.style.display="none";
}