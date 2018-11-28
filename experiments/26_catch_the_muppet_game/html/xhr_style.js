

function update_content() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            addStyle();
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/style.css");
    xhr.send();
}


function addStyle() {
    let style = document.createElement('style');
    style.type = 'text/css';
    style.rel = 'stylesheet';
    style.href = "/style.css"
    document.getElementsByTagName('head')[0].appendChild(style);
}
