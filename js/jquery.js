// 启动代码
$(function(){

    $("p").click(function(){
        $(this).css("background","yellow");
    })

    $("p").css("background","red");
    $("p").append('<p>Hello</p>');
})
