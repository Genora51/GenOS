function strt(){
    date_time('date');
    $('.desktop').mousedown(function(){
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
    $('.grow').click(function(){
        let $w = $(this).parents('.window');
        let bw = parseInt($w.css('border-left-width'), 10) * 2;
        let bh = parseInt($w.css('border-top-width'), 10) * 2;
        $w.css({
            top: 0,
            left: 0,
            bottom: 0,
            width: ($('.windows').width() - bw) + 'px',
            height: ($('.windows').height() - bh) + 'px'
        });
    });
}

function date_time(id)
{
        date = new Date;
        datestring = $('.status').css('content').slice(1,-1);
        result = date.strftime(datestring);
        document.getElementById(id).innerHTML = result;
        setTimeout('date_time("'+id+'");','1000');
        return true;
}

$(strt);