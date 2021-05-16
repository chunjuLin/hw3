# hw3
(1) how to setup and run your program 

This homework can be seperate into two part. The first part is the Gesture ui mode. The second one is the 
Tilt angle mode. In the main function we seperate the same RPC loop , and each mode is controlled by the 
RPC function that I define. I start each thread at the begining of the main function.

Gesture-ui mode

I use a variable to control the start and end of the thread. In the Gesture_ui mode, we put the ML function
 inside the thread. The ML function will judege wheather the we should add the threshold angle or not. If 
the detection of the gesture mode is 0 we add the gestur angle. If the gesture mode is 1 decrease the gesture 
angle. 

Tilt angle mode

in the tilt angle mode, we first get 10 value of the horizontal acceleration of the board to be the initalization
after that we keep detecting the angle by math calculation. If the angle of the board is bigger than thershold angle
we print it on the screen. If we get ten larger angle. We use the mqtt function to send a message to python. Python 
will print the PRC call on the screen to terminate the Tilt_angle mode. 

(2) what are the results

We can see that we first call the RPC function in the screen. We use the user button to confirm the result. After we 
confirm the result. It will terminate the RPC function. Later on we can call the Tilt_angle mode. After we move the board
It will show the angle if it is bigger than thershold. After 10 data, The python will terminate the Tilt_angle mode.
