var fs = require('fs')
var fileName = process.argv[2]

const fileContents = 'Writing to a file with Node.JS'

fs.writeFile(fileName, fileContents, (error, data) => {
	if(error){
		throw error;
	} else {
		console.log('File written successfully');
	}
})