
class WebSocketConnection {
  constructor(username, password, game) {
    this.username = username;
    this.password = password;
    this.ws = new WebSocket("ws://127.0.0.1:6789/?username=" + username + "&password=" + password);
    this.debug = false;
    this.ws.onopen = function (event) {
        if (this.debug)
            console.log(event);
        this.send({"msg":"hello", "username":username});
    }.bind(this);
    this.ws.onmessage = function (event) {
        if (this.debug)
            console.log(event);
        if (JSON.parse(event.data)["msg"] != "tick") {
            console.log(" <- " + event.data);
        }
        game.onWebsocketMessage(event.data);
    }
    this.ws.onerror = function (event) {
        if (this.debug)
            console.log(event);
        game.onWebsocketError(event);
    };
    this.ws.onclose = function (event) {
        if (this.debug)
            console.log(event);
        game.onWebsocketClose(event);
    };
  }

  send(msg) {
    let json_msg = JSON.stringify(msg);
    console.log(" -> " + json_msg);
    this.ws.send(json_msg);
  }

  close() {
    this.ws.close();
  }
}
