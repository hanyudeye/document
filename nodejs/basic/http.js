var http = require('http');

http.createServer(function(request, response) {
    response.writeHead(200, {
        'Content-Type': 'text-plain'
    });

    // console.log(request.method);
    // console.log(request.headers);

    // console.log(response.method);

    response.end('Hello World\n');
}).listen(8124);
