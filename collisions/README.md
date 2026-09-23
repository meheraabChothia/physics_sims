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

## Making Collisions happen:
- Need to explain the problem first.
- The solution I have though of. 

The solution:
So each object in motion will have a line of motion. We should test this out in a field that has no gravity pulling things down. So a ball thrown in a direction will continue travelling in that direction unless stopped or otherwise coerced. At any point of time we can check to see if any 2 lines of motion will intersect. And calculate the exact moment those 2 objects will hit each other from that point, we'll have to calculate an offset value where the size of the object will alter the exact point of contact with the other object. This is because the intersection point we calculate is the point where their centers will collide. But if 23 have 2 balls each with a radius of say 2 pixels, the point of contact between them will be will be different (Math behind this will have to be figured out.)


- Problems:
- Different speeds.

