dashboard = {
    topics_donut: function() {
        $.ajax({
                method: 'GET',
                url: '/dashboard/topics_articles_count'
        }).done(function(data) {
        Morris.Donut({
                element: 'topics-donut',
                data: data
            });
        });
    },
    factors_donut: function() {
        $.ajax({
                method: 'GET',
                url: '/dashboard/factors_count'
        }).done(function(data) {
        Morris.Donut({
                element: 'factors-donut',
                data: data
            });
        });
    }
};

$(document).ready(function() {
    console.log('ready');
    $('#introduction-row').hide();
    dashboard.topics_donut();
    dashboard.factors_donut();
});
