## Simulating collisions in my physics sim

In my last blog post I tried to make a simulator that will drop a ball and accelerate it with gravity in mind.

However these balls don't stop for anything or anyone and they will keep falling until I kill the program. So I need to add some sort of collision logic that will let the balls interact with the edges of the screen and with each other and maybe even other objects.

But how?

To be honest while building this I had a feeling that my math was wrong, especially the way I applied acceleration to the motion vectors.

## References:
[The Nature of Code](https://natureofcode.com/random/)


# New Blog:

## Solution:
- Calculate a point of intersection between the line of motion of the ball and the wall.
- At every update point, check if we have moved beyond the point. If we have, take the distance between the initial position and the point of intersection and subtract it from the distance you would have travelled to get the remaining distance the ball should have travelled in that time frame and flip the relevant velocity component and move the remaining distance in the new direction? Best idea I have for now.


## Problems:
- Different speeds. Not something to be concerned about with walls.

## Modelling the solution with code:
Now I need to be able to actually make this work in code.
- Should first store the lines of motions of every object.
 - To make things easier we will just take the lines from each object and compare them to the lines for the walls for now.
- We'll add them all to a dict with the class object as a key. And for now we'll make a new list that will have the equations of the walls.
- We'll then solve the equations and check for a solution. If we do find one, we add that to the list of collision points.
- We should add them to a 

## Adding equations to my code:
- A line equation follows: 
~~~
y = mx + c
~~~
- So we'll store it in a dictionary like this:
~~~python
line1={'m':<value>,'c':<value>}
~~~

- Then when we have 2 lines we can solve for y and x using this:
~~~python
int_x = (l1['c'] - l2['c']) / (l1['m'] - l2['m'])
int_y = (l1['m'] * int_x) + l1['c']
~~~

## Problem with this:
- Vertical lines cannot be represented in the form of `y = mx + c`, so cant really use code to solve them like that.

- Proposed fix is to use the General Form of representing lines:
~~~
Ax + By + C = 0
~~~

## Parametric Equations
- Best way to really talk about this one is to explain what we need to use this and what we'll be calculating with this expression.
- We start with a point and direction vector. We assume that this point and the vector are both on a line that for our use case the ball will travel on.
- We can then use that to calculate any other point on that line by adding the vector to the initial point while multiplying it with some magnitude. 
- So the way I understood it:
~~~
p=p0+t(d)
~~~
- Where:
  - p is the new point.
  - p0 is the initial point.
  - t is the magnitude.
  - d is the direction vector.

### Solving Parametric Equations:
- Solving them will also follow the same rules, we have 2 equations like so:
~~~
p=p0+t(d1)
q=q0+s(d2)
~~~
Now if we need to check for the lines intersecting we need to equate them to each other so,
If p and q are the same point let's say (x,y) we can then say that:
~~~
x=px+t(d1x)=qx+s(d2x)
y=py+t(d1y)=qy+s(d2y)
~~~
I'm running out of ideas on what to call these variables so ignore the names.

### Code with these equations?
- Now I need to figure out a way to store these equations in code and solve them.
- First let's figure out what values we have and what values we need to calculate.
  - Each line will have 2 equations that we'll store. One for the abcissa and one for the ordinate.

- Ended up making a class for Points, Vectors and Parametric Lines.

- Ended up using Cramer's method to create an algorithm to solve two Parametric equations. 

- Calculations work. And we tested it by drawing lines to the left wall.

### Conclusion
Parametric lines work.

## Testing this out to calculate wall only collisions:
### First I want to calculate which wall the ball will collide with first. 
- To do this I should probably start with creating a similar class for Lines. Just like what we did for Circles.
- So I'll start with initialising all of the necessary values needed to start with the creation of a line and then I'll make methods to draw the line and figure the rest out later on. 

- So now when I create a Parametric line, it basically uses the `Line Class` as an object for it's line. I understand that this is a little stupid when it comes to abstractions but this feels a little neater.
