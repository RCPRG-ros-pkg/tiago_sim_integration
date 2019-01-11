cmake_minimum_required(VERSION 3.5)
project(incare_tiago)
# Get the information about this package's buildtime dependencies
  find_package(catkin REQUIRED
  #  COMPONENTS message_generation std_msgs sensor_msgs
  )

  # Declare the message files to be built
  #add_message_files(FILES
  #  MyMessage1.msg
  #  MyMessage2.msg
  #)

  # Declare the service files to be built
  #add_service_files(FILES
  #  MyService.srv
  #)

  # Actually generate the language-specific message and service files
  #generate_messages(DEPENDENCIES std_msgs sensor_msgs)

  # Declare that this catkin package's runtime dependencies
  catkin_package(
   CATKIN_DEPENDS tiago_2dnav_gazebo
  )

  # define executable using MyMessage1 etc.
  #add_executable(message_program src/main.cpp)
  #add_dependencies(message_program ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

  # define executable not using any messages/services provided by this package
  #add_executable(does_not_use_local_messages_program src/main.cpp)
  #add_dependencies(does_not_use_local_messages_program ${catkin_EXPORTED_TARGETS})

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  PATTERN ".svn" EXCLUDE)
install(DIRECTORY worlds/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/worlds
  PATTERN ".svn" EXCLUDE)

