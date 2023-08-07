# Additional Resources in Autonomous Navigation
>## __Husky Tutorials__
>>To work with the Husky robot in the next tutorials we will first have to install some packages. These are 3 packages you need.
>>```bash
>>$ sudo apt-get install ros-<distro>-husky-navigation
>>$ sudo apt-get install ros-<distro>-husky-gazebo 
>>$ sudo apt-get install ros-<distro>-husky-viz
>>```
>>In your first terminal open up the Gazebo world:
>>```bash
>>$ roslaunch husky_gazebo husky_playpen.launch
>>```
>>In the second terminal open up Rviz with the Clear-path configuration:
>>```bash
>>$ roslaunch husky_viz view_robot.launch
>>```
>>In your third terminal start off gmapping.
>>```bash
>>$ roslaunch husky_navigation gmapping_demo.launch
>>```
>>Now, use 2D Nav Goal tool in the top toolbar to select a movement goal in RViz. 
>>To save the generated map, you can run the map_saver utility:
>>```bash
>>$ rosrun map_server map_saver -f <filename>
>>```
>## __TurtleBot3__
>>The following Tutorials teach you how to work with it. They concepts should be familiar to you by know; however, they may want to try more advanced projects.
>>- [Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#simulation) which will get you started with the TurteBot3 in Gazebo
>>- [Autonomous Driving](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#autonomous-driving) where you will have racing tutorials.
>>- [Videos](https://emanual.robotis.com/docs/en/platform/turtlebot3/videos/#videos) to get you inspired by project other did
>>- [Machine Learning](https://emanual.robotis.com/docs/en/platform/turtlebot3/machine_learning/#machine-learning)
>## __Reading__
>>This is a list of topics to read about in case you are interested in the theory behind what you learned.
>>>__SLAM__
>>>>- EKF SLAM
>>>>- Graph SLAM
>>>>- Occupancy Grid SLAM

>>>__Localisation__
>>>>- Markov localization
>>>>- Grid Localization
>>>>- Monte Carlo Localization

>>>__Path Planning__
>>>>- A* search
>>>>- D* search
>>>>- Probabilistic roadmap
