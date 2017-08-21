function capp(){
	$('.btn.close').click(function(){
		let app = $(this).parents('.window');
		// CLOSE APP FUNCTIONS
        app.find('.con')[0].contentWindow.postMessage({
            'name': 'closeEvent'
        },
        '*');
	});

    $(window).on('message', function(e){
        var event = e.originalEvent;
        // console.log('message')
        $('.window iframe.con').filter(function(){
            return (this.contentWindow === event.source.parent) ||
                   (this.contentWindow === event.source);
        }).parents('.window').remove()
    });
}

$(capp);