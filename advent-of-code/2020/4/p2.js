var fs = require('fs');

var isValid = (passport) => {
    let store = new Map();
    passport.forEach((kv) => {
        store.set(kv[0], kv[1]);
    });

    let byr = store.get("byr");
    if (byr.length != 4 || parseInt(byr) < 1920 || parseInt(byr) > 2002) return false;

    let iyr = store.get("iyr");
    if (iyr.length != 4 || parseInt(iyr) < 2010 || parseInt(iyr) > 2020) return false;

    let eyr = store.get("eyr");
    if (eyr.length != 4 || parseInt(eyr) < 2020 || parseInt(eyr) > 2030) return false;

    let hgt = store.get("hgt");
    if (hgt.slice(hgt.length-2, hgt.length) == "cm") {
        if (parseInt(hgt.slice(0, hgt.length-2)) < 150 || parseInt(hgt.slice(0, hgt.length-2)) > 193) return false;
    } else if (hgt.slice(hgt.length-2, hgt.length) == "in") {
        if (parseInt(hgt.slice(0, hgt.length-2)) < 59 || parseInt(hgt.slice(0, hgt.length-2)) > 76) return false;
    } else return false;

    let hcl = store.get("hcl");
    if (hcl.length != 7) return false;
    if (hcl[0] != "#") return false;
    for (var i = 1; i < hcl.length; i++) {
        if (hcl.charCodeAt(i) < 48 || hcl.charCodeAt(i) > 102 || (hcl.charCodeAt(i) > 57 && hcl.charCodeAt(i) < 97)) return false;
    }

    let ecl = store.get("ecl");
    let eclOptions = new Set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    if (!eclOptions.has(ecl)) return false;

    let pid = store.get("pid");
    if (pid.length != 9) return false;

    return true;
}
 
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
    if (isValid(passports[i])) validCount++;
}

console.log(validCount);