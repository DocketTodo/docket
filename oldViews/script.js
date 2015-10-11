$(document).ready(function(){
	console.log('ready');
	var centerPx = $(window).width()/2;
	$('#signIn').css('left',centerPx-101.5);
	$('#signUp').css('left',centerPx+1.5);
	$('.buttons').mouseenter(function(){
		$(this).animate({opacity:'0.6'}, 200);
	});
	$('.buttons').mouseleave(function(){
		$(this).animate({opacity:'0.8'}, 200);
	});
	$('#signIn').click(function(){
		console.log('click');
		$("#loginStuff").animate('opacity','1');
	});
});