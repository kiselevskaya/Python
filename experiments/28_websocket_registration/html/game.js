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

        this.container.onclick = function(event) {
            let aim = event.target;
            if (aim === this.img){
                this.wsc.send({"msg": "shoot", "result": "hit"});
            } else {
                this.wsc.send({"msg": "shoot", "result": "missed"});
            }
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

}
