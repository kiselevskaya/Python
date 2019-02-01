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

        this.score_table = document.getElementById('table')
        this.create_score_table();

        this.container.onclick = function(event) {
            let cursorX = event.pageX - this.container.offsetLeft;
            let cursorY= event.pageY - this.container.offsetTop;
            this.wsc.send({"msg": "shoot", "result":[cursorX, cursorY]});
        }.bind(this);
    }


    setWebsocketConnection(wsc) {
        this.wsc = wsc;
    }

    onWebsocketMessage(json_msg) {
        try {
            let msg = JSON.parse(json_msg);
            if (msg["msg"] == "tick")
                this.process_tick(msg);
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

    create_score_table(){
        let tbl = document.createElement("table");
        let tblBody = document.createElement("tbody");
        let test_users = [['user1', 0, 0], ['user2', 0, 0], ['user3', 0, 0]];

        for (let i = 0; i < (test_users.length+2); i++) {
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
                else if (i>1 && j==0) {
                    let cellText = document.createTextNode(test_users[i-2][0]);
                    cell.appendChild(cellText);
                    row.appendChild(cell);
                }
                else if (i>1 && j==1) {
                    let cellText = document.createTextNode(test_users[i-2][1]);
                    cell.appendChild(cellText);
                    row.appendChild(cell);
                }
                else if (i>1 && j==2) {
                    let cellText = document.createTextNode(test_users[i-2][2]);
                    cell.appendChild(cellText);
                    row.appendChild(cell);
                }
            }

        tblBody.appendChild(row);
        }

      tbl.appendChild(tblBody);
      this.score_table.appendChild(tbl);
      tbl.setAttribute("border", "2");
    }

}
