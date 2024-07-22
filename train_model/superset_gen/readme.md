# Superset Generator [The combination generator]

The combination generator is written in C++ for speed. These combinations are used to generate the synthetic supersets. The synthetic dataset part is currently written in Python, and it works fine for datasets up to 50,000 in size. However, for the full-scale training needed to take this project to the next level, Python becomes too slow.

## Current Status

- **Combination Generator**:
  - Written in C++ for optimal performance.
  - Efficiently generates unique combinations used in synthetic superset creation.

- **Synthetic Dataset Generator**:
  - Currently implemented in Python.
  - Suitable for smaller datasets (up to 50,000).
  - Performance bottleneck for larger datasets.

## Future Development

When the C++ version of the synthetic dataset generator is complete and the time is right, it will be added here. This will significantly improve performance and allow for handling much larger datasets efficiently.

## Usage

**Combination Generator (C++)**:
- Designed to quickly generate combinations for superset creation.
- Ensures unique combinations to optimize dataset quality.

**Synthetic Dataset Generator (Python)**:
- Ideal for preliminary testing and smaller datasets.
- Easy to understand and modify for initial development stages.

## Performance

- **Python Implementation**:
  - Handles up to 50,000 data points efficiently.
  - Slows down considerably with larger datasets.

- **C++ Implementation**:
  - Expected to handle full-scale datasets.
  - Provides the necessary speed and efficiency for large-scale synthetic dataset generation.

Stay tuned for updates on the progress and integration of the C++ implementation for synthetic dataset generation.

## Command-line Arguments

The combination generator accepts the following command-line arguments:

- `start_index`: Start index for generating combinations.
- `end_index`: End index for generating combinations.
- `min_val`: Minimum value for combination elements.
- `max_val`: Maximum value for combination elements.
- `count`: Number of elements in each combination.
- `print_interval`: Interval for printing progress.
- `max_file_block_size`: Maximum block size for writing to file.
- `write_to_file`: Flag to enable/disable writing to file (1 to enable, 0 to disable).
- `file_reset`: Flag to reset/clear the file before writing (1 to reset, 0 to not reset).

### Compilation and Execution

```sh
g++ -o combination_generator combination_generator.cpp -std=c++11
./combination_generator 1 1925643484 1 59 7 1000000 50000 1 1
```
# Min Superset [current] on a single I7 with Nvdia GTX this takes days, and runs boiling
## Superset Min Specifications
- Mem:48gb
- HD:20gb
- CPU:
- GPU:

- 
## Recomended System
- Mem: 64gb
- HD:  20gb
- CPU:
- GPU:

- 
# Full Superset [funds needed] on a single I7 with Nvdia GTX this would take many lifetimes

## Superset Min Specifications
- Mem:64gb
- HD:40tb
- CPU:
- GPU:
- 
## Recomended System
- Mem: 32tb
- HD: SSD 40tb
- CPU:
- GPU:
