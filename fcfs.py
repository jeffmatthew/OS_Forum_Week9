def fcfs(initial_head, requests):
    current_head = initial_head
    total_head_movements = 0
    
    for request in requests:
        total_head_movements += abs(request - current_head)
        current_head = request
    
    return total_head_movements

def main():
    # Read initial position of the disk head and list of cylinder requests from the text file
    with open('requests.txt', 'r') as file:
        initial_head = int(file.readline().strip())
        requests = [int(line.strip()) for line in file.readlines()]

    # Calculate total amount of head movements using FCFS algorithm
    fcfs_head_movements = fcfs(initial_head, requests)
    
    # Print the total amount of head movements
    print("Total amount of head movements using FCFS algorithm:", fcfs_head_movements)

if __name__ == "__main__":
    main()
