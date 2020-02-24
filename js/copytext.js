function copyText(aim) {
    var copyDOM = document.getElementById(aim);
    // copyDOM.value='want to cope string'; //如果你想要直接复制字符串
    copyDOM.setSelectionRange(0, copyDOM.value.length);
    copyDOM.focus();
    document.execCommand("Copy");
    alert('复制成功！');
}
