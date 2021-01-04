
var sprice = parseInt($('#sprice').val());
var dprice = parseInt($('#dprice').val());

var tprice = sprice + dprice;

$('#tprice').val(tprice);
$('#total').val(tprice);