search_mode=OPTIMIZE_MAX_JOINT
srdf_filename=sr80.srdf
robot_name_in_srdf=sr80
moveit_config_pkg=sr80_moveit_config
robot_name=sr80
planning_group_name=manipulator
ikfast_plugin_pkg=sr80_manipulator_ikfast_plugin
base_link_name=base_link
eef_link_name=flange
ikfast_output_path=/root/ws_moveit/src/sr80_manipulator_ikfast_plugin/src/sr80_manipulator_ikfast_solver.cpp

rosrun moveit_kinematics create_ikfast_moveit_plugin.py\
  --search_mode=$search_mode\
  --srdf_filename=$srdf_filename\
  --robot_name_in_srdf=$robot_name_in_srdf\
  --moveit_config_pkg=$moveit_config_pkg\
  $robot_name\
  $planning_group_name\
  $ikfast_plugin_pkg\
  $base_link_name\
  $eef_link_name\
  $ikfast_output_path
