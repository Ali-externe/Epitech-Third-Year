if (${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})
    message(FATAL_ERROR "Prevented in-tree built. Please create a build directory outside of the source code and call cmake from there")
endif ()

cmake_minimum_required(VERSION 3.5.1)
project(r-type)

#set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../)
set(CMAKE_CXX_STANDARD 17)

add_definitions("-fPIC")

if(MSVC)
    set(CMAKE_EXE_LINKER_FLAGS
            "${CMAKE_EXE_LINKER_FLAGS}")
else()
    set(STANDARD_UNIX_CXX_FLAGS "-Wall -g3 -Wextra -Wfatal-errors")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${STANDARD_UNIX_CXX_FLAGS}")
endif()

if (EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
else()
    message(FATAL_ERROR "No conanbuildinfo.cmake file found")
endif()

#include(CMakeSources.cmake)

conan_basic_setup()


include_directories("${PROJECT_SOURCE_DIR}/client/include/")
include_directories("${PROJECT_SOURCE_DIR}/server/include/")
file(GLOB_RECURSE SOURCES_CLIENT RELATIVE ${CMAKE_SOURCE_DIR} "client/sources/*.cpp")
file(GLOB_RECURSE SOURCES_SERVER RELATIVE ${CMAKE_SOURCE_DIR} "server/sources/*.cpp")

include_directories(build)

add_executable(r-type_client ${SOURCES_CLIENT})
add_executable(r-type_server ${SOURCES_SERVER} ${MOC_SRCS})


#############################################################

target_link_libraries(r-type_client sfml-graphics sfml-network sfml-window sfml-audio sfml-system -pthread)
target_include_directories(r-type_client PRIVATE inc ../common/inc)
