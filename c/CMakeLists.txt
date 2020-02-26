# 此文件是手动编写 的CMake file ，用 cmake . 命令可以编译。
# CMake 最低版本号要求
cmake_minimum_required(VERSION 3.2)

# 项目信息
project (c)

# 指定生成目标
add_executable(c hello.c)

# 设置调试选项
set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")

# 设置测试选项
enable_testing()

# 测试运行 后面是参数列表
add_test (test_run c 5 2)
