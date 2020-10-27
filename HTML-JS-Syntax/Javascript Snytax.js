//single line comment
/* multi line comment */

//prints data on the console access it by using ctrl + shift + I
console.log("Hello World")

//returns a number between 0 and 1 using the math library's random function
Math.random();
//returns the length of the given string
console.log("Hello".length);
//returns the largest integer less than or equal to the given number
console.log(Math.floor(5.95)); //returns 5

/*
	since it is like most other programming languages,
	normal arithmetic operations like +-/* works in addition to % (Modulo)
	which returns the remainder after dividing the numbers provided
	
	In addition to shorten the code things like
	num = num + 1;
	can also become 
	num += 1;
*/

//to declare a variable
var amount1 = 6;
let amount2 = 6;
//it is to store a constant value NOTE: attempting to change the value would cause a runtime error
const dollar = "$";

let age=7
// String concatenation
'Tommy is ' + age + ' years old.';
/*string interpolation - process of evaluating string with one or more placeholder
 ${expression}, is also known as a template literal like the one below
 another example would be: console.log(`Billy is ${6+8} years old.`) 
 NOTE: this uses a backtick instead of normal quotes or double quotes like string does*/
`Tommy is ${age} years old.`;

//logical operator - if one or both values are true return true, if both value false, return false
// OR operator
true || false;        // true
10 > 5 || 10 > 20;    // true
false || false;       // false
10 > 100 || 10 > 20;  // false
// AND operator if both values are true, returns true, if one or both values are false, returns false
true && true;      // true
1 > 2 && 2 > 1;    // false
true && false;     // false
4 === 4 && 3 > 1;  // true
//NOT operator - inverts a boolean value
let correct = true;
let opposite = !correct; //this value is now false

//ternary operator - can either use with conditions aka if else or using the ? way
let price = 10.5;
let day = "Monday";

day === "Monday" ? price -= 1.5 : price += 1.5;

//conditions
let score = 0;

if(score >= 50) {
	console.log("Passed");
}
else if(score < 50) {
	console.log("Failed");
}
else {
	console.log("Invalid score");
}

var food = "pizza";
switch(food) {
	case 'pizza':
		console.log("nice pizza");
		break;
	case 'oyster':
		console.log("nice oyster");
		break;
	default:
		console.log("enjoy");
}

//comparison operator
/*
=== - both data type and the two values are the same so 1 === '1' is false
!== - both data type and the two values are not the same
>
>=
<
<=
*/

//arrow function -> eliminates the need to use the function keyword
//uses a fat arrow to separate parameters from the body
const sum = (num1, num2) => {
	return num1 + num2;
}
console.log(sum(2, 5)); //7

//example 2
let plusFive = (number) => {
  return number + 5;  
};
// f is assigned the value of plusFive
let f = plusFive;

plusFive(3); // 8
// Since f has a function value, it can be invoked. 
f(9); // 14

//normal function
function sum(num1, num2) {
	return num1 + num2;
}

sum(3, 6); //9

//function expressions - creates the function inside an expression
const dog = function() {
	return 'Woof!';
}

//Array usage
//arrays in javascript are mutable, so even if declared as constant it can still be 
//modified using push, pop and reassign values
const nums = [1,2,3,4];
nums.length; //4

//accessing particular index value
nums[0]; //1

//adding on to the end of the array
nums.push(5);
nums.push(6,7,8);

//removing the last element from the array
const poppednum = nums.pop(); //8

//reduce method iterates through an array and retuns a single value
//useful for times like below where you need to add all the values in an array together
const arrayOfNumbers = [1, 2, 3, 4];

const sum = arrayOfNumbers.reduce((accumulator, currentValue) => {  
  return accumulator + currentValue;
});

console.log(sum); // 10

//for each method executes a callback function on each of the elements in the array in order
const numbers = [28, 77, 45, 99, 27];

numbers.forEach(number => {  
  console.log(number);
}); 

//filter method executes a callback function on each element in an array
// this returns another array with any elements that matches the condition
const randomNumbers = [4, 11, 42, 14, 39];
const filteredArray = randomNumbers.filter(n => {  
  return n > 5;
});

//map method executes a callback function on each element in an array
//this returns another array based on what is in the function
//unlike filter, which filters out elements that does not match certain conditions
const finalParticipants = ['Taylor', 'Donald', 'Don', 'Natasha', 'Bobby'];

const announcements = finalParticipants.map(member => {
  return member + ' joined the contest.';
})

console.log(announcements);

//loops
//while loop
let i=0;
while (i < 5) {
	console.log(i);
	i++;
}

//for loop
const nums = [1,2,3,4];
for(var i=0; i<nums.length; i++) {
	console.log(nums[i]);
}

//reverse for loop
const items = ['apricot', 'banana', 'cherry'];

for (let i = items.length - 1; i >= 0; i -= 1) {
  console.log(`${i}. ${items[i]}`);
}

// Prints: 2. cherry
// Prints: 1. banana
// Prints: 0. apricot

//do while loop - NOTE: this is executed at least once before looking at the condition
x = 0
i = 0

do {
  x = x + i;
  console.log(x)
  i++;
} while (i < 5);

// Prints: 0 1 3 6 10

//Objects -> store data in key-value pairs (similar to JSON)
//2 ways of creating an object, one is in this portion of the guide, 2nd way is using a class which is in the next part
//properties of an object can be accessed using the dot notation: object.propertyname
const apple = { 
  color: 'Green',
  price: {
    bulk: '$3/kg',
    smallQty: '$4/kg'
  }
};
console.log(apple.color); // 'Green'
console.log(apple.price.bulk); // '$3/kg'

//objects are muatable, so the values can be changed even if declared as constant
const student = {
  name: 'Sheldon',
  score: 100,
  grade: 'A',
}

console.log(student)
// { name: 'Sheldon', score: 100, grade: 'A' }

delete student.score
student.grade = 'F'
console.log(student)
// { name: 'Sheldon', grade: 'F' }

student = {}
// TypeError: Assignment to constant variable.

//delete opratator -> used to delete properties from an object
const person = {
  firstName: "Matilda",
  age: 27,
  hobby: "knitting",
  goal: "learning JavaScript"
};

delete person.hobby; // or delete person[hobby];
//when printed, only firstName, age, and goal is left

//passing objects as arguments, this makes it possible to just call it like a function
//and passing in the values that you would like to have dynamically
const origNum = 8;
const origObj = {color: 'blue'};

const changeItUp = (num, obj) => {
  num = 7;
  obj.color = 'red';
};

changeItUp(origNum, origObj);

//object methods -> similar to java objects are allowed to have methods that
//manipulates data in the object or that act as accessor or mutator, aka get or set methods

//destructuring assignment is a shorthand syntax that allows object properties to be extracted into variables
const rubiksCubeFacts = {
  possiblePermutations: '43,252,003,274,489,856,000',
  invented: '1974',
  largestCube: '17x17x17'
};
const {possiblePermutations, invented, largestCube} = rubiksCubeFacts;
console.log(possiblePermutations); // '43,252,003,274,489,856,000'
console.log(invented); // '1974'
console.log(largestCube); // '17x17x17'

//shorthand property name syntax also allows for creation of objects without specifying property names
const activity = 'Surfing';
const beach = { activity };
console.log(beach); // { activity: 'Surfing' }

//this keyword -> can be used to access properties belonging to that object
//NOTE: using this keyword when it is in a function defined outside of the object,
//would refer to the global object
const cat = {
  name: 'Pipey',
  age: 8,
  whatName() {
    return this.name  
  }
};

console.log(cat.whatName()); 
// Output: Pipey

//example of a incorrect usage, because arrow functions do not have their own this context
//so the arrow function attempts to find data in the global context but it is not there
const myObj = {
    data: 'abc',
    loggerA: () => { console.log(this.data); },
    loggerB() { console.log(this.data); },
};

myObj.loggerA();    // undefined
myObj.loggerB();    // 'abc'

//access and mutator methods, aka getters and setters
const myCat = {
  _name: 'Snickers',
  get name(){
    return this._name
  },
  set name(newName){
    //Verify that newName is a non-empty string before setting as name property
    if (typeof newName === 'string' && newName.length > 0){
      this._name = newName; 
    } else {
      console.log("ERROR: name must be a non-empty string"); 
    }
  }
}

//a function that returns an object is known as a factory function
//these functions usually accept parameters to customize the return object
// A factory function that accepts 'name', 
// 'age', and 'breed' parameters to return 
// a customized dog object. 
const dogFactory = (name, age, breed) => {
  return {
    name: name,
    age: age,
    breed: breed,
    bark() {
      console.log('Woof!');  
    }
  };
};

//to prevent incorrect interactions with object properties, 
//it might be a better idea to use a getter and setter when interacting with object properties
const myCat = {
  _name: 'Dottie',
  get name() {
    return this._name;  
  },
  set name(newName) {
    this._name = newName;  
  }
};

// Reference invokes the getter
console.log(myCat.name);

// Assignment invokes the setter
myCat.name = 'Yankee';

//static methods -> are not called on individual instances of the class but are called on the call itself
//aka you can just directly call it after specifying the class name, e.g. Dog.bark()
//instead of the usual const myDog = new Dog("LOL"); myDog.introduce();

//this is also known as creating an object
//when an object is created based on the class, the new object is referred to as an instance of the class. 
//New instances are created using the new keyword.
class Dog {
	//this constructor can also not take in any parameters, e.g.
	/*
	constructor() {
		this.title;
		this.author;
	}
	*/
  constructor(name) {
    this._name = name;  
  }
  
  introduce() { 
    console.log('This is ' + this._name + ' !');  
  }
  
  // A static method
  static bark() {
    console.log('Woof!');  
  }
}

const myDog = new Dog('Buster');
myDog.introduce();

// Calling the static method
Dog.bark();

//extends -> concept of inheritance, a child class can extend a parent class
//child classes have access to all of the instance properties and methods of the parent class
//they are also able to add in their own properties and methods

//to access the parent class's constructor, use super(arguments);
//to access the parent class's methods, use super.parentMethod(arguments);
// Parent class
class Media {
  constructor(info) {
    this.publishDate = info.publishDate;
    this.name = info.name;
  }
}

// Child class
class Song extends Media {
  constructor(songData) {
    super(songData);
    this.artist = songData.artist;
  }
}

const mySong = new Song({ 
  artist: 'Queen', 
  name: 'Bohemian Rhapsody', 
  publishDate: 1975
});

//importing javascript modules with the require function
var moduleA = require( "./module-a.js" );

// The .js extension is optional
var moduleA = require( "./module-a" );
// Both ways will produce the same result.

// Now the functionality of moduleA can be used
console.log(moduleA.someFunctionality)

//export default keyword
// in the js file module "moduleA.js"
export default function cube(x) {
  return x * x * x;
}

/*
There are many ways to use the import keyword, for example, you can import all the exports 
from a script by using the * selector as follows: import * from 'module_name';.

A single function can be imported with curly brackets as follows: import {funcA} as name from 'module_name';

Or many functions by name: import {funcA, funcB} as name from 'module_name';
*/

// In main.js
import cube from './moduleA.js';
// Now the `cube` function can be used straightforwardly.
console.log(cube(3)); // 27

//javascript promise object is used to handle async-await functions-> can be pending, resolved or rejected
//when the value is not yet available, the promise stays in the pending state
//if there are errors the promise may also go into the rejected state
const promise = new Promise((resolve, reject) => {
  const res = true;
  // An asynchronous operation.
  if (res) {
    resolve('Resolved!');
  }
  else {
    reject(Error('Error'));
  }
});

promise.then((res) => console.log(res), (err) => alert(err));

/* The .catch() method for handling rejection
The function passed as the second argument to a .then() method of a promise object is used when the promise is rejected. 
An alternative to this approach is to use the JavaScript .catch() method of the promise object. The information for the 
rejection is available to the handler supplied in the .catch() method.
*/
const promise = new Promise((resolve, reject) => {  
  setTimeout(() => {
    reject(Error('Promise Rejected Unconditionally.'));
  }, 1000);
});

promise.then((res) => {
  console.log(value);
});

promise.catch((err) => {
  alert(err);
});

/*
JavaScript Promise.all()
The JavaScript Promise.all() method can be used to execute multiple promises in parallel. 
The function accepts an array of promises as an argument. 
If all of the promises in the argument are resolved, the promise returned from Promise.all() 
will resolve to an array containing the resolved values of all the promises in the order of the initial array. 
Any rejection from the list of promises will cause the greater promise to be rejected.

In the code block, 3 and 2 will be printed respectively even though promise1 will be resolved after promise2.
*/
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(3);
  }, 300);
});
const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(2);
  }, 200);
});

Promise.all([promise1, promise2]).then((res) => {
  console.log(res[0]);
  console.log(res[1]);
});

/*
const loginAlert = () =>{
  alert('Login');
};

settimeout is an async javascript function that executes a certain code after a delay in milliseconds
setTimeout(loginAlert, 6000);
*/

// in this example, there are 3 functions to be executed in async Chaining them all together
promise.then(twoStars).then(oneDot).then(print);

/*
Resolving JavaScript Promises
When using JavaScript async...await, multiple asynchronous operations can run concurrently. If the resolved value is required for each promise initiated, Promise.all() 
can be used to retrieve the resolved value, avoiding unnecessary blocking.
*/
let promise1 = Promise.resolve(5);
let promise2 = 44;
let promise3 = new Promise(function(resolve, reject) {
  setTimeout(resolve, 100, 'foo');
});

Promise.all([promise1, promise2, promise3]).then(function(values) {
  console.log(values);
});
// expected output: Array [5, 44, "foo"]

/* 
Asynchronous JavaScript function
An asynchronous JavaScript function can be created with the async keyword before the function name, or before () when using the async arrow function.
 An async function always returns a promise.
 */
 function helloWorld() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('Hello World!');
    }, 2000);
  });
}

const msg = async function() { //Async Function Expression
  const msg = await helloWorld();
  console.log('Message:', msg);
}

/* OR without assigning to a variable
async function msg() {
  const msg = await helloWorld();
  console.log('Message:', msg);
}
*/

const msg1 = async () => { //Async Arrow Function
  const msg = await helloWorld();
  console.log('Message:', msg);
}

msg(); // Message: Hello World! <-- after 2 seconds
msg1(); // Message: Hello World! <-- after 2 seconds

//async function error handling
let json = '{ "age": 30 }'; // incomplete data

try {
  let user = JSON.parse(json); // <-- no errors
  alert( user.name ); // no name!
} catch (e) {
  alert( "Invalid JSON data!" );
}

/*
AJAX enables HTTP requests to be made not only during the load time of a web page but also anytime after a page initially loads. 
This allows adding dynamic behavior to a webpage. 
This is essential for giving a good user experience without reloading the webpage for transferring data to and from the web server.

The XMLHttpRequest (XHR) web API provides the ability to make the actual asynchronous request and uses AJAX to handle the data from the request.

The given code block is a basic example of how an HTTP GET request is made to the specified URL.
*/
const xhr = new XMLHttpRequest();
xhr.open('GET', 'mysite.com/api/getjson');

/*
The query string is separated from the original URL using the question mark character ?.

In a query string, there can be one or more key-value pairs joined by the equal character =.

For separating multiple key-value pairs, an ampersand character & is used.
*/
//HTTP GET Request
const req = new XMLHttpRequest();
req.responseType = 'json';
req.open('GET', '/myendpoint/getdata?id=65');
req.onload = () => {
  console.log(xhr.response);
};

req.send();

//POST request, is to send information to the server
//To make an HTTP POST request with the JavaScript XMLHttpRequest API, a request type, response type, request URL, request body, and handler for the response data must be provided. 
const data = {
  fish: 'Salmon',
  weight: '1.5 KG',
  units: 5
};
const xhr = new XMLHttpRequest();
xhr.open('POST', '/inventory/add');
xhr.responseType = 'json';
xhr.send(JSON.stringify(data));

xhr.onload = () => {
  console.log(xhr.response);
};

//In a Fetch API function fetch() the ok property of a response checks to see if it evaluates to true or false.
fetch(url, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
      'apikey': apiKey
    },
    body: data
  }).then(response => {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Request failed!');
  }, networkError => {
    console.log(networkError.message)
  })
}

//promise combined with fetch
fetch('url')
.then(
  response  => {
    console.log(response);
  },
 rejection => {
    console.error(rejection.message);
);

/* 
async await syntax
The async…await syntax is used with the JS Fetch API fetch() to work with promises. In the code block example we see the keyword async placed the function. This means that the function will return a promise. 
The keyword await makes the JavaScript wait until the problem is resolved.
*/
const getSuggestions = async () => {
  const wordQuery = inputField.value;
  const endpoint = `${url}${queryParams}${wordQuery}`;
  try{
const response = __~await~__ __~fetch(endpoint, {cache: 'no-cache'});
    if(response.ok){
      const jsonResponse = await response.json()
    }
  }
  catch(error){
    console.log(error)
  }
}