# 2D-Occupancy-Grid-Map_Intel-Unnati
For Intel Unnati for the problem statement: Develop a 2D Occupancy Grid Map of a Room using Overhead Cameras by Team Phoenix, rom Nitte Meenakshi Institute of Technology


sudo apt update
sudo apt upgrade
sudo apt install xserver-xorg-video-amdgpu
# In new terminal - Install ros2 on pc
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros2_foxy.sh
sudo chmod 755 ./install_ros2_foxy.sh
bash ./install_ros2_foxy.sh

# New terminal again - install dependent ros2 packages
sudo apt-get install ros-foxy-gazebo-*
sudo apt install ros-foxy-cartographer
sudo apt install ros-foxy-cartographer-ros
sudo apt install ros-foxy-navigation2
sudo apt install ros-foxy-nav2-bringup

# Install turtlebot3 packages
source ~/.bashrc
sudo apt install ros-foxy-dynamixel-sdk
sudo apt install ros-foxy-turtlebot3-msgs
sudo apt install ros-foxy-turtlebot3

export TURTLEBOT3_MODEL=waffle_pi

mkdir –p ~/turtlebot3_ws/src
git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/turtlebot3_ws && colcon build --symlink-install
source install/setup.bash

# Install gazebo
export TURTLEBOT3_MODEL=waffle_pi
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py






