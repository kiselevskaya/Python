
class WebSocketConnection {
    constructor(username, password, game) {
        this.username = username;
        this.password = password;
        this.ws = new WebSocket("ws://127.0.0.1:6789/?username=" + username + "&password=" + password);
        this.debug = false;
        this.game = game;
        this.ws.onopen = function (event) {
            if (this.debug)
                console.log(event);
            this.send({"msg":"hello", "username": username});
        }.bind(this);
        this.ws.onmessage = function (event) {
            if (this.debug)
                console.log(event);
            if (JSON.parse(event.data)["msg"] != "") {
                console.log(" <- " + event.data);
            }
            this.game.onWebsocketMessage(event.data);
        }.bind(this);
        this.ws.onerror = function (event) {
            if (this.debug)
                console.log(event);
            this.game.onWebsocketError(event);
        }.bind(this);
        this.ws.onclose = function (event) {
            if (this.debug)
                console.log(event);
            this.game.onWebsocketClose(event);
        }.bind(this);
    }

    setGame(game) {
        this.game = game;
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
