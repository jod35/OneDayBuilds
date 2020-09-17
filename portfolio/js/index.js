const navigation_bar = document.querySelector(".scroll-nav-bar");
const nav_links = document.querySelectorAll(".nav-item");
const nav_open_button = document.querySelector(".open-btn");
const mobile_nav_bar = document.querySelector(".mobile-links");
const mobile_nav_links = document.querySelector(".mob-nav-item");

window.onscroll = function () {
  documentScroll();
};
function documentScroll() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    navigation_bar.style.backgroundColor = "white";
    nav_open_button.style.color = "black";

    for (let i of nav_links) {
      i.style.color = "black";
      i.style.padding = "20px";
    }
  } else {
    navigation_bar.style.backgroundColor = "dodgerblue";
    nav_open_button.style.color = "white";
    for (let i of nav_links) {
      i.style.color = "white";
      //    i.style.backgroundColor="dodgerblue";
    }
  }
}

const footer = document.querySelector(".footer-section");
const year = document.querySelector(".year");

const date = new Date();

const this_year = date.getFullYear();

year.innerHTML = this_year;

nav_open_button.addEventListener("click", openMobileNav);

function openMobileNav() {
  if (mobile_nav_bar.style.display == "none") {
    mobile_nav_bar.style.display = "block";

    for (let i of mobile_nav_links) {
      i.style.display = "block";
    }
  } else {
    mobile_nav_bar.style.display = "none";
  }
}
