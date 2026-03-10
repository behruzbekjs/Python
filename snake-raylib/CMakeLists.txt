cmake_minimum_required(VERSION 3.20)
project(snake_raylib LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(raylib CONFIG REQUIRED)

add_executable(snake_raylib main.cpp)
target_link_libraries(snake_raylib PRIVATE raylib)

if (WIN32)
  target_compile_definitions(snake_raylib PRIVATE _CRT_SECURE_NO_WARNINGS)
endif()
