
class WebSocketConnection {
    constructor(username, password, some_object) {
        this.username = username;
        this.password = password;
        this.ws = new WebSocket("ws://127.0.0.1:6789/?username=" + username + "&password=" + password);
        this.debug = false;
        this.some_object = some_object;
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
            this.some_object.onWebsocketMessage(event.data);
        }.bind(this);
        this.ws.onerror = function (event) {
            if (this.debug)
                console.log(event);
            this.some_object.onWebsocketError(event);
        }.bind(this);
        this.ws.onclose = function (event) {
            if (this.debug)
                console.log(event);
            this.some_object.onWebsocketClose(event);
        }.bind(this);
    }

    setSomeObject(some_object) {
        this.some_object = some_object;
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
