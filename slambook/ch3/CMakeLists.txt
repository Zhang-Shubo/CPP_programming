cmake_minimum_required( VERSION 2.8 )

project( use_eigen )

set(CMAKE_BULID_TYPE "Release")
#set(CMAKE_CXX_FLAGS "-03")

include_directories("/usr/include/eigen3")

add_executable(use_egien use_eigen.cpp)