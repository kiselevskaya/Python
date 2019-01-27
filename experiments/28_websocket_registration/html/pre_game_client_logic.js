
class PreGame {
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

        this.container = document.createElement("div");
        this.container.setAttribute("id", "container");
        this.img = document.createElement("img");
        this.img.setAttribute("src", "images/cookie.png");
        this.img.setAttribute("id", "muppet")
        this.container.appendChild(this.img);
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
            if (msg['msg'] == "start_game") {
                this.btn.parentNode.removeChild(this.btn);
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
        while (this.status_div.firstChild) {
           this.status_div.removeChild(this.status_div.firstChild);
        }
        this.create_game_field();
    }

    create_game_field() {
          this.status_div.appendChild(this.container);
    }
}
