

function orderWeight(strng) {
//    console.log(strng);
    let output = [];
    let weightList = strng.split(" ").sort();
//    console.log(weightList);
    let sumList = [];

    for (let i=0; i < weightList.length; i++){
        sumList.push(sumDigits(parseInt(weightList[i])));
    }

    sumList.sort(function(a, b){return a-b});
//    console.log(sumList);
    let uniqueSumList = Array.from(new Set(sumList));
//    console.log(uniqueSumList);

    for (let i=0; i < uniqueSumList.length; i++) {
        for (let j=0; j < weightList.length; j++){
            if (sumDigits(parseInt(weightList[j])) === uniqueSumList[i]) {
                output.push(weightList[j]);
            }
        }
    }
    console.log(output);
    console.log(output.toString().replace(/,/g,' '));
}

function sumDigits(value) {
    let sum = 0;
    while (value) {
        sum += value % 10;
        value = Math.floor(value / 10);
    }
    return sum;
}


orderWeight("103 123 4444 99 2000");
orderWeight("2000 10003 1234000 44444444 9999 11 11 22 123");


//Test.describe("Order Weights",function() {
//Test.it("Basic tests",function() {
//    Test.assertEquals(orderWeight("103 123 4444 99 2000"), "2000 103 123 4444 99")
//    Test.assertEquals(orderWeight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
//})})
//["11", "11", "2000", "10003", "22", "123", "1234000", "44444444", "9999"]
