my_car = {
  color: 'red',
  drive:  () => {
    console.log("I'm driving");
  }
}

jehads_car = {
  color: 'black',
  drive:  () => {
    console.log("I'm driving");
  }
}

monas_car = {
  color: 'white',
  drive:  () => {
    console.log("I'm driving");
  }
}

function Car(color) {
  this.color = color
}

Car.prototype.drive = function () {
  console.log("I'm driving");
}

adhams_car = new Car('hotpink')
abds_car = new Car('lighting_blue')

/*
Don't
Repeat
Yourself
*/

// Prototypal OOP
// Javascript

// Classical OOP
/**
 * C++
 * Java
 * C#
 * PHP
 * Python
 * 
 */

class Hotel {

  constructor(stars, name) {
    this.stars = stars
    this.name = name
  }

  book_stay() {

  }

}

my_hotel = new Hotel(5, "The Thornhill")