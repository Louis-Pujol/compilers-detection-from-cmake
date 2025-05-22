cmake_minimum_required(VERSION 3.10)
project(MyProject LANGUAGES CXX)

# Find OpenMP package
find_package(OpenMP)
find_package(CUDAToolkit)


message(STATUS "C++ Compiler: ${CMAKE_CXX_COMPILER}")
message(STATUS "C++ Compiler Version: ${CMAKE_CXX_COMPILER_VERSION}")

# Check if OpenMP is found
if(OpenMP_CXX_FOUND)
    
    # Display OpenMP version
    if(NOT DEFINED OpenMP_CXX_VERSION)
        message(STATUS "OpenMP found, but version information not available.")
    else()
        message(STATUS "OpenMP found, version: ${OpenMP_CXX_VERSION}")
    endif()
else()
    message(WARNING "OpenMP not found.")
endif()


# Check for CUDA
if(DEFINED CUDAToolkit_VERSION)
    message(STATUS "CUDA found, version: ${CUDAToolkit_VERSION}")
    
    # Check nvcc
    if(DEFINED CUDAToolkit_NVCC_EXECUTABLE)
        message(STATUS "NVCC executable: ${CUDAToolkit_NVCC_EXECUTABLE}")
    else()
        message(WARNING "NVCC executable not found!")
    endif()

    # CUDA include path
    if (DEFINED CUDAToolkit_INCLUDE_DIRS)
        message(STATUS "CUDA Include Dirs: ${CUDAToolkit_INCLUDE_DIRS}/")
    else()
        message(WARNING "Libraries not found!")
    endif()

    # CUDA library path
    if (DEFINED CUDAToolkit_LIBRARY_DIR)
        message(STATUS "CUDA Library dir: ${CUDAToolkit_LIBRARY_DIR}/")

        find_library(CUDA_NVRTC "nvrtc" PATHS "${CUDAToolkit_LIBRARY_DIR}" NO_DEFAULT_PATH)
        if(DEFINED CUDA_NVRTC)
            message(STATUS "Library NVRTC found at: ${CUDA_NVRTC}")
        else()
            message(WARNING "Library NVRTC not found!")
        endif()

        find_library(CUDA_CUDART "cudart" PATHS "${CUDAToolkit_LIBRARY_DIR}" NO_DEFAULT_PATH)
        if(DEFINED CUDA_CUDART)
            message(STATUS "Library CUDART found at: ${CUDA_CUDART}")
        else()
            message(WARNING "Library CUDART not found!")
        endif()

        find_library(CUDA_CUDA "cuda" PATHS "${CUDAToolkit_LIBRARY_DIR}" NO_DEFAULT_PATH)
        if(DEFINED CUDA_CUDA)
            message(STATUS "Library CUDA found at: ${CUDA_CUDA}")
        else()
            message(WARNING "Library CUDA not found!")
        endif()


    else()
        message(WARNING "Libraries not found!")
    endif()

else()
    message(WARNING "CUDA Toolkit not found.")
endif()