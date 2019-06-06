

class Game {
    constructor(text_id, username, user_list) {
    this.username = username;
    this.text = document.getElementById(text_id);
    this.user_list = user_list;
    this.process_user_list(this.user_list);
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
            else if (msg["msg"] == "do_smth"){
                this.process_do_smth(msg);
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

    /////////////////////////////////////////////////////////////

    process_user_list(user_list) {
        console.log('Hi: ', user_list)
        this.users = document.createElement("p");
        this.users.innerHTML = user_list;
        this.text.appendChild(this.users);

        this.get_character_choice();
    }


    clear_div(div){
        while (div.firstChild) {
            div.removeChild(div.firstChild);
        }
    }

    get_character_choice() {
        let btn_x = document.createElement('button');
        btn_x.innerHTML = 'X';
        btn_x.onclick = function(){
            console.log(btn_x.innerHTML, this.username);
        }.bind(this);
        this.text.appendChild(btn_x);

        this.str = document.createElement("p");
        this.str.innerHTML = "OR";
        this.text.appendChild(this.str);

        let btn_o = document.createElement('button');
        btn_o.innerHTML = 'O';
        btn_o.onclick = function(){
            console.log(btn_o.innerHTML, this.username);
        }.bind(this);
        this.text.appendChild(btn_o);
    }

}
