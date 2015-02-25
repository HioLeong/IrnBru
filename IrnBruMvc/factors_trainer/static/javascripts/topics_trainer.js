var trainer = {
    changeArticleIndex: function(url, num) {
        var lastIndex = url.length - 1;
        if (url[lastIndex] === '/') {
            url = url.substring(0, url.length-1)
        }
        
        splitUrl = url.split('/');
        var newPageNum = num + parseInt(splitUrl.pop());
        window.location.href = splitUrl.join('/') + '/' + (newPageNum);
    },
    
    nextPage: function() {
        var url = window.location.href;
        this.changeArticleIndex(url, 1);
    },
    prevPage: function() {
        var url = window.location.href;
        this.changeArticleIndex(url, -1);
    },

    updateTopics: function() {
        var $form = $('form');
        $form.submit(function(){
            $.post($(this).attr('action'), $(this).serialize(), function(response){
                $("#submission_status").append("Updated");
            },'json');
            return false;
        });
    }
}

document.onkeydown = function(event) {
    if (!event) {
        event = window.event;
    }
    var code = event.keyCode;
    switch(code) {
    case 37:
        // Key left.
        console.log('Previous page');
        $('form').submit();
        trainer.prevPage();
        break;
    case 38:
        break;
    case 39:
        console.log('Next page');
        $('form').submit();
        trainer.nextPage();
        break;
    case 40:
        // Key down.
        break;
    };
};

$(document).ready(function(){
    trainer.updateTopics();
});
