

function update_content() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        // console.log(this.readyState, this.status);
        if (this.readyState == 4 && this.status == 200) {
            $css("style.css");
            let muppet = JSON.parse(xhttp.response);
            parseLogs(muppet);

            setTimeout(function(){
                update_content();
            }, 5000);
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhttp.open("GET", "/get_position");
    xhttp.send();
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












//function update_content() {
//    var xhr = new XMLHttpRequest();
//
//    // Hack to pass bytes through unprocessed.
//    xhr.overrideMimeType('text/plain; charset=x-user-defined');
//
//    xhr.onreadystatechange = function(e) {
//        if (this.readyState == 4 && this.status == 200) {
//            var binStr = this.responseText;
//            for (var i = 0, len = binStr.length; i < len; ++i) {
//              var c = binStr.charCodeAt(i);
//              //String.fromCharCode(c & 0xff);
//              var byte = c & 0xff;  // byte at offset i
//            }
//        }
//    };
//
//    xhr.open('GET', 'cookie.png', true);
//    xhr.send();
//}
