
class Countdown {
    constructor(status_id, username, password, new_game_users) {
        this.status_div = document.getElementById(status_id);

        this.user_list_div = document.createElement("div");
        this.user_list_div.id = "user_list";

        this.last_user_list = new_game_users;

        this.status_div.appendChild(this.user_list_div);
        this.status_div.appendChild(document.createElement("hr"));

        this.countdown = document.createElement("div");
        this.countdown.id = "countdown";
        this.status_div.appendChild(this.countdown);

        this.add_start_button();
    }

    setWebsocketConnection(wsc) {
        this.wsc = wsc;
    }

    onWebsocketMessage(json_msg) {
        try {
            let msg = JSON.parse(json_msg);
            if (msg["msg"] == "user_list") {
                this.process_user_list(msg);
            } else if (msg['msg'] == "start_game") {
                this.started = true;
            } else if (msg["msg"] == "countdown") {
                this.process_countdown(msg);
            } else if (msg["msg"] == "cannot_start_game") {
                this.wsc.close();
            } else {
                console.log("unknown message: ", json_msg);
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

    process_user_list(msg) {
        let user_list = msg["user_list"];
        this.last_user_list = user_list;
        let str = "";
        for (let i = 0; i < user_list.length; i++) {
            str += user_list[i] + "<br/>";
        }
        this.user_list_div.innerHTML = str;
        this.user_list = user_list;
    }

    add_start_button() {
        if (!this.started) {
            this.div_btn = document.createElement("div");
            this.btn = document.createElement("button");
            this.btn.onclick = function(){
                this.startGame();
            }.bind(this);
            this.btn.appendChild(document.createTextNode("Start Game"));
            this.div_btn.appendChild(this.btn)

            this.status_div.appendChild(this.div_btn);
        }
    }

    startGame() {
        this.wsc.send({"msg": "start_game"});
    }

    process_countdown(msg) {
        this.clear_div(this.div_btn);

        let seconds = msg["countdown"];
        var minutes = Math.floor(seconds / 60);
        seconds = seconds - minutes * 60;

        function str_pad_left(string,pad,length) {
            return (new Array(length+1).join(pad)+string).slice(-length);
        }

        var finalTime = str_pad_left(minutes,'0',2)+':'+str_pad_left(seconds,'0',2);
        this.countdown.innerHTML = finalTime;

        if (msg['started']) {
            this.process_start_game();
        }
    }

    process_start_game() {
        this.clear_div(this.status_div);
        this.create_game_field();
    }

    create_game_field() {
        console.log("check user list_", this.last_user_list);
        this.game = new Game("data", params.get("username"), this.last_user_list);
        this.wsc.setGame(this.game);
        this.game.setWebsocketConnection(this.wsc);
    }

    clear_div(div){
        while (div.firstChild) {
            div.removeChild(div.firstChild);
        }
    }

}
