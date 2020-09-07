/**
 * 拉丁猪文字游戏
 *    这是一个英语语言游戏。基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay（譬如“banana”会变成“anana-bay”）。可以在维基百科上了解更多内容。
 */

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: '>>>'
});

rl.prompt();

rl.on('line', line => {
  console.log(`<<< ${pigLatin(line)}`);
  rl.prompt();
}).on("close", () => {
  console.log('');
  console.log('<<< process exit 0');
  process.exit(0);
});

function pigLatin(word){
  if(word.toLowerCase().startsWith('a') ||
  word.toLowerCase().startsWith('e') ||
  word.toLowerCase().startsWith('i') ||
  word.toLowerCase().startsWith('o') ||
  word.toLowerCase().startsWith('u'))  return word;
  let [_word,w] = [word[0]+'-',word.slice(1)];
  return w+_word+'ay'
}