var price = parseInt($('#price').text());
var newprice;
$('#pacradio1').prop("checked", true);
$('#totalprice').val(price);
$('#packet').val("1");
$('#pac1').click(function(){
    $('#pacradio1').prop("checked", true);
    $('#pacradio2').prop("checked", false);
    $('#pacradio3').prop("checked", false);
   
    newprice = price * 1;
    $('#packet').val("1");
    $('#price').text(newprice);
    $('#totalprice').val(newprice);
    $('#pacb').remove();
    $('#pacc').remove();

});

$('#pac2').click(function(){
    $('#pacradio1').prop("checked", false);
    $('#pacradio2').prop("checked", true);
    $('#pacradio3').prop("checked", false);
    newprice = price * 3;
    $('#price').text(newprice);
    $('#totalprice').val(newprice);
    $('#packet').val("3");
    $('#paca').remove();
    $('#pacc').remove();

});

$('#pac3').click(function(){
    $('#pacradio1').prop("checked", false);
    $('#pacradio2').prop("checked", false);
    $('#pacradio3').prop("checked", true);
    newprice = price * 5;
    $('#price').text(newprice);
    $('#totalprice').val(newprice);
    $('#packet').val("5");
    $('#paca').remove();
    $('#pacb').remove();
});

