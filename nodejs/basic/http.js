// 简单的服务器

var http = require('http');

http.createServer(function(request, response) {
    response.writeHead(200, {
        'Content-Type': 'text-plain'
    });

    // console.log(request.method);
    // console.log(request.headers);

    // response.write("");
    con
    response.end('Hello World\n my name is aming\n');
}).listen(8888);
