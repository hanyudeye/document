let fs = require('fs')

let dirs = fs.readdir('./', (err, data) => {
    // console.log(err)
   

})


let path=require('path')

console.log(path.basename("/home/aming/a.b"))
console.log(path.dirname("/home/wuming"))



