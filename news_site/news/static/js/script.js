window.onscroll = function() {scrollFunction()};

let warningModal = new bootstrap.Modal(document.getElementById('warningModal'), {
  keyboard: false
});
let cancelModal = new bootstrap.Modal(document.getElementById('cancelModal'), {
  keyboard: false
});
let failModal = new bootstrap.Modal(document.getElementById('failModal'), {
  keyboard: false
});

const validateEmail = (email) => {
  const emailPattern = /\S+@\S+\.\S+/;
  return emailPattern.test(email);
};

$(".send-button").on("click", function(){
  if(validateEmail($("#newsletter").val())){
    warningModal.show();
    $("#cancel").on("click", function(){
      warningModal.hide();
      cancelModal.show();
      $("#confirm").on("click", function(){
        cancelModal.hide();
      });
    });
  }else{ 
    failModal.show();
    $("#confirm-fail").on("click", function(){
      failModal.hide();
      $("#newsletter").focus();
    });
  }
});

function scrollFunction() {
  if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
    $(".navbar").addClass("bg-light");
    $(".navbar-brand").css("color", "rgb(177, 26, 26)").css("font-size", 35 + "px");
    $(".nav-link").css("opacity", 100 + "%");
} else {
    $(".navbar").removeClass("bg-light");
    $(".navbar-brand").css("color", "#fff").css("font-size", 60 + "px");
    $(".nav-link").css("opacity", 0 + "%");
  }
}

$(document).ready(function() {
    $("#notice-carousel").lightSlider({
        loop: true,
        item: 4,
        auto: true,
        pauseOnHover: true,
        slideMargin: 10,
        speed: 1000,
        pause: 5000,
        pager: false,
        adaptiveHeight: true,
    });
});

$(document).ready(function() {
  $("#comments-carousel").lightSlider({
    loop: true,
    item: 4,
    auto: true,
    pauseOnHover: true,
    slideMargin: 10,
    speed: 1000,
    pause: 5000,
    controls: false,
    pager: false,
    adaptiveHeight: true,
});
});

$('.scroll-to').on('click', function(event){
  event.preventDefault();
  let section  = $(this).attr('href');
  let top = $(section).offset().top - 78;
  $('html').animate({
    scrollTop: top
  }, 500)
});