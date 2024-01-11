#!/usr/bin/node
const arg = parseInt(process.argv[2]);
let i = 0;
if (isNaN(arg)){
	console.log("Missing number of occurrences");
} else if (arg > 0){
	while (i < arg){
		console.log("C is fun");
		i++;
	}}

