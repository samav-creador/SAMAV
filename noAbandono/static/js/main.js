$(document).ready(function(){
	$('.submenu li:has(ul)').click(function(e){
		e.preventDefault();

		if ($(this).hasClass('activado')) {
			$(this).removeClass('activado');
			$(this).children('ul').slideUp();
		}else{
			$('.submenu li ul').slideUp();
			$('.submenu li').removeClass('activado');
			$(this).addClass('activado');
			$(this).children('ul').slideDown();
		}
	});
	$('.submenu li ul li a').click(function(){
		window.location.href= $(this).attr("href");
	});
});