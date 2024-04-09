#!/usr/bin/node

const factorial = (n) => {
  if (isNaN(n)) {
    console.log(1);
  } else if (n === 0 || n === 1) {
    console.log(1);
  } else {
    console.log(n * factorial(n - 1));
  }
};

const [,,arg] = process.argv;
factorial(parseInt(arg));
