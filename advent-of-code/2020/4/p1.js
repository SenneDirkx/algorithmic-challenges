var fs = require('fs');
 
var passports = fs.readFileSync('./input.txt').toString().split("\n\n");

var validCount = 0;

for (var i = 0; i < passports.length; i++) {
    passports[i] = new Set(passports[i].split(/[\s,]+/).map(kv => kv.split(":")));
    if (passports[i].size < 7) continue;
    if (passports[i].size == 7) {
        var containsCid = false;
        passports[i].forEach((kv) => {
            if (kv[0] == "cid") containsCid = true;
        })
        if (containsCid) continue;
    }
    validCount++;
}

console.log(validCount);