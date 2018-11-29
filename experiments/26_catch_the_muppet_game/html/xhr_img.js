

//  When click on START button
function start() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let muppet = JSON.parse(xhr.response);
            //  Return certain image of muppet in a right position
            parseMuppet(muppet);
            //
            update_score()
            update_level()
            //  Return time in sec of all missed shots
            update_logs()
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/get_muppet");
//    xhr.open("GET", "/get_logs");
    xhr.send();
}


function parseMuppet(jsonObj) {
    let img = document.getElementById("muppet");
    img.src = jsonObj['muppet'];
//    img.style.width = 70+'px';
//    img.style.height = 70+'px';
    img.style.left = jsonObj['x']+'px';
    img.style.top = jsonObj['y']+'px';
}


function update_score() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let score = JSON.parse(xhr.response);
            parseScore(score);
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/get_score");
    xhr.send();
}


function parseScore(jsonObj) {
    let caught = document.getElementById("score");
    caught.innerHTML = jsonObj['caught'];

    let missed = document.getElementById("missed");
    missed.innerHTML = jsonObj['missed'];
}


function update_level() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let muppet = JSON.parse(xhr.response);
            parseLevel(muppet);
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/get_level");
    xhr.send();
}


function parseLevel(jsonObj){
    let level = document.getElementById("level");
    level.innerHTML = jsonObj['level'];
}


function update_logs() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let muppet = JSON.parse(xhr.response);
            parseLogs(muppet);
            start();
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/get_logs");
    xhr.send();
}


function parseLogs(jsonObj) {
    let logs = document.getElementById("time_log");
    logs.innerHTML = "";

    let myLogs = document.createElement('p');
    myLogs.textContent = jsonObj['logs'];
    logs.appendChild(myLogs);
}
