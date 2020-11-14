const MarkdownIt = require("markdown-it");
md = new MarkdownIt();
const result = md.render("# markdown-it rulezz!");
console.log(result);
