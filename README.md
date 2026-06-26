## Ball???

I want to try to simulate some physical phenomenon using code. The first thing that came into my mind was simulate a Black Hole. I did once see a video of someone doing this using C and that was a little insane. I need to work my way to that point so I thought why not just start with simulating a ball falling from some height. This is my documentation of doing this??

## The Display
The first thing I need to understand is how will I display this? The equation of a ball falling is simple enough, I just need to start at 0 velocity and increase the speed of the ball by 9.81 meters per second (value for the acceleration due to gravity). My knowledge of physical equations right now is pretty shit. I have forgotten way too much to be doing this blind. I'm about 99% sure that the only thing I need to account for right now is the ball's acceleration. If I'm wrong we'll find out pretty soon. 

So assuming the math is right, I can calculate where the ball will be at each second, when dropping the ball at some height called `h`. But I also want to be able to display it on my screen. I have no clue how it's possible. 

So off to google we go. I managed to find a bunch of people vouching for numpy and matplotlib. I can sort of understand, using a matrix as my 2D space to run these simulations and I guess people can use matplotlib to see the grid in a UI of sorts? By plotting the positions onto a graph? I'll have to look into this. 

The second method was to use PyGame. This was not mentioned too often but it was the first thing that came to my mind. However, I think I'll try out the numpy and matplotlib method first. 

## Numpy and Matplotlib
I did use numpy a long time ago, but naturally as always I have forgotten practically everything. In fact the only reason I even used it in the first place was when I was transitioning from C++ to Python, I found the flexibility of lists stupid (for some weird reason???) and wanted to bring back arrays to mess with my head (again no clue why??) and numpy gave me that freedom (once again why did I want this?). I should stop hating on my past self he must have had a good reason for doing what he did. 

But first let me actually understand what people mean when they say use numpy and matplotlib to simulate these things.  
I ended up asking Claude for this, when I googled this I mainly found stack overflow posts of people trying to fix problems in their code and everyone was trying to simulate some far more complicated stuff or basically graph paths of objects? Which is also not what I wanted. But apparently mathplotlib has animation capabilities, which might work. We won't know unless we try.  

## Starting off
I started by just making a code that will calculate the distance the ball travels in `t` seconds using the kinematic equation for displacement: 

~~~math
s=ut+0.5a(t^2)
~~~

This will calculate the distance travelled by the ball at any time `t` in seconds. Since we know that the value of `u` is 0 and the value of `a` is the acceleration due to gravity which is `9.81`.

Now I need to be able to display this in some way. 

After looking into what matplotlib is used for vis-a-vis animations, I mean it might do the job? It's all pretty complicated for me because I have never used matplotlib (called `plt` from now on) before.  

But if I'm being honest I also wanted to figure out how these GUI display thingies are built. Now if I want to make more complex simulation stuff, I probably will want to use some existing libraries or software, but let's just give making our own display application thingy (I don't know what to call it) a try.  

But where do I start?

## Display Window

