$('#inputpassword, #confirmpassword').on('keyup', function ()
    {
    if ($('#inputpassword').val() == $('#confirmpassword').val())
    {
        $('#pwmessage').html('Matching').css('color', 'green');
    }
    else
        $('#pwmessage').html('Not Matching').css('color', 'red');
    }
);
