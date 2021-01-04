var height = $('.productbanner').offset();
var oftop = height.top;
$(window).scroll(function(){
    var scrolltop = $(window).scrollTop();
    if(scrolltop > oftop)
    {
        $('.text').css({"transform":"translateY(0px)", "opacity":"1"});
    } 
});


$('#pac1').click(function(){
    $('#pacradio1').prop("checked", true);
    $('#pacradio2').prop("checked", false);
    $('#pacradio3').prop("checked", false);


});

$('#demo').fadeIn();

alert('fck');