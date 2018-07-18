

function update_log() {
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let logs = JSON.parse(xmlhttp.response);
            parseLogs(logs);

            setTimeout(function(){
                update_content();
            }, 5000);

        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xmlhttp.open("GET", "/zoo_shop_logs");
    xmlhttp.send();
}

function update_content() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        // console.log(this.readyState, this.status);
        if (this.readyState == 4 && this.status == 200) {
            $css("style.css");
            let petShop = JSON.parse(xhttp.response);
            parseTitle(petShop);
            tableAnimals(petShop);
            update_log();
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhttp.open("GET", "/zoo_shop_state");
    xhttp.send();
}


function parseTitle(jsonObj) {
    let content = document.getElementById("content");
    content.innerHTML = "";

    let myH1 = document.createElement('h1');
    myH1.textContent = jsonObj['title'];
    content.appendChild(myH1);

    let myPara = document.createElement('p');
    myPara.textContent = jsonObj['data_time'];
    content.appendChild(myPara);
}

function parseLogs(jsonObj) {
    let log = document.getElementById("log");
    log.innerHTML = "";

    let table = document.createElement('table');
    table.width = "100%";

    let thead = document.createElement('thead');
    table.appendChild(thead);

    let tbody = document.createElement('tbody');
    table.appendChild(tbody);

    let header = document.createElement('tr');

    let localtime = document.createElement('th');
    let logHead = document.createElement('th');

    localtime.appendChild(document.createTextNode('Time'));
    logHead.appendChild(document.createTextNode('Log'));

    header.appendChild(localtime);
    header.appendChild(logHead);

    thead.appendChild(header);

    for (var i = 0; i < jsonObj.length; i++){
        let tr = document.createElement('tr');
        let localtimeCell = document.createElement('td');
        let logCell =  document.createElement('td');

        localtimeCell.appendChild(document.createTextNode(jsonObj[i]['localtime']));
        logCell.appendChild(document.createTextNode(jsonObj[i]['log']));

        tr.appendChild(localtimeCell);
        tr.appendChild(logCell);
        tbody.appendChild(tr);
    }

   log.appendChild(table);
}

(function() {
  var loadedFiles = {};
  this.$css = function(filename) {
    if (loadedFiles[filename]) {
      return;
    }
    loadedFiles[filename] = true;
    var xhr = new XMLHttpRequest();
    xhr.open("GET", filename, true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        var head = document.getElementsByTagName("head")[0];
        var styleTag = document.createElement("style");
        var style = document.createTextNode(xhr.responseText);
        styleTag.appendChild(style);
        head.appendChild(styleTag);
      }
    };
    xhr.send(null);
  };
})();
