var wrapper = $( "#button-wrapper" );

$( ".submit" ).click(function() {
      if(wrapper.not( ".checked" )) {
            wrapper.addClass( "checked" );
            setTimeout(function(){
                wrapper.removeClass( "checked" );
            }, 8000);
       }
});

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
  // Update select options
  const titleSelect = document.getElementById('title');
  const yearSelect = document.getElementById('year');
  titleSelect.selectedIndex = slideIndex - 1;
  yearSelect.selectedIndex = slideIndex - 1;
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
  // Update select options
  const titleSelect = document.getElementById('title');
  const yearSelect = document.getElementById('year');
  titleSelect.selectedIndex = slideIndex - 1;
  yearSelect.selectedIndex = slideIndex - 1;
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides fade");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";

  // Update select options
  const titleSelect = document.getElementById('title');
  const yearSelect = document.getElementById('year');
  titleSelect.selectedIndex = slideIndex - 1;
  yearSelect.selectedIndex = slideIndex - 1;
}
