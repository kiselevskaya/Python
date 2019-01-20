
class WebSocketConnection {
  constructor(status_id, username, password) {
    this.status_div = document.getElementById(status_id);
    this.username = username;
    this.password = password;
    this.ws = new WebSocket("ws://127.0.0.1:6789/?username=" + username + "&password=" + password);
    this.ws.onopen = function (event) {
        console.log(event);
        this.ws.send(JSON.stringify({"msg":"hello", "username":username}));
    }.bind(this);
    this.ws.onmessage = function (event) {
        console.log(event);
    }
    this.ws.onerror = function (event) {
        console.log(event);
    };
    this.ws.onclose = function (event) {
        console.log(event);
    };
  }
}
