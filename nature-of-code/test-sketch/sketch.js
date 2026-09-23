// const sketch = (p) => {
//   p.setup = () => {
//     p.createCanvas(400, 400);
//   };
//
//   p.draw = () => {
//     p.background(220);
//     p.circle(p.mouseX, p.mouseY, 50);
//   };
// };
//
// new p5(sketch);

class Walker {
  // Objects have a constructor where they are initialized.
  constructor() {
    // Objects have data.
    this.x = width / 2;
    this.y = height / 2;
  }


