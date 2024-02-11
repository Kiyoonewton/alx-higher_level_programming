#!/usr/bin/env node
for (let i = 2; i < 10; i++) {
  for (let x = 0; x < i; x++) {
    if (x % i === 0) {
      console.log(i + "equals" + x + "*" + Math.floor(i / x));
      break;
    }
  }
  console.log(i + "is a prime number");
}
