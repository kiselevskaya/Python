

function start() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let muppet = JSON.parse(xhr.response);
            parseLogs(muppet);
            update_pos()
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/get_position");
    xhr.send();
}

function update_pos(){
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let muppet = JSON.parse(xhr.response);
            parseMuppet(muppet);
            start();
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/get_position");
    xhr.send();
}


function parseLogs(jsonObj) {
    let logs = document.getElementById("time_pos_log");
    logs.innerHTML = "";

    let myTime = document.createElement('p');
    myTime.textContent = jsonObj['time'];
    logs.appendChild(myTime);

    let myMuppet = document.createElement('p');
    myMuppet.textContent = jsonObj['pos'];
    logs.appendChild(myMuppet);
}

function parseMuppet(jsonObj) {
    let img = document.getElementById("muppet");
    img.src = jsonObj['muppet'];

    img.style.left = jsonObj['x']+'px';
    img.style.top = jsonObj['y']+'px';
}
