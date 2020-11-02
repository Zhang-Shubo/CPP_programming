# 声明要求cmake最低版本
cmake_minimum_required( VERSION 2.8 )

# 声明项目名称
project( word_break )

# 头文件目录
#include_directories(
#
#)

# 编译共享库
#add_library(trie SHARED trie.cpp)

#添加一个可执行程序
add_executable(word_break word_break.cpp)


target_link_libraries(word_break ${PROJECT_SOURCE_DIR}/libtrie.so)