import ctypes
import random
import time

# Load the C library
c_lib = ctypes.CDLL('./libquicksort.so')

# C function prototypes
c_lib.quicksort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]

# Load the Rust library
rust_lib = ctypes.CDLL('./quicksort/target/release/libquicksort.so')

# Rust function prototype
rust_lib.quicksort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

def test_quicksort():
    # Test with a random list of 100000000 integers
    size = 100000000
    arr = [random.randint(0, 10000) for _ in range(size)]
    

    # C QuickSort
    c_arr = (ctypes.c_int * size)(*arr)
    start_time = time.time()
    c_lib.quicksort(c_arr, 0, size - 1)
    c_time = time.time() - start_time
    print(f"C QuickSort completed in {c_time:.6f} seconds")
    

    # Rust QuickSort
    rust_arr = (ctypes.c_int * size)(*arr)
    start_time = time.time()
    rust_lib.quicksort(rust_arr, size)
    rust_time = time.time() - start_time
    print(f"Rust QuickSort completed in {rust_time:.6f} seconds")

    # C QuickSort
    c_arr = (ctypes.c_int * size)(*arr)
    start_time = time.time()
    c_lib.quicksort(c_arr, 0, size - 1)
    c_time = time.time() - start_time
    print(f"C QuickSort completed in {c_time:.6f} seconds")

    # Rust QuickSort
    rust_arr = (ctypes.c_int * size)(*arr)
    start_time = time.time()
    rust_lib.quicksort(rust_arr, size)
    rust_time = time.time() - start_time
    print(f"Rust QuickSort completed in {rust_time:.6f} seconds")

    
    # Check if both results are the same
    start_time = time.time()
    pythonsorttime = sorted(arr)
    python_time = time.time() - start_time
    print(f"Python sort completed in {python_time:.6f} seconds")

    assert list(c_arr) == sorted(arr), "C QuickSort failed!"
    assert list(rust_arr) == sorted(arr), "Rust QuickSort failed!"
    print("Both QuickSort implementations worked correctly!")

if __name__ == '__main__':
    test_quicksort()

