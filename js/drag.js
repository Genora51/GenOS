function drg(elem){
    $(elem).draggable({
        'stack' : '.windows .window',
        'handle' : '.window-head',
        'iframeFix' : true,
        'containment' : '.windows'
    });
    $(elem).resizable({
        'minHeight' : 50,
        'minWidth' : 105,
        'iframeFix' : true,
        'containment' : '.windows',
        start:function(event,ui){
            $("iframe").each(function() {
                $('<div class="ui-resizable-iframeFix" style="background: #fff;"></div>')
                .css({
                    width: this.offsetWidth+"px", height: this.offsetHeight+"px",
                    position: "absolute", opacity: "0.001", zIndex: 1000
                })
                .css($(this).offset())
                .appendTo("body");
            });
        },
        stop: function(event,ui){
            $("div.ui-resizable-iframeFix").each(function() { this.parentNode.removeChild(this); }); //Remove frame helpers
        }
    }); 
}

// $(".windows").on("DOMNodeInserted", ".window", function() { drg(this); });
$(function(){
    drg('.window');
    $('.desktop .shortcut').draggable({
        'stack' : '.desktop .shortcut',
        'containment' : '.desktop',
        'opacity' : 0.7,
        'grid' : [$('.shortcut').outerWidth(true), $('.shortcut').outerHeight(true)]
    });
});