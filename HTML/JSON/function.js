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