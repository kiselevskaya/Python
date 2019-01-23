
class Game {
    constructor(status_id) {
        this.status_div = document.getElementById(status_id);

        this.user_list_div = document.createElement("div");
        this.user_list_div.id = "user_list";

        this.status_div.appendChild(this.user_list_div);

        var btn = document.createElement("button");
        btn.appendChild(document.createTextNode("Start Game"));

        this.status_div.appendChild(document.createElement("hr"));
        this.status_div.appendChild(btn);
        this.status_div.appendChild(document.createElement("hr"));
    }

    setWebsocketConnection(wsc) {
        this.wsc = wsc;
    }

    onWebsocketMessage(json_msg) {
        try {
            let msg = JSON.parse(json_msg);
            if (msg["msg"] == "user_list") {
                this.process_user_list(msg);
            }
        } catch(e) {
            console.log(e);
            this.wsc.close();
        }
    }

    onWebsocketError(event) {
        this.status_div.innerHTML = "Websocket error: " + event;
    }

    onWebsocketClose(event) {
        this.status_div.innerHTML = "Websocket closed: " + event;
    }

    //

    process_user_list(msg) {
        let user_list = msg["user_list"];
        let str = "";
        for (let i = 0; i < user_list.length; i++) {
            str += user_list[i] + "<br/>";
        }
        this.user_list_div.innerHTML = str;
    }
}
