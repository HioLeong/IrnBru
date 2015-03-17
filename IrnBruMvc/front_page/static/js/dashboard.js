$(document).ready(function() {
    console.log('ready');
    $.ajax({
            method: 'GET',
            url: '/dashboard/topics_articles_count'
    }).done(function(data) {
    console.log(data);
    Morris.Donut({
            element: 'topics-donut',
            data: data
    });
    });
});
