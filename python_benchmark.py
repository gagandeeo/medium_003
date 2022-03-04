import python_self
import cpp_wrapper
import rust_wrapper

@profile
def python_ext(lines, size_):
    return python_self.insertionSort(lines, size_)

@profile
def cpp_ext(lines, size_):
    return cpp_wrapper.insertionSort(lines,size_)

@profile
def rust_ext(lines, size_):
    return rust_wrapper.insertion_sort(lines,size_)

if __name__ == "__main__":
    
    text_file = "randomNumbers.txt"
    with open(text_file, 'r') as f:
        data = f.read()
    lines = [int(i) for i in data.split(",")]
    size_ = len(lines)
    
    # python_self
    python_ext(lines.copy(), size_)
    # cpp
    cpp_ext(lines.copy(), size_)
    # rust
    rust_ext(lines.copy(), size_)