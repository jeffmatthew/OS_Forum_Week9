# C-SCAN (Circular SCAN) Algorithm

def c_scan(initial_head, requests):
    total_head_movements = 0
    current_head = initial_head
    
    # Sort requests in ascending order
    sorted_requests = sorted(requests)
    
    # Service requests until the end of the disk
    for request in sorted_requests:
        total_head_movements += abs(request - current_head)
        current_head = request
    
    # Jump to the beginning of the disk
    total_head_movements += abs(current_head - 0)
    current_head = 0
    
    # Service remaining requests until the last request
    for request in sorted_requests:
        total_head_movements += abs(request - current_head)
        current_head = request
    
    return total_head_movements

def main():
    # Read initial position of the disk head and list of cylinder requests from the text file
    with open('requests.txt', 'r') as file:
        initial_head = int(file.readline().strip())
        requests = [int(line.strip()) for line in file.readlines()]

    # Calculate total amount of head movements using C-SCAN algorithm
    c_scan_head_movements = c_scan(initial_head, requests)
    
    # Print the total amount of head movements
    print("Total amount of head movements using C-SCAN algorithm:", c_scan_head_movements)

if __name__ == "__main__":
    main()
