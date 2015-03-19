var trainer = {
    updateFactor: function() {
        var $form = $('form');
        $form.submit(function(){
            $.post($(this).attr('action'), $(this).serialize(), function(response){
                $("#submission_status").append("Updated");
            },'json');
            return false;
        });
    }
};

$(document).ready(function(){
    $('input[type=checkbox]').on('change',function(event) {
        event.preventDefault();
        var form = $(this).closest('form');
        $(form).on('submit',function(event) { 
            event.preventDefault();
            var postData = $(this).serializeArray();
            var formUrl = $(this).attr('action');
            $.ajax(
                {
                    url: formUrl, 
                    type: 'POST',
                    data: postData,
                    success: function(data, textStatus, jqHr) {
                        $(form).closest('tr').hide();
                        console.log(data);
                        return true;
                    },
                    error: function(jqHr, textStatus, errorThrown) {
                        return false;
                    }
                }
            );
        });
        $(form).submit();
        $(form).unbind('submit');
    });
});

