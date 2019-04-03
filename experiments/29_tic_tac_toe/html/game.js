

class SomeClass {
    constructor(text_id, username, password) {
    this.username = username;
    this.text = document.getElementById(text_id);

    this.first_user = document.getElementById("user1");
    this.user1 = document.createElement("h2");
    this.u1choice = document.getElementById("u1choice");
    this.u1score = document.getElementById("u1score");

    this.second_user = document.getElementById("user2");
    this.user2 = document.createElement("h2");
    this.u2choice = document.getElementById("u2choice");
    this.u2score = document.getElementById("u2score");

    this.choice_x = document.getElementById("x");
    this.choice_or = document.getElementById("or");
    this.choice_o = document.getElementById("o");

    this.info =  new Object();
    this.started = false;

    this.beginner = true;
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
            else if (msg["msg"] == "board"){
                this.process_board(msg);
            }
            else if (msg["msg"] == "win"){
                this.process_win(msg);
            }
            else if (msg["msg"] == "next"){
                this.process_next(msg);
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

    process_user_list(msg) {
        let user_list = msg["user_list"];
        this.user1.innerHTML = user_list[0];

        if (user_list.length > 1){
            this.user2.innerHTML = user_list[1];
        } else {
            this.user2.innerHTML = "Computer";
        }

        this.first_user.appendChild(this.user1);
        this.second_user.appendChild(this.user2);

        this.get_choice();
    }

    get_choice() {
        let btn_x = document.createElement('button');
        btn_x.setAttribute("class", "button");
        btn_x.innerHTML = 'X';

        let btn_o = document.createElement('button');
        btn_o.setAttribute("class", "button");
        btn_o.innerHTML = 'O';

        btn_x.onclick = function(){
            this.process_choice(btn_x.innerHTML, true, btn_o.innerHTML, false)
        }.bind(this);
        this.choice_x.appendChild(btn_x);

        btn_o.onclick = function(){
            this.process_choice(btn_o.innerHTML, false, btn_x.innerHTML, true)
        }.bind(this);
        this.choice_o.appendChild(btn_o);

        let node_or = document.createElement("p");
        node_or.innerHTML = "OR";
        this.choice_or.appendChild(node_or);
    }

    process_choice(choice, order1, rest, order2) {
        this.started = true;
        this.wsc.send({"msg": "choice", "status": this.started});
        this.clear_div(this.choice_x);
        this.clear_div(this.choice_or);
        this.clear_div(this.choice_o);

        let user1_choice = document.createElement("p");
        let user2_choice = document.createElement("p");
        this.user1_score = document.createElement("p");
        this.user2_score = document.createElement("p");

        if (this.user1.innerHTML == this.username) {
            user1_choice.innerHTML = choice;
            user2_choice.innerHTML = rest;
            this.info[this.user1.innerHTML] = [choice, 0, order1];
            this.info[this.user2.innerHTML] = [rest, 0, order2];
        } else {
            user2_choice.innerHTML = choice;
            user1_choice.innerHTML = rest;
            this.info[this.user2.innerHTML] = [choice, 0, order1];
            this.info[this.user1.innerHTML] = [rest, 0, order2];
        }

        this.user1_score.innerHTML = this.info[this.user1.innerHTML][1];
        this.user2_score.innerHTML = this.info[this.user2.innerHTML][1];

        this.u1choice.appendChild(user1_choice);
        this.u2choice.appendChild(user2_choice);
        this.u1score.appendChild(this.user1_score);
        this.u2score.appendChild(this.user2_score);
    }

    process_board(msg){
        this.board = msg["new_board"]
        let container = document.getElementById('container');
        this.table = document.createElement('table');
        this.table.style.border = "1px solid black";
        for (let row = 0; row < this.board.length; row++){
            let tr = document.createElement('tr');
            for (let col = 0; col < this.board[row].length; col++){
                let td = document.createElement('td');
                let tn = document.createTextNode(this.board[row][col]);
                td.appendChild(tn);
                tr.appendChild(td);
                td.style.border = "1px solid black";
                td.onclick = function(){
                    if (this.started) {
                        if (tn.nodeValue == "" && this.info[this.username][2] == this.beginner) {
                            tn.nodeValue = this.info[this.username][0];
                            this.wsc.send({"msg": "step", "user":this.username, "position": [row, col], "char": this.info[this.username][0]});
                            if (this.beginner) {
                                this.beginner = false;
                            } else {
                                this.beginner = true;
                            }
                        }
                    }
                }.bind(this);
            }
            this.table.appendChild(tr);
        }
        container.appendChild(this.table);

        this.process_computer_step();
    }

    process_computer_step() {
        if (this.info["Computer"][2] == this.beginner && this.started){
            console.log("Computer random step")
            let y = Math.floor(Math.random() * this.board.length);
            let x = Math.floor(Math.random() * this.board.length);
            while (this.table.rows[y].cells[x].innerHTML != ""){
                y = Math.floor(Math.random() * this.board.length);
                x = Math.floor(Math.random() * this.board.length);
            }
            console.log(y, x);
            this.table.rows[y].cells[x].innerHTML = this.info["Computer"][0];
            this.wsc.send({"msg": "step", "user":"Computer", "position": [y, x], "char": this.info["Computer"][0]});

            if (this.beginner) {
                this.beginner = false;
            } else {
                this.beginner = true;
            }
        }
    }

    process_next(msg){
        console.log(msg['next_player'])
        this.process_computer_step()
    }

    process_win(msg){
        this.started = false
        console.log("WIN", msg["combination"])

        for(let pos in msg["combination"]){
            let y = msg["combination"][pos][0];
            let x = msg["combination"][pos][1];
            this.table.rows[y].cells[x].style.fontSize = "30px";
        }
        let winner = this.table.rows[msg["combination"][0][0]].cells[msg["combination"][0][1]].innerHTML;
        this.process_score(winner);
    }

    process_score(winner){
        for (let key in this.info){
            if (this.info[key][0] == winner) {
                this.info[key][1] += 1;
            }
        }
    }

    clear_div(div){
        while (div.firstChild) {
            div.removeChild(div.firstChild);
        }
    }

}
