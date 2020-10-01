# 声明要求cmake最低版本
cmake_minimum_required( VERSION 2.8 )

# 声明项目名称
project( hello_slam )

# 头文件目录
#include_directories(
#
#)

#添加一个可执行程序
add_executable(hello helloslam.cpp)

# 编译共享库
#add_library(hello_shared SHARED libhello_shared.cpp)

#添加一个可执行程序
add_executable(usehello usehello.cpp)

target_link_libraries(usehello ${PROJECT_SOURCE_DIR}/libhello_shared.so)