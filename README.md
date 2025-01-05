# ComparingCandRustQuicksort

A performance comparison between the C and Rust implementations of the classic QuickSort algorithm.

## Overview

This repository contains two implementations of the QuickSort algorithm: one written in **C** and the other in **Rust**. The goal of this project is to compare the performance, of QuickSort in these two languages.

## Key Features

- **C Implementation**: A traditional C implementation of the QuickSort algorithm.
- **Rust Implementation**: A modern, memory-safe implementation of QuickSort in Rust, taking advantage of Rust's ownership and borrowing model.
- **Performance Benchmarking**: Testing the speed of sorting a random list of numbers.


## Setup and Installation

```bash
gcc -shared -o libquicksort.so -fPIC -O3 -march=native -flto -funroll-loops quicksort.c
```

```bash
cargo --lib new quicksort
```
Then add the code from lib.rs and use the Cargo.toml
```bash
cargo build --release
```

```bash
python test.py
```

### Prerequisites

- **C Compiler**: Make sure you have a C compiler installed, such as GCC or Clang.
- **Rust Toolchain**: Install the Rust programming language via [rustup](https://rustup.rs/).
- **Benchmarking Tools**: Python


### Results

C was generally 10% faster than Rust.

