# Object-Detection
2 projects in 1 :). This repository contains a project that can move the mouse on the screen based on detection of a green-ball and another that helps a robot to search for the same ball and manipulate it.

--- All the credits for creating the neuronal network using Tensorflow goes to EdjeElectronics (https://github.com/EdjeElectronics) ----
--- In order to get the setup done for using this files please follow his instructions. All the files that I used can be found to this link:
https://drive.google.com/drive/folders/1WDJoUwIfUMR8nTXbrSvj6A3ClLjOprNV ---
--- This repository contains only the code for the 2 projects and video demonstrations ---
--- You can find my frozen inference graph and all the pictures that I used for training this model to the link mentioned above ----
1. First project is based on detecting a ball, getting its coordinates and moving the mouse based on that detection. The mouse is useless in this project :)
The project is under path: "models\research\object_detection" and the filename is Object_detection_MOUSE.py

2. The second project is also my bachelor thesis and it works like this:
- a robot it's taking frames from the room where it is and it's sending those frames to a laptop
- the laptop is analaizing the frames that has been received and it tries to see if the ball has been detected or not
- the laptop is sending a message with "left", "right", "forward", etc. to the robot
- based on the message the robot is moving in order to achieve its finall mission (grabbing the green ball)
- after having the ball, a GUI will appear so a person can manipulate the robot

This is a program based on server-client where the robot is the client and the laptop is the server

The project is under path: "models\research\object_detection" and the filename is "Object_detection_Streaming (SERVER).py" for the server side and for the client side, in the same path, the name is: "Object_detection_CLIENT.py"

A video of how the projects work is included in the "models\research\object_detection" file ("Robot controlled using a GUI" and "Robot searching for its ball" are the videos for the second project and "Mouse movement based on object detection" and "Playing a game with mouse movement" - videos for the first project)
