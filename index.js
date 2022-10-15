// https://github.com/lydiahallie/javascript-questions

function sayHi() {
    console.log(name);
    console.log(age);
    var name = 'Lydia';
    let age = 21;
  }
sayHi();

//-----
for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 1);
  }
  
for (let i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 1);
}

//----
const shape = {
    radius: 10,
    diameter() {
      return this.radius * 2;
    },
    perimeter: () => 2 * Math.PI * this.radius,
  };
  
  console.log(shape.diameter());
  console.log(shape.perimeter());

//-----
+true;
!'Lydia';

//-----
const bird = {
    size: 'small',
  };
  
const mouse = {
  name: 'Mickey',
  small: true,
};

// console.log(mouse.bird.size);
console.log(mouse[bird.size]);
console.log([bird["size"]]);

//-----
let c = { greeting: 'Hey!' };
let d;

d = c;
c.greeting = 'Hello';
console.log(d.greeting);

//-----

//-----

//-----

//-----

//-----

//-----