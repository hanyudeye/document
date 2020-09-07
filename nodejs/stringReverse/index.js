/**
 * 逆转字符串
 *    输入一个字符串，将其逆转并输出。
 */
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: '>>>'
});

rl.prompt();

rl.on('line', line => {
  console.log(`<<< ${line.split('').reverse().join('')}`);
  rl.prompt();
}).on("close", () => {
  console.log('');
  console.log('<<< process exit 0');
  process.exit(0);
});