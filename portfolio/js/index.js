const scroll_navigation=document.querySelector('nav');
const navigation=document.querySelector('.top-nav');

if (document.body.scrollTop >80 || document.documentElement.scrollTop>80){
    scroll_navigation.style.display = "flex";
    navigation.style.display="none";
}