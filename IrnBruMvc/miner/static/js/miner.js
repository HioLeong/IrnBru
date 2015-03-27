var miner = {
    mine: function() {
        $.ajax({
                type: 'POST',
                url: '/miner/mine/',
                data: $('#miner-form').serialize(),
                beforeSend: function() {
                    $('#loading').show();
                },
                success: function(data) {
                    $('#loading').hide();
                }
        });
    }
};

$(document).ready(function () {
    $('#loading').hide();
    $('#mine-button').on('click', function(e) {
        e.preventDefault();
        miner.mine();
        return false;
    });
});
