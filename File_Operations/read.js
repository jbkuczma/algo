var fs = require('fs')
var fileName = process.argv[2]

if(process.argv.length < 3){
	console.log('Provide a file path');
	process.exit(1);
}

fs.readFile(fileName, 'utf-8', (error, data) => {
	if(error){
		throw error;
	} else {
		console.log(data);
	}
})

/***

	node read.js read.txt

	prints:
		This
		is
		a
		test
		file
		
***/