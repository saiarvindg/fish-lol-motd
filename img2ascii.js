// Dependencies
const imageToAscii = require("image-to-ascii");

// The path can be either a local path or an url
imageToAscii("/Users/saiarvind/Downloads/ahrichibicolor2.png",{
	reverse: true,
	size: {
		height: "50%"
	},
	pixels: " .,:;i1tf08@"
}, (err, converted) => {
    console.log(err || converted);
});

// Passing options
imageToAscii("/Users/saiarvind/Downloads/ahrichibicolor2.png", {
    colored: false,
    reverse: true,
    size: {
		height: "50%"
	},
}, (err, converted) => {
    console.log(err || converted);
});