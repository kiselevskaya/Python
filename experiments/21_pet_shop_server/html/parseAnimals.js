

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
