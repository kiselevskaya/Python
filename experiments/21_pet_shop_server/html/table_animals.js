
function tableAnimals(jsonObj) {
    let animals = jsonObj['animals'];
    let content = document.getElementById("content");
//    content.innerHTML = "";

    let table = document.createElement('table');
    table.width = "100%";
//    table.id = 'itemData';

    let thead = document.createElement('thead');
    table.appendChild(thead);

    let tbody = document.createElement('tbody');
    table.appendChild(tbody);

    let header = document.createElement('tr');

    let name = document.createElement('th');
    let gender = document.createElement('th');
    let age = document.createElement('th');
    let weight = document.createElement('th');
    let description = document.createElement('th');
    let species = document.createElement('th');

    name.appendChild(document.createTextNode('Name'));
    gender.appendChild(document.createTextNode('Gender'));
    age.appendChild(document.createTextNode('Age (years)'));
    weight.appendChild(document.createTextNode('Weight (kg)'));
    description.appendChild(document.createTextNode('Description'));
    species.appendChild(document.createTextNode('Species'));

    header.appendChild(name);
    header.appendChild(gender);
    header.appendChild(age);
    header.appendChild(weight);
    header.appendChild(description);
    header.appendChild(species);

    thead.appendChild(header);

    for (var i = 0; i < animals.length; i++) {
        let tr = document.createElement('tr');
        let nameCell = document.createElement('td');
        let genderCell = document.createElement('td');
        let ageCell = document.createElement('td');
        let weightCell = document.createElement('td');
        let descriptionCell = document.createElement('td');
        let speciesCell = document.createElement('td');

        nameCell.appendChild(document.createTextNode(animals[i].name));
        genderCell.appendChild(document.createTextNode(animals[i].gender));
        ageCell.appendChild(document.createTextNode(animals[i].age));
        weightCell.appendChild(document.createTextNode(animals[i].weight));
        descriptionCell.appendChild(document.createTextNode(animals[i].description));
        speciesCell.appendChild(document.createTextNode(animals[i].species));

        tr.appendChild(nameCell);
        tr.appendChild(genderCell);
        tr.appendChild(ageCell);
        tr.appendChild(weightCell);
        tr.appendChild(descriptionCell);
        tr.appendChild(speciesCell);
        tbody.appendChild(tr);
    }

    content.appendChild(table);
}
