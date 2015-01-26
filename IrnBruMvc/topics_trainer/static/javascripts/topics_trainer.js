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

    updateTopics: function(data) {
        $.ajax({
                type: 'POST', 
                url: 'http://127.0.0.1:8000/topic_trainer/29/',
                data: data
        }).done(function (msg) {
            console.log(msg);
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
        trainer.prevPage();
        break;
    case 38:
        trainer.updateTopics({'topic':'topics'});
        break;
    case 39:
        // Key right.
        console.log('Next page');
        trainer.nextPage();
        break;
    case 40:
        // Key down.
        break;
    };
};
