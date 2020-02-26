# CMake 最低版本号要求
cmake_minimum_required(VERSION 3.2)

# 项目信息
project (c)

# 指定生成目标
add_executable(c hello.c)

set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")
