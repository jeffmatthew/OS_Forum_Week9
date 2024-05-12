def scan(initial_head, requests):
    total_head_movements = 0
    current_head = initial_head
    direction = 1  # 1 for moving towards higher cylinder numbers, -1 for moving towards lower cylinder numbers

    # Sort requests in ascending order
    sorted_requests = sorted(requests)

    # Find the closest request in the current direction
    while True:
        next_request = None
        for request in sorted_requests:
            if direction == 1 and request >= current_head:
                next_request = request
                break
            elif direction == -1 and request <= current_head:
                next_request = request
        if next_request is None:
            break
        total_head_movements += abs(next_request - current_head)
        current_head = next_request
        sorted_requests.remove(next_request)

    # Reverse direction and scan back to the beginning
    direction *= -1
    total_head_movements += abs(current_head - (0 if direction == 1 else 4999))
    current_head = 0 if direction == 1 else 4999

    # Service remaining requests in the reverse direction
    while sorted_requests:
        next_request = None
        for request in sorted_requests:
            if direction == 1 and request >= current_head:
                next_request = request
                break
            elif direction == -1 and request <= current_head:
                next_request = request
        if next_request is None:
            break
        total_head_movements += abs(next_request - current_head)
        current_head = next_request
        sorted_requests.remove(next_request)

    return total_head_movements

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

def optimize_scan(initial_head, requests):
    sorted_requests = sorted(requests)
    lower_requests = [r for r in sorted_requests if r < initial_head]
    upper_requests = [r for r in sorted_requests if r >= initial_head]
    return lower_requests[::-1] + upper_requests

def optimize_c_scan(initial_head, requests):
    sorted_requests = sorted(requests)
    lower_requests = [r for r in sorted_requests if r <= initial_head]
    upper_requests = [r for r in sorted_requests if r > initial_head]
    return lower_requests[::-1] + upper_requests

def main():
    # Read initial position of the disk head and list of cylinder requests from the text file
    with open('requests.txt', 'r') as file:
        initial_head = int(file.readline().strip())
        requests = [int(line.strip()) for line in file.readlines()]

    # Optimize the order of requests for SCAN algorithm
    optimized_scan_requests = optimize_scan(initial_head, requests)
    scan_head_movements_optimized = scan(initial_head, optimized_scan_requests)
    
    # Optimize the order of requests for C-SCAN algorithm
    optimized_c_scan_requests = optimize_c_scan(initial_head, requests)
    c_scan_head_movements_optimized = c_scan(initial_head, optimized_c_scan_requests)
    
    # Print the total amount of head movements for optimized SCAN and C-SCAN algorithms
    print("Total amount of head movements using optimized SCAN algorithm:", scan_head_movements_optimized)
    print("Total amount of head movements using optimized C-SCAN algorithm:", c_scan_head_movements_optimized)

if __name__ == "__main__":
    main()
