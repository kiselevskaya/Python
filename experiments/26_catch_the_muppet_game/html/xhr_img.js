

//  I. Start button (reset game)
function update_start() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let start = JSON.parse(xhr.response);
            if (start["start"]){
                update_muppet();
            }
            update_level();
            update_logs();
            parseScore(start);
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/get_start");
    xhr.send();
}


//  II. Follows muppet position
function update_muppet() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let muppet = JSON.parse(xhr.response);
            parseMuppet(muppet);
            update_muppet();
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/get_muppet");
    xhr.send();
}


function parseMuppet(jsonObj) {
    let img = document.getElementById("muppet");
    img.src = jsonObj["muppet"];
//    img.style.width = 70+'px';
//    img.style.height = 70+'px';
    img.style.left = jsonObj["x"]+"px";
    img.style.top = jsonObj["y"]+"px";
}


//  III. Update score and call level and logs updates
function update_score(event) {
    let xhr = new XMLHttpRequest();
    let muppet = document.getElementById("muppet")
    let aim = event.target;
    if (aim === muppet){
        xhr.open("GET", "/get_caught");
    } else {
        xhr.open("GET", "/get_missed");
    }
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let score = JSON.parse(xhr.response);
            parseScore(score);
            update_level();
            update_logs();
            update_end();
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.send();
}


function parseScore(jsonObj) {
    let caught = document.getElementById("score");
    caught.innerHTML = jsonObj["caught"];

    let missed = document.getElementById("missed");
    missed.innerHTML = jsonObj["missed"];
}


//  IV. Updates level if necessary
function update_level() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let level = JSON.parse(xhr.response);
            parseLevel(level);
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/get_level");
    xhr.send();
}


function parseLevel(jsonObj){
    let newLevel = document.getElementById("level");
    newLevel.innerHTML = "LEVEL " + jsonObj["level"];
}


//  V. Update logs changes if necessary
function update_logs() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let muppet = JSON.parse(xhr.response);
            parseLogs(muppet);
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

    let myLogs = document.createElement("p");
    myLogs.textContent = jsonObj["logs"];
    myLogs.innerHTML = myLogs.innerHTML.replace(/,/g, "<br />")
    logs.appendChild(myLogs);
}
