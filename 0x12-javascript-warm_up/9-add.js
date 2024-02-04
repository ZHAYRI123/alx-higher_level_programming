#!/usr/bin/node
const arg = parseInt(process.argv[2]);
const arg1 = parseInt(process.argv[3]);
function add(a, b){
	return a + b;
}
if (isNaN(arg)){
	console.log(NaN);
}
else if (isNaN(arg1)){
	console.log(NaN);
}
else{
	console.log(add(arg, arg1))
}
