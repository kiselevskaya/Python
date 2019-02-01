class Game {
    constructor(content_id) {
        this.content_div = document.getElementById(content_id);

        this.container = document.createElement("div");
        this.container.setAttribute("id", "container");

        this.img = document.createElement("img");
        this.img.setAttribute("src", "images/cookie.png");
        this.img.setAttribute("id", "muppet")
        this.img.style.position = "absolute";
        this.container.appendChild(this.img);
        this.content_div.appendChild(this.container);

        this.score_table = document.getElementById('table');

        this.container.onclick = function(event) {
            let cursorX = event.pageX - this.container.offsetLeft;
            let cursorY= event.pageY - this.container.offsetTop;
            this.wsc.send({"msg": "shoot", "result":[cursorX, cursorY]});
        }.bind(this);

        this.user_score = new Object();;
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
                this.process_user_list(msg);
            }
            else if (msg["msg"] == "hit" || msg["msg"] == "miss"){
                this.process_shoot(msg);
            }
            else
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
        this.content_div.innerHTML = "Websocket closed: " + event;
    }

    //

    process_tick(tick) {
        let x = tick["position"][0];
        let y = tick["position"][1];
        this.img.style.top = parseInt(y, 10) + "px";
        this.img.style.left = parseInt(x, 10) + "px";
        if (this.img.getAttribute("src") != "images/" + tick["image"]) {
            console.log("NEW IMAGE!!!!");
        }

    }

    process_shoot(msg){
        let user = msg["username"];
        let value = this.user_score[user];
        if (msg["msg"] == "hit"){
            value[0] += 1;
        } else {
            value[1] += 1;
        }
        this.update_table();
    }

    process_user_list(msg) {
        let user_set = Array.from(new Set(msg["user_list"]));
        console.log("process_user_list_"+user_set);
        for (let i = 0; i < user_set.length; i++) {
            if (!(user_set[i] in this.user_score)) {
                this.user_score[user_set[i]] = [0, 0];
            }
        }
        console.log("ghghg", this.user_score);
        this.process_score_table();

    }

    process_score_table(){
        let tbl = document.createElement("table");
        let tblBody = document.createElement("tbody");
        let num_of_user = Object.keys(this.user_score).length;

        for (let i = 0; i < (num_of_user+2); i++) {
            let row = document.createElement("tr");

            for (let j = 0; j < 3; j++) {
                let cell = document.createElement("td");

                if (i==0 && j==0){
                    let cellText = document.createTextNode('Name');
                    cell.rowSpan = 2;
                    cell.appendChild(cellText);
                    row.appendChild(cell);
                }
                else if (i==0 && j==1) {
                    let cellText = document.createTextNode('SCORE');
                    cell.colSpan = 2;
                    cell.appendChild(cellText);
                    row.appendChild(cell);
                }
                else if (i==1 && j==1){
                    let cellText = document.createTextNode('Hit');
                    cell.appendChild(cellText);
                    row.appendChild(cell);
                }
                else if (i==1 && j==2){
                    let cellText = document.createTextNode('Missed');
                    cell.appendChild(cellText);
                    row.appendChild(cell);
                }
                else if (i>1) {
                    for (let key in this.user_score) {
                        if (j==0){
                            let cellText = document.createTextNode(key);
                            cell.appendChild(cellText);
                            row.appendChild(cell);
                        }
                        if (j==1){
                            let cellText = document.createTextNode(this.user_score[key][0]);
                            cell.appendChild(cellText);
                            row.appendChild(cell);
                        }
                        if (j==2){
                            let cellText = document.createTextNode(this.user_score[key][1]);
                            cell.appendChild(cellText);
                            row.appendChild(cell);
                        }
                    }
                }
            }

        tblBody.appendChild(row);
        }

      tbl.appendChild(tblBody);
      this.score_table.appendChild(tbl);
      tbl.setAttribute("border", "2");
    }

    update_table() {
        while (this.score_table.firstChild) {
            this.score_table.removeChild(this.score_table.firstChild);
        }
        this.process_score_table();
    }

}
