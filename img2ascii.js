// Dependencies
const imageToAscii = require("image-to-ascii");

// The path can be either a local path or an url
var pic = "/Users/saiarvind/Downloads/ahrichibicolor2.png";

var image = new art.Image({
	filepath: pic,
	alphabet: variant1
});

image.write(function(err, rendered) {
	console.log(rendered);
});

/*
imageToAscii(pic,{
	//reverse: true,
	//bg: true,
	//fg: false,
	//pixels: " .,:;lITt",
	size_options: {
		px_size: {
			width: 2,
		},
		screen_size: {
			width: 20,
			height: 20
		}
	}
}, (err, converted) => {
    console.log(err || converted);
});
*/

// Passing options
// imageToAscii(pic, {
//     colored: false,
//     reverse: true,

// }, (err, converted) => {
//     console.log(err || converted);
// });