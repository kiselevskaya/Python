

function update_log() {
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let log = document.getElementById("log");
            log.innerHTML = xmlhttp.responseText;

            setTimeout(function(){
                update_content();
            }, 5000);
        }
    }
    xmlhttp.open("GET", "/zoo_shop_logs");
    xmlhttp.send();
}


function update_content() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let content = document.getElementById("content");
            content.innerHTML = xhttp.responseText;
            update_log();
        }
    }
    xhttp.open("GET", "/zoo_shop_state");
    xhttp.send();
}
