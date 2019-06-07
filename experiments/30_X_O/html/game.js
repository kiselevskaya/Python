

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
            }else
            if (msg["msg"] == "characters") {
                this.process_characters(msg);
            } else {
                console.log("unknown message: ", json_msg);
            }
        } catch(e) {
            console.log(e);
            this.wsc.close();
        }
    }

    onWebsocketError(event) {
        this.text.innerHTML = "Websocket error: " + event;
    }

    onWebsocketClose(event) {
        this.text.innerHTML = "Websocket closed: " + event;
    }

    /////////////////////////////////////////////////////////////

    process_user_list(user_list) {
        this.clear_div(this.text);
        this.users = document.createElement("p");
        this.users.innerHTML = this.user_list;
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
        btn_x.innerHTML = "X";
        btn_x.onclick = function(){
            console.log(btn_x.innerHTML, this.username);
            this.wsc.send({"msg": "button", "character": btn_x.innerHTML});
        }.bind(this);
        this.text.appendChild(btn_x);

        this.str = document.createElement("p");
        this.str.innerHTML = "OR";
        this.text.appendChild(this.str);

        let btn_o = document.createElement('button');
        btn_o.innerHTML = "O";
        btn_o.onclick = function(){
            console.log(btn_o.innerHTML, this.username);
            this.wsc.send({"msg": "button", "character": btn_o.innerHTML});
        }.bind(this);
        this.text.appendChild(btn_o);
    }

    process_characters(msg) {
        this.clear_div(this.text);
        this.create_user_data_table(msg);
    }

    create_user_data_table(msg) {
        let table = document.createElement("table");
        table.border=1;
        this.text.appendChild(table);

        for(let i = 0 ; i < Object.keys(msg["users_data"]).length ; ++i ) {
            let user_name = Object.keys(msg["users_data"])[i];
            let tr = document.createElement("tr");
            let name = document.createElement("td");
            name.appendChild(document.createTextNode(user_name));

            let character = document.createElement("td");
            let char_div = document.createElement("div");
            char_div.id = user_name + "_char_div";
            char_div.appendChild(document.createTextNode(msg["users_data"][user_name][0]));
            character.appendChild(char_div);

            let score = document.createElement("td");
            let score_div = document.createElement("div");
            score_div.id = user_name + "_score_div";
            score_div.appendChild(document.createTextNode(msg["users_data"][user_name][1]));

            score.appendChild(score_div);

            tr.appendChild(name);
            tr.appendChild(character);
            tr.appendChild(score);

            table.appendChild(tr);
        }
    }

}
