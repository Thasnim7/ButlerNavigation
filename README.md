# ButlerNavigation
# Goat Robotics ROS2 Task – Navigation Demo

This package is created for the ROS Developer task at Goat Robotics Pvt Ltd.

It controls a TurtleBot3 in Gazebo and makes it deliver orders to 7 tables using Nav2.

---

## 💻 How to Run

👉 Terminal 1:

export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

👉 Terminal 2:

export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=true

👉 Terminal 3:

ros2 run butler_nav butler_node

To send an order:

ros2 topic pub --once /order_request std_msgs/String "data: 'table1'"
ros2 topic pub --once /order_request std_msgs/String "data: 'table2'"
ros2 topic pub --once /order_request std_msgs/String "data: 'table3'"
ros2 topic pub --once /order_request std_msgs/String "data: 'table4'"
ros2 topic pub --once /order_request std_msgs/String "data: 'table5'"
ros2 topic pub --once /order_request std_msgs/String "data: 'table6'"
ros2 topic pub --once /order_request std_msgs/String "data: 'table7'"

video link:
https://drive.google.com/file/d/1h73T5lp-wDDs-HTNHUmN228zo9yhjexV/view?usp=drive_link
https://drive.google.com/file/d/1hFsvRa_5Nbl5r1_B2ORdQMZAXRhDPLNF/view?usp=drive_link
 
  Made by **Thasnim Rihana S**

 
