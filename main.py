# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0] * n
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        min_completion_time = threads[0]
        min_thread = 0
        for j in range(1, n):
            if threads[j] < min_completion_time:
                min_completion_time = threads[j]
                min_thread = j
        output.append((min_thread, min_completion_time))
        threads[min_thread] += data[i]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    # n = 0
    # m = 0
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    # data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread, start_time in result:
        print(thread, start_time)



if __name__ == "__main__":
    main()
