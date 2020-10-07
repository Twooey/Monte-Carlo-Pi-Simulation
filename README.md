This is just a very basic Pi generator. There isn't a real reason to use it other then for fun, and as a learning
experience. I am using anaconda and numba to parallelize  it so you can process a larger amount of random numbers, 
and get a more accurate estimate of Pi. 

The principal is quite simple. We know the radius of the Circle is 1. This we can calculate the hypotenuse of any one
point, and find if it is inside, or outside of the circle.  The ratio of points inside of the circle (times 4) divided 
by total points will give you a reasonable estimate of Pi, as we know the ratio to of an area of a square, to the area 
of a circle is pi / 4.

In Theory, the more points used, the more accurate your value will be, but as it is random, this is not always the case.
