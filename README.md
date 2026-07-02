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
I tried to search this up. The stuff I found was a little scary. This stuff is understandably really complicated, and it's gonna take a long time to actually make something that works. I did find a book that I'll probably go through and see if it helps, [Computer Graphics by Gabriel Gambetta](https://gabrielgambetta.com/computer-graphics-from-scratch/index.html). But we should definitely use a pre existing graphics software or library for now. I think instead of matplotlib I'll use Pygame. At least give it a shot because matplotlib seems to be more complex.  

I ended up on the [Pygame docs front page](https://www.pygame.org/docs/index.html), which contained a quick start program. The program was basically a circle on a blank window, that you can control with WASD. I ended up using this code as a base. Basically it had everything I needed to get started with Pygame. It showed me how to make the window, add a background to it, make a circle, position it on the window and move the circle. The only thing I needed to add to it was replace the WASD controls with the displacement calculations from the Kinematic Equations and continuously update the y-axis position of the ball.  

The next steps involved tinkering with the program. I changed some of the values on the ball's starting position and figured out that the top left corner of my screen was the origin of the entire window (0,0). I adjusted the position of the ball to start close to the top of the window. Now I need to make it fall. My implementation of the kinematic equation is to calculate the distance it would travel from rest in a given time frame. So I decided to just update the y-axis position continuously with the new value.  
In the quick start program they have a variable called `dt`. The value for `dt` from what I understand is basically the time between frames. In this case it's 0.016 seconds. So I calculate how far the ball would have travelled after every multiple of 0.016 seconds. So the distance it travels after 0.016 seconds then after 0.032 seconds, and so on. A slight problem with this is that we are basically adding the value of `dt` after every `dt` seconds and calculating the position of the ball at that compounded total time. I know the way I'm explaining this might not make sense so I'll plug the code I have here:
~~~python
import pygame

G = 9.81


def calculate_position(time: float):
    # time in seconds
    dis = 0.5*G*(time**2)
    return dis  # How much of the 1000 meters it has fallen


def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    time = 0
    line_left = [0, screen.get_height()-100]
    line_right = [screen.get_width(), screen.get_height()-100]

    player_pos = pygame.Vector2(screen.get_width()/2, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('black')

        pygame.draw.circle(screen, 'white', player_pos, 5)
        pygame.draw.line(screen, 'white', line_left, line_right, 5)

        pygame.display.flip()
        if player_pos.y < screen.get_height()-110:
            print(player_pos.y)
            player_pos.y = calculate_position(time)
        dt = clock.tick(60)/1000
        time += dt
    pygame.quit()


if __name__ == '__main__':
    main()
~~~

The was a rough attempt to try stuff out. I'm just adding and changing values here and there to see how it affects the stuff on the display window. I also tried to add a line to the window and it worked.  

Now this rough implementation was successful, the ball falls at an accelerating pace until it goes out of the bounds of the window. So it works.

After this I tried to clean up the code and make it more useable. While doing that I was trying to think of a way to make the calculations of the ball's movement more dynamic.  

Basically I want the ball to maintain it's own state separately. This should also be true for any other objects that will be added to the simulation. Next, pygame will poll all available objects for their current state. Each object, our ball in this case will be told that it should calculate it's next state. In the case of our ball, it should use it's current state to calculate what the it's next state in the given time frame should be. This time frame will be given to it by pygame. It should then tell pygame how and where it should be moved.  

But to make this happen I need to separate the creation logic for objects from pygame's screen loop.  
What I ended up doing is make a function that adds any object I want to create to a list. This will have the necessary details for each object that are required to make them, so for a circle it will be the position of the center, for a line it will be the coordinates of each end, and so on.  
And now I'll have to create something that will detect what I want to create and call the necessary function for me, but for now this list is designed to only accept circles. So pygame polls this list and creates 'n' circles for us. 
