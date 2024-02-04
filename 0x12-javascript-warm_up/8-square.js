#!/usr/bin/node
const arg =parseInt(process.argv[2]);
if (isNaN(arg))
{
	console.log("Missing size");
} else if (arg > 0)
{
	let i = 0;
	let j = 0;
	let li = '';
	while (i < arg)
	{
		while (j < arg)
		{
			li = li + 'X';
			j++;
		}
		console.log(li);
		i++;
	}}
