cmake_minimum_required(VERSION 3.8)
project(moveit2_tutorials)

#if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
#  add_compile_options(-Wall -Wextra -Wpedantic)
#endif()

find_package(moveit_common REQUIRED)

moveit_package()

set(THIS_PACKAGE_INCLUDE_DIRS
  doc/interactivity/include
)

set(THIS_PACKAGE_INCLUDE_DEPENDS
  ament_cmake
  Boost
  control_msgs
  Eigen3
  interactive_markers
  moveit_core
  moveit_msgs
  moveit_ros_planning
  moveit_ros_planning_interface
  moveit_servo
  pluginlib
  rclcpp
  rclcpp_action
  tf2_geometry_msgs
  tf2_geometry_msgs
  tf2_ros
)

foreach(Dependency IN ITEMS ${THIS_PACKAGE_INCLUDE_DEPENDS})
  find_package(${Dependency} REQUIRED)
endforeach()

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

include_directories(${THIS_PACKAGE_INCLUDE_DIRS})

add_executable(servo_keyboard_input src/servo_keyboard_input.cpp)
target_include_directories(servo_keyboard_input PUBLIC include)
#  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
#  $<INSTALL_INTERFACE:include>)
ament_target_dependencies(
  servo_keyboard_input 
  ${THIS_PACKAGE_INCLUDE_DEPENDS}
  #rclcpp 
  #control_msgs 
  #geometry_msgs
  )

target_include_directories(servo_keyboard_input PUBLIC include)
#  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
#  $<INSTALL_INTERFACE:include>)

#target_compile_features(servo_keyboard_input PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17

add_executable(robot_model_and_state src/robot_model_and_state.cpp)

target_include_directories(robot_model_and_state PUBLIC include)
#  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
#  $<INSTALL_INTERFACE:include>)

ament_target_dependencies(
    robot_model_and_state
    ${THIS_PACKAGE_INCLUDE_DEPENDS}
    #moveit_core
    #moveit
    #moveit_common
    #Boost
    )


#target_compile_features(robot_model_and_state PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17

install(
  TARGETS
    servo_keyboard_input
    robot_model_and_state  
  DESTINATION 
    lib/${PROJECT_NAME}
)

ament_export_dependencies(
  ${THIS_PACKAGE_INCLUDE_DEPENDS}
)

ament_export_include_directories(include)

ament_package()
