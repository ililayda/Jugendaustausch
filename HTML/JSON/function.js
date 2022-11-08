function check() {
    if(document.getElementById('inputpassword').value ===
            document.getElementById('confirmpassword').value) {
        document.getElementById('message').innerHTML = "match";
    } else {
        document.getElementById('message').innerHTML = "no match";
    }
}
