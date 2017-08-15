function strt(){
	$('.windows').click(function(){
		$('.selectedWin').removeClass('selectedWin');
	})
	$('.windows').on('mousedown', '.window', function(){
		$('.selectedWin').removeClass('selectedWin');
		$(this).addClass('selectedWin');
	});
	$('.windows').on('click', '.window', function(e){
		e.stopPropagation();
	});
	window.addEventListener('blur',function(){
      	if(document.activeElement.className == 'con'){
        	$('.selectedWin').removeClass('selectedWin');
			$(document.activeElement).parents('.window').addClass('selectedWin');
      	}
	});
	$('.shrink').click(function(){
		$(this).parents('.window').addClass('animated zoomOutDown');
	});
}

$(strt);