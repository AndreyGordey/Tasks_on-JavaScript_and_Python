let fizzBuzz = 100;

for (let i = 1; i <= fizzBuzz; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log('FizzBuzz'); // Если число делится и на 3, и на 5
    } else if (i % 3 === 0) {
      console.log('Fizz'); // Если число делится только на 3
    } else if (i % 5 === 0) {
      console.log('Buzz'); // Если число делится только на 5
    } else {
      console.log(i); // Если не делится ни на 3, ни на 5
    }
  }
  