# generated from catkin/cmake/template/pkgConfig.cmake.in

# append elements to a list and remove existing duplicates from the list
# copied from catkin/cmake/list_append_deduplicate.cmake to keep pkgConfig
# self contained
macro(_list_append_deduplicate listname)
  if(NOT "${ARGN}" STREQUAL "")
    if(${listname})
      list(REMOVE_ITEM ${listname} ${ARGN})
    endif()
    list(APPEND ${listname} ${ARGN})
  endif()
endmacro()

# append elements to a list if they are not already in the list
# copied from catkin/cmake/list_append_unique.cmake to keep pkgConfig
# self contained
macro(_list_append_unique listname)
  foreach(_item ${ARGN})
    list(FIND ${listname} ${_item} _index)
    if(_index EQUAL -1)
      list(APPEND ${listname} ${_item})
    endif()
  endforeach()
endmacro()

# pack a list of libraries with optional build configuration keywords
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_pack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  set(_argn ${ARGN})
  list(LENGTH _argn _count)
  set(_index 0)
  while(${_index} LESS ${_count})
    list(GET _argn ${_index} lib)
    if("${lib}" MATCHES "^(debug|optimized|general)$")
      math(EXPR _index "${_index} + 1")
      if(${_index} EQUAL ${_count})
        message(FATAL_ERROR "_pack_libraries_with_build_configuration() the list of libraries '${ARGN}' ends with '${lib}' which is a build configuration keyword and must be followed by a library")
      endif()
      list(GET _argn ${_index} library)
      list(APPEND ${VAR} "${lib}${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}${library}")
    else()
      list(APPEND ${VAR} "${lib}")
    endif()
    math(EXPR _index "${_index} + 1")
  endwhile()
endmacro()

# unpack a list of libraries with optional build configuration keyword prefixes
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_unpack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  foreach(lib ${ARGN})
    string(REGEX REPLACE "^(debug|optimized|general)${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}(.+)$" "\\1;\\2" lib "${lib}")
    list(APPEND ${VAR} "${lib}")
  endforeach()
endmacro()


if(industrial_extrinsic_cal_CONFIG_INCLUDED)
  return()
endif()
set(industrial_extrinsic_cal_CONFIG_INCLUDED TRUE)

# set variables for source/devel/install prefixes
if("TRUE" STREQUAL "TRUE")
  set(industrial_extrinsic_cal_SOURCE_PREFIX /home/casch/yumi_depends_ws/src/extrinsic_Industrial/industrial_calibration/industrial_extrinsic_cal)
  set(industrial_extrinsic_cal_DEVEL_PREFIX /home/casch/yumi_depends_ws/devel)
  set(industrial_extrinsic_cal_INSTALL_PREFIX "")
  set(industrial_extrinsic_cal_PREFIX ${industrial_extrinsic_cal_DEVEL_PREFIX})
else()
  set(industrial_extrinsic_cal_SOURCE_PREFIX "")
  set(industrial_extrinsic_cal_DEVEL_PREFIX "")
  set(industrial_extrinsic_cal_INSTALL_PREFIX /home/casch/yumi_depends_ws/install)
  set(industrial_extrinsic_cal_PREFIX ${industrial_extrinsic_cal_INSTALL_PREFIX})
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "WARNING: package 'industrial_extrinsic_cal' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  message("${_msg}")
endif()

# flag project as catkin-based to distinguish if a find_package()-ed project is a catkin project
set(industrial_extrinsic_cal_FOUND_CATKIN_PROJECT TRUE)

if(NOT "/home/casch/yumi_depends_ws/devel/include;/home/casch/yumi_depends_ws/src/extrinsic_Industrial/industrial_calibration/industrial_extrinsic_cal/include;/usr/include;/usr/include/eigen3 " STREQUAL " ")
  set(industrial_extrinsic_cal_INCLUDE_DIRS "")
  set(_include_dirs "/home/casch/yumi_depends_ws/devel/include;/home/casch/yumi_depends_ws/src/extrinsic_Industrial/industrial_calibration/industrial_extrinsic_cal/include;/usr/include;/usr/include/eigen3")
  if(NOT "https://github.com/ros-industrial/industrial_calibration/issues " STREQUAL " ")
    set(_report "Check the issue tracker 'https://github.com/ros-industrial/industrial_calibration/issues' and consider creating a ticket if the problem has not been reported yet.")
  elseif(NOT "http://wiki.ros.org/industrial_extrinsic_cal " STREQUAL " ")
    set(_report "Check the website 'http://wiki.ros.org/industrial_extrinsic_cal' for information and consider reporting the problem.")
  else()
    set(_report "Report the problem to the maintainer 'Chris Lewis <clewis@swri.org>, AustinDeric <Austin.Deric@gmail.com>' and request to fix the problem.")
  endif()
  foreach(idir ${_include_dirs})
    if(IS_ABSOLUTE ${idir} AND IS_DIRECTORY ${idir})
      set(include ${idir})
    elseif("${idir} " STREQUAL "include ")
      get_filename_component(include "${industrial_extrinsic_cal_DIR}/../../../include" ABSOLUTE)
      if(NOT IS_DIRECTORY ${include})
        message(FATAL_ERROR "Project 'industrial_extrinsic_cal' specifies '${idir}' as an include dir, which is not found.  It does not exist in '${include}'.  ${_report}")
      endif()
    else()
      message(FATAL_ERROR "Project 'industrial_extrinsic_cal' specifies '${idir}' as an include dir, which is not found.  It does neither exist as an absolute directory nor in '/home/casch/yumi_depends_ws/src/extrinsic_Industrial/industrial_calibration/industrial_extrinsic_cal/${idir}'.  ${_report}")
    endif()
    _list_append_unique(industrial_extrinsic_cal_INCLUDE_DIRS ${include})
  endforeach()
endif()

set(libraries "industrial_extrinsic_cal;/usr/lib/libceres.so.1.12.0")
foreach(library ${libraries})
  # keep build configuration keywords, target names and absolute libraries as-is
  if("${library}" MATCHES "^(debug|optimized|general)$")
    list(APPEND industrial_extrinsic_cal_LIBRARIES ${library})
  elseif(TARGET ${library})
    list(APPEND industrial_extrinsic_cal_LIBRARIES ${library})
  elseif(IS_ABSOLUTE ${library})
    list(APPEND industrial_extrinsic_cal_LIBRARIES ${library})
  else()
    set(lib_path "")
    set(lib "${library}-NOTFOUND")
    # since the path where the library is found is returned we have to iterate over the paths manually
    foreach(path /home/casch/yumi_depends_ws/devel/lib;/home/casch/yumi_depends_ws/devel/lib;/opt/ros/kinetic/lib)
      find_library(lib ${library}
        PATHS ${path}
        NO_DEFAULT_PATH NO_CMAKE_FIND_ROOT_PATH)
      if(lib)
        set(lib_path ${path})
        break()
      endif()
    endforeach()
    if(lib)
      _list_append_unique(industrial_extrinsic_cal_LIBRARY_DIRS ${lib_path})
      list(APPEND industrial_extrinsic_cal_LIBRARIES ${lib})
    else()
      # as a fall back for non-catkin libraries try to search globally
      find_library(lib ${library})
      if(NOT lib)
        message(FATAL_ERROR "Project '${PROJECT_NAME}' tried to find library '${library}'.  The library is neither a target nor built/installed properly.  Did you compile project 'industrial_extrinsic_cal'?  Did you find_package() it before the subdirectory containing its code is included?")
      endif()
      list(APPEND industrial_extrinsic_cal_LIBRARIES ${lib})
    endif()
  endif()
endforeach()

set(industrial_extrinsic_cal_EXPORTED_TARGETS "industrial_extrinsic_cal_generate_messages_cpp;industrial_extrinsic_cal_generate_messages_eus;industrial_extrinsic_cal_generate_messages_lisp;industrial_extrinsic_cal_generate_messages_nodejs;industrial_extrinsic_cal_generate_messages_py;industrial_extrinsic_cal_gencfg")
# create dummy targets for exported code generation targets to make life of users easier
foreach(t ${industrial_extrinsic_cal_EXPORTED_TARGETS})
  if(NOT TARGET ${t})
    add_custom_target(${t})
  endif()
endforeach()

set(depends "actionlib;actionlib_msgs;cv_bridge;geometry_msgs;image_transport;message_runtime;moveit_ros_planning_interface;rosconsole;roscpp;roslib;roslint;sensor_msgs;std_msgs;std_srvs;tf;tf_conversions;pcl_ros;pcl_conversions")
foreach(depend ${depends})
  string(REPLACE " " ";" depend_list ${depend})
  # the package name of the dependency must be kept in a unique variable so that it is not overwritten in recursive calls
  list(GET depend_list 0 industrial_extrinsic_cal_dep)
  list(LENGTH depend_list count)
  if(${count} EQUAL 1)
    # simple dependencies must only be find_package()-ed once
    if(NOT ${industrial_extrinsic_cal_dep}_FOUND)
      find_package(${industrial_extrinsic_cal_dep} REQUIRED NO_MODULE)
    endif()
  else()
    # dependencies with components must be find_package()-ed again
    list(REMOVE_AT depend_list 0)
    find_package(${industrial_extrinsic_cal_dep} REQUIRED NO_MODULE ${depend_list})
  endif()
  _list_append_unique(industrial_extrinsic_cal_INCLUDE_DIRS ${${industrial_extrinsic_cal_dep}_INCLUDE_DIRS})

  # merge build configuration keywords with library names to correctly deduplicate
  _pack_libraries_with_build_configuration(industrial_extrinsic_cal_LIBRARIES ${industrial_extrinsic_cal_LIBRARIES})
  _pack_libraries_with_build_configuration(_libraries ${${industrial_extrinsic_cal_dep}_LIBRARIES})
  _list_append_deduplicate(industrial_extrinsic_cal_LIBRARIES ${_libraries})
  # undo build configuration keyword merging after deduplication
  _unpack_libraries_with_build_configuration(industrial_extrinsic_cal_LIBRARIES ${industrial_extrinsic_cal_LIBRARIES})

  _list_append_unique(industrial_extrinsic_cal_LIBRARY_DIRS ${${industrial_extrinsic_cal_dep}_LIBRARY_DIRS})
  list(APPEND industrial_extrinsic_cal_EXPORTED_TARGETS ${${industrial_extrinsic_cal_dep}_EXPORTED_TARGETS})
endforeach()

set(pkg_cfg_extras "industrial_extrinsic_cal-msg-extras.cmake")
foreach(extra ${pkg_cfg_extras})
  if(NOT IS_ABSOLUTE ${extra})
    set(extra ${industrial_extrinsic_cal_DIR}/${extra})
  endif()
  include(${extra})
endforeach()
