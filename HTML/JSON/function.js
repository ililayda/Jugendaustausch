function check()
{
  if (document.getElementById('inputpassword').value == document.getElementById('confirmpassword').value)
  {
    document.getElementById('pwmessage').style.color = 'green';
    document.getElementById('pwmessage').innerHTML = 'matching';
  }
  else
  {
    document.getElementById('pwmessage').style.color = 'red';
    document.getElementById('pwmessage').innerHTML = 'not matching';
  }
}

function created()
{
    document.getElementById('created').style.color = 'green';
    document.getElementById('created').innerHTML = 'Admin angelegt';
    document.getElementById('created').style.border = '1px solid green';
}