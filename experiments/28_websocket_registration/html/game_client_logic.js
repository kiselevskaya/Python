
class Game {
    constructor(status_id) {
        this.status_div = document.getElementById(status_id);

        this.user_list_div = document.createElement("div");
        this.user_list_div.id = "user_list";

        this.status_div.appendChild(this.user_list_div);
        this.status_div.appendChild(document.createElement("hr"));


        this.countdown = document.createElement("div");
        this.countdown.id = "countdown";

        this.status_div.appendChild(this.countdown);


        this.btn = document.createElement("button");
        this.btn.onclick = function(){
            this.startGame();
        }.bind(this);
        this.btn.appendChild(document.createTextNode("Start Game"));

        this.status_div.appendChild(this.btn);
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
            if (msg["msg"] == "countdown") {
                this.process_countdown(msg);
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
        this.user_list = user_list;
    }

    startGame() {
        this.wsc.send({"msg": "start_game"});
    }

    process_countdown(msg) {
        this.btn.style.visibility='hidden';

        let countdown = msg["countdown"];
        this.countdown.innerHTML = countdown;
    }
}
