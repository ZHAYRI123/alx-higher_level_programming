#!/usr/bin/node
if (process.argv.length > 1) {
	let max  = 0;
	let Sec_max = 0;
	for (let i = 2; i < process.argv.length; i++) {
		if (max > parseInt(process.argv[i]) && Sec_max < parseInt(process.argv[i])){
			Sec_max = parseInt(process.argv[i]);
		}
		else if (max < parseInt(process.argv[i])){
			Sec_max = max;
			max = parseInt(process.argv[i]);
		}
	}
	console.log(Sec_max);
}
else {
	console.log(0);
}
