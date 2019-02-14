class Game {
    constructor(content_id, username, user_list) {
        this.username = username;
        this.content_div = document.getElementById(content_id);

        this.container = document.createElement("div");
        this.container.setAttribute("id", "container");

        this.img = document.createElement("img");
        this.img.setAttribute("src", "images/"+"cookie.png");
        this.img.setAttribute("id", "muppet")
        this.img.style.position = "absolute";
        this.container.appendChild(this.img);
        this.content_div.appendChild(this.container);

        this.score_table = document.getElementById("score-block");
        this.clear_div(this.score_table);

        this.level = document.getElementById("level");
        this.level_content = document.createElement("p");
        this.level_num = 1;
        this.level_content.innerHTML = "Level "+this.level_num;
        this.level.appendChild(this.level_content);

        this.container.onclick = function(event) {
            if (this.lost || this.win) {
                return;
            }
            let cursorX = event.pageX - this.container.offsetLeft;
            let cursorY= event.pageY - this.container.offsetTop;
            this.wsc.send({"msg": "shoot", "result":[cursorX, cursorY]});
        }.bind(this);

        this.lost = false;
        this.win = false;

        this.user_list = user_list;
        this.process_user_list(this.user_list);
    }


    setWebsocketConnection(wsc) {
        this.wsc = wsc;
    }

    onWebsocketMessage(json_msg) {
        try {
            let msg = JSON.parse(json_msg);
            if (msg["msg"] == "tick") {
                this.process_tick(msg);
            }
            else if (msg["msg"] == "user_list"){
                this.process_user_list_msg(msg);
            }
            else if (msg["msg"] == "hit" || msg["msg"] == "miss"){
                this.update_score(msg);
            }
            else if (msg["msg"] == "round"){
                this.process_level(msg);
            }
            else if (msg["msg"] == "win"){
                this.process_win(msg);
            }
            else if (msg["msg"] == "lost"){
                this.process_lost(msg);
            }
            else if (msg["msg"] == "stop"){
                this.process_game_stop(msg);
            } else
                console.log("unknown message " + json_msg);
        } catch(e) {
            console.log(e);
            this.wsc.close();
        }
    }

    onWebsocketError(event) {
        this.content_div.innerHTML = "Websocket error: " + event;
    }

    onWebsocketClose(event) {
        if (!this.lost || !this.win) {
            this.content_div.innerHTML = "Websocket closed: " + event;
        }
    }

    //

    process_tick(tick) {
        if (!this.lost) {
            let x = tick["position"][0];
            let y = tick["position"][1];
            this.img.style.top = parseInt(y, 10) + "px";
            this.img.style.left = parseInt(x, 10) + "px";
            if (this.img.getAttribute("src") != "images/" + tick["image"]) {
                this.img.setAttribute("src", "images/"+tick["image"]);
            }
        }
    }

    process_user_list_msg(msg) {
        if (this.user_list == msg["user_list"] && this.user_list.length != 0) {
            this.process_user_list(this.user_list);
        }
    }

    process_user_list(user_list) {
        console.log("process_user_list_", user_list);
        this.process_score_table(user_list);
    }

    process_level(msg) {
        this.level_num = msg['level'];
        this.level.innerHTML = "Level "+this.level_num;
    }

    process_win(msg) {
        if (msg["username"] == this.username) {
            this.img.setAttribute("src", "images/" + msg["image"]);
            this.img.style.left = "180px";
            this.img.style.top = "180px";
            this.win = true;
//            this.wsc.close();
            this.container.onclick = function() {}
        }
    }

    process_lost(msg) {
        if (msg["username"] == this.username) {
            this.img.setAttribute("src", "images/" + msg["image"]);
            this.img.style.left = "180px";
            this.img.style.top = "180px";
            this.lost = true;
//            this.wsc.close();
            this.container.onclick = function() {}
        }
    }

    process_score_table(user_list){
        let table = document.createElement("table");
        table.border=1;
        let heads = [["Name", "Score"], ["Hit", "Missed"]]

        for (let i = 0 ; i < heads.length ; ++i) {
            let trh = document.createElement("tr");
            for (let u = 0 ; u < heads[i].length ; ++u) {
                let th = document.createElement("th");
                th.appendChild(document.createTextNode(heads[i][u]));
                trh.appendChild(th);
            }
            table.appendChild(trh);
        }
        table.rows[0].cells[1].colSpan = 2;
        table.rows[0].cells[0].rowSpan = 2;
        this.score_table.appendChild(table);

        for(let i = 0 ; i < user_list.length ; ++i ) {
            let user_name = user_list[i];
            let tr = document.createElement("tr");
            let td1 = document.createElement("td");
            td1.appendChild(document.createTextNode(user_name));

            let tdh = document.createElement("td");
            let hitdiv = document.createElement("div");
            hitdiv.id = user_name + "_hitdiv";
            hitdiv.appendChild(document.createTextNode("0"));
            tdh.appendChild(hitdiv);

            let tdm = document.createElement("td");
            let missdiv = document.createElement("div");
            missdiv.id = user_name + "_missdiv";
            missdiv.appendChild(document.createTextNode("0"));

            tdm.appendChild(missdiv);

            tr.appendChild(td1);
            tr.appendChild(tdh);
            tr.appendChild(tdm);

            table.appendChild(tr);
        }
    }

    update_score(msg) {
        if (msg["msg"] == "hit") {
            let div_id = msg["username"] + "_hitdiv";
            let d = document.getElementById(div_id);
            let c = d.innerHTML;
            d.innerHTML = parseInt(c) + 1;
        } else {
            let div_id = msg["username"] + "_missdiv";
            let d = document.getElementById(div_id);
            let c = d.innerHTML;
            d.innerHTML = parseInt(c) + 1;
        }
    }

    clear_div(div) {
        while (div.firstChild) {
           div.removeChild(div.firstChild);
        }
    }

    process_game_stop(msg){
        if (msg["status"] == true) {
            console.log("TRUE");

            this.clear_div(this.content_div);
            this.clear_div(this.score_table);
            this.clear_div(this.level);

            this.game = new PreGame("page_content", params.get("username"), params.get("password"), this.user_list);
            this.wsc.setGame(this.game);
            this.game.setWebsocketConnection(this.wsc);
//            window.location.pathname = "/new_game";

        }
    }

}
