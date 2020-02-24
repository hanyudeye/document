// var http=require('http');

// http.createServer(function (request, response) {
//     response.writeHead(200, { 'Content-Type': 'text-plain' });
//     response.end('Hello World\n nice to meet you ');
// }).listen(8124);

// console.log(process.argv);


// let aa =require('./module.js');
// aa.sayHello()

let p=require('path');
let r=p.basename("/home/wuming/abck")
console.log(r)
