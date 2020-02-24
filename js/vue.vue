// 组件
Vue.component('todo-item', {
props: ['todo'],
template: '<li>{{ todo.text }}</li>'
})


Vue.component('todo-item1', {
template: '<li>这是个待办项</li>'
})

var Child={
template: '<div>局部组件定义</div>'
}

const app=new Vue(
{
el:'#app', 
data:{
message:'Hello Vue',
movies:['longzhu','xingji','chuanyue'],
counter:0,
groceryList: [
{ id: 0, text: '蔬菜' },
{ id: 1, text: '奶酪' },
{ id: 2, text: '随便其它什么人吃的东西' }
]

},
methods:{
add:function(){
this.counter++;
},
min:function(){
this.counter--;
}
},
created: function () {
// `this` 指向 vm 实例
console.log('生命周期钩子');
},
computed:{
msg:function(){
return this.message + " fuckyou !";
}
},
components:{
'local-components':Child
}
})
