# SR80_moveit
ros noetic moveit workspace

> start-docker.sh noetic

> terminator

> cd /root/grass

> DEBUG grass:* npm start

-- splip terminal to 4 --

> roslaunch rosbridge_server rosbridge_websocket.launch

> rosrun tf2_web_republisher tf2_web_republisher

> roslaunch sr80_moveit_config_new demo_gazebo.launch

> roslaunch sr80_moveit_config_new sr80_servo.launch

