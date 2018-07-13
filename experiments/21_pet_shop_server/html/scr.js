


function update_log() {
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let log = document.getElementById("log");
            // log.innerHTML = xmlhttp.responseText;

            setTimeout(function(){
                update_content();
            }, 5000);
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xmlhttp.open("GET", "/zoo_shop_logs");
    xmlhttp.send();
}

function update_content() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        console.log(this.readyState, this.status);
        if (this.readyState == 4 && this.status == 200) {
            console.log("HELLO");
            let petShop = JSON.parse(xhttp.response);

            console.log(xhttp.response);
            console.log(petShop);

            parseTitle(petShop);
//            parseAnimals(petShop);
            tableAnimals(petShop)
            update_log();
        } else
            if (this.readyState == 4 && this.status != 200)
                alert("LOST");
    }
    xhttp.open("GET", "/zoo_shop_state");
    xhttp.send();
}

function parseTitle(jsonObj) {
    let content = document.getElementById("content");
    content.innerHTML = "";

    let myH1 = document.createElement('h1');
    myH1.textContent = jsonObj['title'];
    content.appendChild(myH1);

    let myPara = document.createElement('p');
    myPara.textContent = jsonObj['data_time'];
    content.appendChild(myPara);
}

function parseAnimals(jsonObj) {
    let animals = jsonObj['animals'];
    let content = document.getElementById("content");

    for (var i = 0; i < animals.length; i++) {
        let myArticle = document.createElement('article');
        let myH2 = document.createElement('h2');
        let myPara1 = document.createElement('p');
        let myPara2 = document.createElement('p');
        let myPara3 = document.createElement('p');
        let myPara4 = document.createElement('p');
        let myPara5 = document.createElement('p');

        myH2.textContent = animals[i].name;
        myPara1.textContent = animals[i].species + ': ' + animals[i].name;
        myPara2.textContent = animals[i].gender;
        myPara3.textContent = animals[i].age + ' years';
        myPara4.textContent = animals[i].weight + ' kg';
        myPara5.textContent = animals[i].description;

        myArticle.appendChild(myH2);
        myArticle.appendChild(myPara1);
        myArticle.appendChild(myPara2);
        myArticle.appendChild(myPara3);
        myArticle.appendChild(myPara4);
        myArticle.appendChild(myPara5);

        content.appendChild(myArticle);
    }
}




