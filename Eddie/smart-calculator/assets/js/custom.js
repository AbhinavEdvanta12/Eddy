$(document).ready(function(){
	$('.mob-menu').click(function(){
		$(this).toggleClass('active-menu');
		$('.navigation').slideToggle();
		$('.from-wrap').slideUp();
	});
	// Accordion Start
	$('.footer-menu h5').click(function(){
		if($(window).width() < 768 ){
			$('.footer-menu ul').slideUp();
			$(this).next('ul').slideDown();
		}
	});
});