/**
 * 统计字符串中的单词数目
 *    统计字符串中单词的数目，更复杂的话从一个文本中读出字符串并生成单词数目统计结果。
 */
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: '>>>'
});

rl.prompt();

rl.on('line', line => {
  console.log(`<<< ${line}\n${wordCount(line)}`);
  rl.prompt();
}).on("close", () => {
  console.log('');
  console.log('<<< process exit 0');
  process.exit(0);
});

function wordCount(line){
  let obj = {};
  let arr = line.split(' ');
  arr.forEach(item => {
    obj.hasOwnProperty(item)? obj[item] ++ : obj[item] = 1
  });
  // return obj;
  let retD = '';
  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      retD += `${key} ==> ${obj[key]}\n`;
    }
  }
  return retD;
}