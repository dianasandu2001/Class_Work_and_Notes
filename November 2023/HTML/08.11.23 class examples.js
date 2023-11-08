//declare variables: const, let, var
//recommendation: const, let
/*
let char= "hi";
console.log(char);
alert(char);
prompt("who are you?");


//if statement
let num1 = prompt("Give me the 1st number: ");
let num2 =  prompt("Give me the 2nd number: ");
if(num1 != num2){
    console.log("This " + num1 + "and " + num2 + "are not the same");
}

// if else statement
let num = prompt("Let's check a number");
if(num % 2 == 0) {
    console.log("this is an even number")
}
else {
    console.log("This is an odd number")
}

const age = prompt("How old are you? ")
if (age>=65) {
    console.log("oops, you're old xd")
}
else if (age>= 18) {
    console.log("Life is still long, you are young")
}
else if (age> 5) {
    console.log("Go back, kiddo")
}

const num = prompt("Input a number ")
if (num>=0) {
    console.log("The number is positive")
}
else if (num<0) {
    console.log("The number is negative")
}
else {
    console.log("i said a number")
}

let age, dose, weight;
    age = prompt("how old is the patient?")
    if (age>=12){
        dose = 500;
    }
    else if (age >=2) {
        weight = prompt("What is the weight of the patient? ")
        dose = weight*12.5
        if (dose>500){
            dose = 450;
        }
    }
else{
    console.log("the patient is too young to take the medicine")
    }
console.log("The dose for the patient is "+ dose)

const cabinClass = prompt("what is your cabinclass A/B/C")
    switch(cabinClass){
        case "A":
            console.log("Your cabin is top floor with a sea view");
            break;
        case "B":
            console.log("Your cabin is upper floor with a window");
            break;
        case "C":
            console.log("Your cabin is lower floor with a nice hallway");
            break
        default:
        console.log("You should input a valid class")
    }

//while
const weight = prompt("Enter your weight")
while(weight <=0 ){
    console.log("Your weight has to be a positive number")
}
console.log("Your weight is "+ weight);

// for loop
for (let i = 0; i <=10; i++){
    console.log(i);
}

let multiplication;
for (let i=1; i<=5; i++){
    for (let j=1; j <=5; j++){
        multiplication = i * j;
        console.log("this is the multiplication: " + i + " time " + j + " is " + multiplication)
    }
}

//array
const array = [];
// add items to the array
array[0] = 3
array[1] = 4;
array[2] = 5;
console.log(array);
const array2 = [4, 6.8];
console.log(array2);
// array and loop:
const nameList = ["Cha-del", "Lihn", "Kim"];
for (let i=0; i<nameList.length; i++){
    console.log(`Names in the list:${nameList[i]}`)
}
//object
const student = {
    firstName: "Peter",
    lastName: "Pan",
    studentID: "001",
    phoneNum: "123456789",
}
const greeting = `hello, my name is ${student.firstName} ${student.lastName}`;
const studentInfo = `student number is: ${student.phoneNum} and my student ID is ${student.studentID}`
console.log(greeting);
console.log(studentInfo);
student.address = "Hameentie 23"
console.log(student);
delete student.phoneNum;
console.log(student);

//function

function greet(){
    console.log("Hi all!");
}
greet();

function greetCompli(text, times){
    for (let i=1; i<= times; i++){
        console.log(text + " " +i +" times");
    }
}
greetCompli("look, I am saying to you hi", 5)

function disCalculation(total, percent){
    const percentage = percent / 100
    const disResult = total*percentage;
    return disResult;
}
let total = prompt("Please input the total sum of bill: ");
let percent = prompt("How many percentage discount? ");
let result = disCalculation(total, percent);
console.log("You have got a discount of " + result+ " euros");

function numIncrease(array){
    for (let i = 0; i<array.length; i++){
        array[i]++;
        console.log(array[i]);
    }
    return;
}

const number = [8,9,10]
numIncrease(number);
console.log(number[0], " ", number[1], " ", number[2]);

*/
// array as return value in function
function makeSentance(){
    let newArray = new Array(5)
    newArray[0]="This";
    newArray[1]="is";
    newArray[2]="the almost";
    newArray[3]="end of";
    newArray[4]="our class";
    return newArray;
}
function showSentence(array){
    let sentence = " ";
    for (let i = 0; i<array.length; i++){
        sentence += array[i] + " ";
    }
    return sentence;
}

const  sent1 = makeSentance();
console.log(showSentence(sent1))

//object and function
function creditCal(credits){
    return 240 - credits;
}
let stud = {
    firstName: "Phil",
    lastName: "Lester",
    credits: 30,
}
let remainingCredits = creditCal(stud.credits)
console.log("Student " + stud.firstName + " has " + remainingCredits + " credits remaining.")
