#!/usr/bin/node
const arg = parseInt(process.argv[2]);
function fact(a)
{
	let f = 1;
	for(i = 1; i <= a; i++)
        {
                f = f * i;
        }
	return f;
}
if (isNaN(arg))
{
	console.log("1");
}
else
{
	console.log(fact(arg));
}
