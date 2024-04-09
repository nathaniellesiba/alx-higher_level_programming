#!/usr/bin/node
/*print 2 arguments*/
const [, , arg1, arg2] = process.argv;
console.log(`${arg1} is ${arg2}`);
