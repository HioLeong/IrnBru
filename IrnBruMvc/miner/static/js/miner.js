var miner = {
    mine: function() {
        $.ajax({
                type: 'POST',
                url: '/miner/mine/',
                data: $('#miner-form').serialize(),
                success: function(data) {
                    console.log(data);
                }
        });
    }
};

$(document).ready(function () {
    $('#mine-button').on('click', function(e) {
        e.preventDefault();
        miner.mine();
        return false;
    });
});
