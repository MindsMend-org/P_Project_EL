#include <iostream>
#include <vector>
#include <unordered_set>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <dirent.h>
#include <stdio.h>
#include <string.h>

// Function to delete existing files matching a pattern
void delete_existing_files(const std::string& pattern) {
    DIR *dir;
    struct dirent *ent;
    if ((dir = opendir(".")) != NULL) {
        while ((ent = readdir(dir)) != NULL) {
            std::string filename = ent->d_name;
            if (filename.find(pattern) != std::string::npos) {
                remove(filename.c_str());
            }
        }
        closedir(dir);
    } else {
        perror("Could not open directory");
    }
}

// Function to generate the next combination
bool next_combination(std::vector<int>& combination, int n, int k) {
    for (int i = k - 1; i >= 0; --i) {
        if (combination[i] < n - k + i + 1) {
            ++combination[i];
            for (int j = i + 1; j < k; ++j) {
                combination[j] = combination[j - 1] + 1;
            }
            return true;
        }
    }
    return false;
}

// Function to validate a combination (ensures no duplicates)
bool is_valid_combination(const std::vector<int>& combination) {
    std::unordered_set<int> seen;
    for (int num : combination) {
        if (seen.find(num) != seen.end()) {
            return false;  // Duplicate found
        }
        seen.insert(num);
    }
    return true;  // All numbers are unique
}

// Function to write combinations to a file
void write_combinations_to_file(const std::vector<std::vector<int>>& buffer, std::ofstream& file) {
    for (const auto& combination : buffer) {
        for (int num : combination) {
            file << num << " ";
        }
        file << "\n";
    }
}

int main(int argc, char* argv[]) {
    // Default values
    int min_val = 1;
    int max_val = 59;
    int count = 7;
    unsigned long long start_index = 1;
    unsigned long long end_index = 1925643484;
    unsigned long long print_interval = 1000000; // Adjust this value as needed
    unsigned long long max_file_block_size = 150000; // Max combinations per file
    bool write_to_file = true; // Whether to write combinations to a file
    bool file_reset = true; // Whether to reset the file at the start
    std::ofstream file;
    int file_index = 0; // File index for multiple files

    // If command-line arguments are provided, use them
    if (argc == 10) {
        try {
            start_index = std::stoull(argv[1]);
            end_index = std::stoull(argv[2]);
            min_val = std::stoi(argv[3]);
            max_val = std::stoi(argv[4]);
            count = std::stoi(argv[5]);
            print_interval = std::stoull(argv[6]);
            max_file_block_size = std::stoull(argv[7]);
            write_to_file = std::stoi(argv[8]);
            file_reset = std::stoi(argv[9]);
        } catch (const std::invalid_argument& e) {
            std::cerr << "Invalid argument: " << e.what() << std::endl;
            return 1;
        } catch (const std::out_of_range& e) {
            std::cerr << "Argument out of range: " << e.what() << std::endl;
            return 1;
        }
    } else if (argc != 1) {
        std::cerr << "Usage: " << argv[0] << " <start_index> <end_index> <min_val> <max_val> <count> <print_interval> <max_file_block_size> <write_to_file> <file_reset>" << std::endl;
        return 1;
    }

    // Print the used values for debugging
    std::cout << "Using values:" << std::endl;
    std::cout << "start_index: " << start_index << std::endl;
    std::cout << "end_index: " << end_index << std::endl;
    std::cout << "min_val: " << min_val << std::endl;
    std::cout << "max_val: " << max_val << std::endl;
    std::cout << "count: " << count << std::endl;
    std::cout << "print_interval: " << print_interval << std::endl;
    std::cout << "max_file_block_size: " << max_file_block_size << std::endl;
    std::cout << "write_to_file: " << write_to_file << std::endl;
    std::cout << "file_reset: " << file_reset << std::endl;

    if (file_reset) {
        delete_existing_files("valid_combinations");
    }

    if (write_to_file) {
        std::ostringstream filename;
        filename << "valid_combinations_" << std::setw(4) << std::setfill('0') << file_index++ << ".txt";
        file.open(filename.str(), std::ofstream::out | std::ofstream::trunc); // Open in truncate mode

        if (!file.is_open()) {
            std::cerr << "Error: Could not open file for writing." << std::endl;
            return 1;
        }
    }

    // Initialize the first combination
    std::vector<int> combination(count);
    for (int i = 0; i < count; ++i) {
        combination[i] = min_val + i;
    }

    std::vector<std::vector<int>> buffer;
    const size_t buffer_size = 1000; // Adjust buffer size as needed
    unsigned long long current_block_size = 0; // Current block size counter

    unsigned long long index = 0;
    do {
        if (index >= start_index && index < end_index) {
            // Print progress every print_interval updates
            if ((index - start_index) % print_interval == 0) {
                std::cout << "Checked " << (index - start_index) << " combinations: ";
                for (int num : combination) {
                    std::cout << num << " ";
                }
                std::cout << std::endl;
            }

            if (is_valid_combination(combination)) {
                buffer.push_back(combination);
            }

            if (write_to_file && buffer.size() >= buffer_size) {
                write_combinations_to_file(buffer, file);
                buffer.clear();
                current_block_size += buffer_size;

                if (current_block_size >= max_file_block_size) {
                    file.close();
                    std::ostringstream filename;
                    filename << "valid_combinations_" << std::setw(4) << std::setfill('0') << file_index++ << ".txt";
                    file.open(filename.str(), std::ios::app); // Open in append mode

                    if (!file.is_open()) {
                        std::cerr << "Error: Could not open file for writing." << std::endl;
                        return 1;
                    }

                    current_block_size = 0;
                }
            }
        }
        ++index;
    } while (next_combination(combination, max_val, count) && index < end_index);

    // Write any remaining combinations in the buffer to the file
    if (write_to_file && !buffer.empty()) {
        write_combinations_to_file(buffer, file);
    }

    if (write_to_file) {
        file.close();
        std::cout << "File closed." << std::endl;
    }

    std::cout << "Total combinations processed: " << (index - start_index) << std::endl;

    return 0;
}
