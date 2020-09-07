// 方法集合

// 内部对象
// 无穷 Infinity
const infinity = () =>{
    var maxNumber= Math.pow(10,1000);
    if(maxNumber== Infinity){
        console.log("maxNumber is Infinity\n");
    }
    console.log(1/maxNumber);
}

// infinity()

// nan 是否可转换为数字型 NaN
const nan =() =>{
    console.log(isNaN('1'));
    console.log(isNaN("22.3"));
    console.log(isNaN("Hl"));
}

// nan()

// undefined 未定义'值'就使用
const undefineds=(x)=>{
    if(x===undefined){
        return "Undefined value!";
    }
    return x;
}

// var y;
// console.log(undefineds(y))



// Write a function identity that takes an argument and returns that argument
//原味输出输入的参数
const identity = (x) => x;

