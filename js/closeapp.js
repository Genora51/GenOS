function capp(){
	$('.btn.close').click(function(){
		let app = $(this).parents('.window');
		// CLOSE APP FUNCTIONS

		app.remove();
	});
}

$(capp);