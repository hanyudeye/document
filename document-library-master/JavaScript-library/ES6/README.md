ES6 小册
===
## 五 解构赋值

```js
// 对象的解构赋值
const obj = {
  a: 1,
  b: 2,
};
const {objA, objB, objC} = obj;
console.log(objA, objB, objC); // 1 2 undefined

// 数组的解构赋值
let a = 0, b = 1;
// 数组：swap
const c = a;
a = b;
b = c;
console.log(a, b); // 1 0
// 数组：结构赋值
const [d, e] = [b, a];
console.log(d, e); // 0 1

// 字符串的解构赋值
const str = 'abc';
const [str1, str2] = str;
console.log(str1, str2); // a b

// 数字的解构赋值
const [a1, b1] = 123;
// 报错：VM208:1 Uncaught TypeError: 123 is not iterable
// MDN：为了统一集合类型，ES6 标准引入了新的 iterable 类型，Array、Map 和 Set 都属于 iterable 类型。
```

## 六 展开运算符

```js
// 数组展开
const arr1 = [1, 2, 3];
const arr2 = ['a', 'b', ...arr1, 'c'];
console.log(arr2); // ['a', 'b', 1, 2, 3, 'c']

const [a, b, ...c] = arr;
console.log(a, b, c); // 'a', 'b', [1, 2, 3, 'c']


// 对象展开
const obj1 = {
  a: 1,
  b: 2,
};
const obj2 = {
  ...obj1,
  c: 3,
  d: 4,
};
console.log(obj2); // { a: 1, b: 2, c: 3, d: 4 }
```

##  新增函数拓展
> 代码 1：普通函数、箭头函数 以及 不定参

```js
// 普通函数
function fn1() {
  return ;
};

// 箭头函数
const fn2 = () => {
  return ;
};

const getSum = num => num *2;
console.log(getSum(10)); // 20

// 不定参 - rest 参数
const fn3 = (a, b, ...arg) => {
  console.log(a, b, arg);
};
fn3(1, 2, 3, 4); // 1 2 [3, 4]
```

> 代码 2：this 指向问题

```js
// this 指向问题
document.onclick = function() {
  console.log(this); // #document
};
document.onclick = () => {
  console.log(this); // Window
}
// 箭头函数本身没有 this，调用箭头函数的 this 时，指向是其声明时所在的作用域的 this。
```

> 代码 3：this 题目

```js
let fn;
let fn2 = function() {
  console.log(this);
  fn = () => {
    console.log(this);
  };
};
fn2(); // Window
fn(); // Window

fn2 = fn2.bind(document.body);
fn2(); // body
fn(); // body
```

> 代码 4：参数默认值

```js
const fn = (a = 10, b = 2) => {
  console.log(a * b); // 20
};
fn();
```

##  新增数组拓展
* `Array.from()`、`Array.of()`
* `find()`、`findIndex()`、`includes()`
* `flat()`、`flatMap()`
* `fill()`

将类数组转成数组：

> 代码 1：Array.from()

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <ul>
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li>4</li>
    </ul>

    <script>
      let liItems = document.querySelectorAll("ul li");
      let arr1 = [];
      const li1 = Array.from(
        liItems,
        function (item, index) {
          console.log(item, index, this);
          return index;
        },
        arr1
      );
      /*
        * <li>1</li> 0 []
        * <li>2</li> 1 []
        * <li>3</li> 2 []
        * <li>4</li> 3 []
      */
      console.log(li1); // [0, 1, 2, 3]

      const arr2 = [...liItems];
      console.log(arr2); // [li, li, li, li]
    </script>
  </body>
</html>
```

> 代码 2：Array.of()

```js
console.log(Array.of(1, 2, 3, 4, 'A')); // [1, 2, 3, 4, "A"]
```

> 代码 3：Array.isArray()

```js
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <ul>
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li>4</li>
    </ul>

    <script>
      let liItems = document.querySelectorAll("ul li");
      console.log(Array.isArray(liItems)); // false
      console.log(Array.isArray([1, 2, 3, 4])); // true
    </script>
  </body>
</html>
```

其他的不一一例举，可自行查看 MDN 文档。

## 新增对象拓展
> 代码 1：简洁表示法

```js
const a = 0, b = 1;
let obj1 = {
  a: a,
  b: b,
};
console.log(obj1); // {a: 0, b: 1}
let obj2 = {
  a,
  b,
};
console.log(obj2); // {a: 0, b: 1}
```

> 代码 2：属性名表达式

```js
const name = '小明';
const obj = {
  c() {
    console.log('a');
  },
  [name]: 18,
};
console.log(obj); // {c: ƒ, 小明: 18}
```

> 代码 3：Object.assign() 浅拷贝

```js
const obj1 = {
  a: 1,
  b: 2,
};
const obj2 = {
  c: 3,
  d: 4,
};
console.log(Object.assign({}, obj1, obj2)); // {a: 1, b: 2, c: 3, d: 4}
```

> 代码 4：Object.is 判断

```js
// 大致和三目运算符一致，但是有区别
console.log(+0 === -0);           // true
console.log(Object.is(+0, -0));   // false
console.log(NaN === NaN);         // false
console.log(Object.is(NaN, NaN)); // true
```

##  ES6 高级 - MVVM
原生 JavaScript 实现 Vue 中的 `{{ message }}` 需要考虑的内容：

1. 先区分文本节点还是标签节点。`{{ message }}` 或者 `<span>{{ message }}</span>` 或者其他。
2. 如果是单个文本，即文本内仅有一个 `{{ message }}`，那么我们可以正则匹配然后将其替换为传入的数据。
3. 如果是多个文本，即文本为 `{{ message }} - {{ name }}` 之类的格式，那么我们可以在上面条件的基础上，通过正则的 `match()` 方法匹配所有，然后逐个替换。
4. 如果是标签节点，即 `<div>{{ message }}</div>`（有可能里面还有更多嵌套），我们就需要考虑递归实现。

## 模板字符串

```js
let arr1 = '', arr2 = '';
let name = 'jsliang';
arr1 += 'Hello, my name is: ' + name;
arr2 += `Hello, my name is ${name}`;
```
