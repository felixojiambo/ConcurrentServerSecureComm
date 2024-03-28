import timeit
import matplotlib.pyplot as plt

def prompt_for_file_path():
    return input("Enter the file path: ")

def linear_search(file_path, search_string):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if search_string in line:
                print(f"Found '{search_string}' in line {line_number}: {line.strip()}")
def binary_search(file_path, search_string):
    lines = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Skip lines that don't start with a number
            if not line.strip().startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                continue
            lines.append((line_number, line))
    
    # Sort lines based on the first number in each line
    lines.sort(key=lambda x: int(x[1].split(';')[0]))
    
    low = 0
    high = len(lines) - 1
    while low <= high:
        mid = (low + high) // 2
        line_number, line = lines[mid]
        if search_string in line:
            print(f"Found '{search_string}' in line {line_number}: {line.strip()}")
            return
        elif search_string < line:
            high = mid - 1
        else:
            low = mid + 1
    print("Search string not found.")


def benchmark_search_methods(file_path, search_string):
    # Benchmark linear_search
    start_time = timeit.default_timer()
    linear_search(file_path, search_string)
    method_1_time = timeit.default_timer() - start_time
    
    # Benchmark binary_search
    start_time = timeit.default_timer()
    binary_search(file_path, search_string)
    method_2_time = timeit.default_timer() - start_time
    
    return method_1_time, method_2_time

if __name__ == "__main__":
    file_path = prompt_for_file_path()
    search_string = input("Enter the search string: ")
    
    method_1_time, method_2_time = benchmark_search_methods(file_path, search_string)
    
    # Print the table to the console
    print("| Method          | Execution Time |")
    print("|-----------------|----------------|")
    print(f"| Linear Search   | {method_1_time}   |")
    print(f"| Binary Search   | {method_2_time}   |")
    
    # Data for the chart
    methods = ['Linear Search', 'Binary Search']
    times = [method_1_time, method_2_time]
    
    # Create the bar chart
    plt.bar(methods, times)
    plt.xlabel('Method')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Search Method Performance')
    plt.show()
