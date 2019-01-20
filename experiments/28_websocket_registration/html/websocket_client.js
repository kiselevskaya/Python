
class WebSocketConnection {
  constructor(status_id, username, password) {
    this.status_div = document.getElementById(status_id);
    this.username = username;
    this.password = password;

  }
}

//var // log = document.querySelector('.log'),
    // value = document.querySelector('.username'),
//    var register = document.querySelector('.register');
//    // ws = new WebSocket("ws://127.0.0.1:6789/");
//
//register.onclick = function (event) {
//    log.console(register);
//  //  ws.send(JSON.stringify({action: 'register'}));
//};
//ws.onmessage = function (event) {
//        value.innerHTML = document.createTextNode(event.data);
//};

function register(form) {
    console.log("ololol " + form.elements["username"].value);
}
