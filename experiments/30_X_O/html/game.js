

class Game {
    constructor(text_id, username, user_list) {
    this.username = username;
    this.text = document.getElementById(text_id);
    this.user_list = user_list;
    this.process_user_list(this.user_list);
    this.game_started = false;
    }

    setWebsocketConnection(wsc) {
        this.wsc = wsc;
    }

    onWebsocketMessage(json_msg) {
        try {
            let msg = JSON.parse(json_msg);
            if (msg["msg"] == "user_list") {
                this.process_user_list(msg);
            } else if (msg["msg"] == "characters") {
                this.process_characters(msg);
            } else if (msg["msg"] == "board") {
                this.process_board(msg);
            } else if (msg["msg"] == "user_info") {
                this.update_user_data(msg);
            } else if (msg["msg"] == "board_info") {
                this.update_board_data(msg);
            } else if (msg["msg"] == "winner_info") {
                this.process_winner_info(msg);
            } else if (msg["msg"] == "reset") {
                this.process_reset(msg);
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
        this.game_started = true;
        this.clear_div(this.text);
        this.create_user_data_table(msg);
    }

    create_user_data_table(msg) {
        this.users_table = document.createElement("table");
        this.users_table.border=1;
        this.text.appendChild(this.users_table);
        this.user_info = msg["users_data"];

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

            this.users_table.appendChild(tr);
        }
    }

    process_board(msg) {
        this.board = msg["new_board"];

        this.board_div = document.getElementById("field");

        this.table = document.createElement("table");
        this.table.style.border = "1px solid black";
//        this.table.style.height = "250px";
//        this.table.style.width = "250px";

        for (let row = 0; row < this.board.length; row++) {
            let tr = document.createElement('tr');
            for (let col = 0; col < this.board[row].length; col++){
                let td = document.createElement('td');
                td.style.height = "20px";
                td.style.width = "20px";
                let tn = document.createTextNode(this.board[row][col]);
                td.appendChild(tn);
                tr.appendChild(td);
                td.style.border = "1px solid black";
                td.onclick = function(){
                    console.log("position:", [row, col]);
                    if (tn.nodeValue == "" && this.user_info[this.username][2] == true) {
                        this.wsc.send({"msg": "step", "position": [row, col]});
                    }
                }.bind(this);
            }
            this.table.appendChild(tr);
        }
        this.board_div.appendChild(this.table);
    }

    update_user_data(msg) {
        this.user_info = msg["update"];
    }

    update_board_data(msg) {
        this.board = msg["update"];

        for (let row = 0; row < this.board.length; row++) {
            for (let cell = 0; cell < this.board[row].length; cell++){
                this.table.rows[row].cells[cell].innerHTML = this.board[row][cell];
            }
        }
    }

    process_winner_info(msg) {
        this.update_score(msg);
        this.win_set = msg["data"][1];
        this.draw_win_set(this.win_set);
        this.add_reset_button();
    }

    update_score(msg) {
        let winner = msg["data"][0];
        let score_id = winner + "_score_div";
        let score = document.getElementById(score_id);
        score.innerHTML = parseInt(this.user_info[winner][1]);
    }

    draw_win_set(list) {
        console.log("DRAW");
        for (let p = 0; p < list.length; p++){
            this.table.rows[list[p][0]].cells[list[p][1]].style.color = "red";
        }
    }

    add_reset_button() {
        this.reset = document.createElement('button');
        this.reset.innerHTML = "RESET";
        this.reset.onclick = function(){
            this.wsc.send({"msg": "reset_status"});
        }.bind(this);

        this.text.appendChild(this.reset);
    }

    process_reset() {
        this.text.removeChild(this.reset);
        for (let p = 0; p < this.win_set.length; p++){
            this.table.rows[this.win_set[p][0]].cells[this.win_set[p][1]].style.color = "black";
        }
    }

}
