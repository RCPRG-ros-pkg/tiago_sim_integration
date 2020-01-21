sudo apt update
sudo apt upgrade
mkdir ~/tiago_public_ws
cd ~/tiago_public_ws
wget https://raw.githubusercontent.com/RCPRG-ros-pkg/tiago_sim_integration/master/rcprg_tiago_public-melodic.rosinstall
sudo apt install -y python-rosinstall
rosinstall src /opt/ros/melodic rcprg_tiago_public-melodic.rosinstall
sudo apt install -y ros-melodic-control-toolbox python-catkin-tools ros-melodic-imu-sensor-controller ros-melodic-force-torque-sensor-controller ros-melodic-twist-mux ros-melodic-four-wheel-steering-controller ros-melodic-image-proc ros-melodic-range-sensor-layer ros-melodic-pointcloud-to-laserscan ros-melodic-laser-filters ros-melodic-teb-local-planner ros-melodic-gmapping ros-melodic-octomap-server ros-melodic-octomap-mapping ros-melodic-people-msgs ros-melodic-rosbridge-server ros-melodic-rospy-message-converter bison flex
cp src/rcprg/tiago_sim_integration/move_group_patch/move_group.launch src/pal/tiago_moveit_config/launch/move_group.launch
cd ~/tiago_public_ws
source /opt/ros/melodic/setup.bash
catkin build -DCATKIN_ENABLE_TESTING=0
