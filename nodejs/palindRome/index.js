/**
 * 判断是否为回文
 *    判断用户输入的字符串是否为回文。回文是指正反拼写形式都是一样的词，譬如“racecar”。
 */

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: '>>>'
});

rl.prompt();

rl.on('line', line => {
  console.log(`<<< ${line} ${palindRome(line)? '是回文' : '不是回文'}`);
  rl.prompt();
}).on("close", () => {
  console.log('');
  console.log('<<< process exit 0');
  process.exit(0);
});

function palindRome(str){
  let len = str.length;
  for (let i = 0; i < len; i++) {
    if(str[i] !== str[len-1-i]) return false;
  }
  return true;
}