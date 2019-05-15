$(document).ready(()=>{
    $('.carousel').hover('pause', ()=>{
        console.log("Paused");
    });
    
    $('.carousel').on('slide.bs.carousel',()=>{
        console.log("Slide");
        $('.carousel').carousel('.next').hide();
        $('.carousel').carousel('.prev').fadeOut();
        
    });
    $('.carousel').on('slid.bs.carousel', ()=>{
        console.log("Slid");
        $('.carousel').carousel('.next').fadeIn();
        $('.carousel').carousel('.prev').hide();
    })
});

function openModal(){
    document.getElementById("the_modal").style.display = "block";
}
function closeModal(){
    document.getElementById("the_modal").style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
     showSlides(slideIndex += n);
}

function currentSlide(n){
    showSlides(slideIndex = n);
}

function showSlides(n){
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("modal-image");
    var captionText = document.getElementById("caption");
    if(n > slides.length) {slideIndex = 1}
    if(n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++){
        slides[i].style.display = "none";
    }
    for(i = 0; i < dots.length; i++){
        dots[i].className = dots[i].className.replace(" modal-active", "");
    }
    slides[slideIndex-1].style.display="flex";
    slides[slideIndex-1].style.justifyContent="center";
    dots[slideIndex-1].className += " modal-active";
    captionText.innerHTML = dots[slideIndex-1].alt;
}