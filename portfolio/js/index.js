const navigation_bar=document.querySelector('.scroll-nav-bar');
const nav_links=document.querySelectorAll('.nav-item');

window.onscroll=function(){documentScroll()};
function documentScroll(){
    if(document.body.scrollTop>80 || document.documentElement.scrollTop>80){
        navigation_bar.style.backgroundColor="white";



        for (let i of nav_links){
            i.style.color="rgb(172, 65, 26)";
            i.style.padding="8px";
        }
    }
    else{
        navigation_bar.style.backgroundColor="rgb(172, 65, 26)";
        for (let i of nav_links){
           i.style.color="white";
           i.style.backgroundColor=""
        }
    }
}