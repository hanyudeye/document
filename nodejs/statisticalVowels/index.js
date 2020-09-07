/**
 * 统计元音字母
 *    输入一个字符串，统计处其中元音字母的数量。更复杂点的话统计出每个元音字母的数量。
 */

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: '>>>'
});

rl.prompt();

rl.on('line', line => {
  console.log(`<<< ${vowels(line)}`);
  rl.prompt();
}).on("close", () => {
  console.log('');
  console.log('<<< process exit 0');
  process.exit(0);
});

function vowels(str){
  let obj = {};
  for (const char of str) {
    if (char !== undefined){
      switch (char.toLowerCase()) {
        case 'a':
          obj.hasOwnProperty('a')? obj['a'] += 1 : obj['a'] = 1;
          break;
        case 'e':
          obj.hasOwnProperty('e')? obj['e'] += 1 : obj['e'] = 1;
          break;
        case 'i':
          obj.hasOwnProperty('i')? obj['i'] += 1 : obj['i'] = 1;
          break;
        case 'o':
          obj.hasOwnProperty('o')? obj['o'] += 1 : obj['o'] = 1;
          break;
        case 'u':
          obj.hasOwnProperty('u')? obj['u'] += 1 : obj['u'] = 1;
          break;
      }
    }
  }
  return JSON.stringify(obj);
}