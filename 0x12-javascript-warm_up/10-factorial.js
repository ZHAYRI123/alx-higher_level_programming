#!/usr/bin/node
const arg = parseInt(process.argv[2]);
let fact = 1;
if (isNaN(arg))
{
	console.log("1");
}
else
{
	for(i = 1; i <= arg; i++)
	{
		fact = fact * i;
	}
	console.log(fact);
}
