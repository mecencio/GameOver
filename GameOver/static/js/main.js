$(document).ready(function(){
    $('.owl-carousel').owlCarousel({
        loop:true,
        margin:10,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    });

    const spinner = document.getElementById("spinner1")
    const content = document.getElementById("content1")

    $.ajax({
        type:'GET',
        url: '/',
        success: function(res){
        setTimeout(()=>{
            spinner.classList.add('no-display')
            content.classList.remove('no-display')
            },300)
        },
    })
})

