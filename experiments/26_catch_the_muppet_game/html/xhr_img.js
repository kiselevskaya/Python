

function update_content() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $css("style.css");
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

            setTimeout(function(){
                update_content();
            }, 5000);
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhr.open("GET", "/get_muppet");
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
    let muppet = document.getElementById("muppet");
    muppet.src = jsonObj['muppet'];

    muppet.style.left = jsonObj['x'];
    muppet.style.top = jsonObj['y'];
    muppet.appendChild(muppet);
}


(function() {
  let loadedFiles = {};
  this.$css = function(filename) {
    if (loadedFiles[filename]) {
      return;
    }
    loadedFiles[filename] = true;
    let xhr = new XMLHttpRequest();
    xhr.open("GET", filename, true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        let head = document.getElementsByTagName("head")[0];
        let styleTag = document.createElement("style");
        let style = document.createTextNode(xhr.responseText);
        styleTag.appendChild(style);
        head.appendChild(styleTag);
      }
    };
    xhr.send(null);
  };
})();
