# SCAN Algorithm

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

def main():
    # Read initial position of the disk head and list of cylinder requests from the text file
    with open('requests.txt', 'r') as file:
        initial_head = int(file.readline().strip())
        requests = [int(line.strip()) for line in file.readlines()]

    # Calculate total amount of head movements using SCAN algorithm
    scan_head_movements = scan(initial_head, requests)
    
    # Print the total amount of head movements
    print("Total amount of head movements using SCAN algorithm:", scan_head_movements)

if __name__ == "__main__":
    main()
