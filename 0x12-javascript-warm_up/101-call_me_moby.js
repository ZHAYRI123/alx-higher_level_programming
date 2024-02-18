#!/usr/bin/node
exports.cammMeMoby = function (x, theFunction) {
	while (x > 0) {
		theFunction();
		x--;
	}
};
