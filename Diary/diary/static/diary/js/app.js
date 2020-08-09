const event_creation_form=document.querySelector('.addform');
const event_display_form=document.querySelector('#view-events');
const event_form_button=document.querySelector('#show-form');
const event_display_button=document.querySelector('#show-events');



event_form_button.addEventListener('click',displayForm);

function displayForm(){
    event_creation_form.style.display="block";
    console.log("hello");
   
}