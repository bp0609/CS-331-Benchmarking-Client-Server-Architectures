#!/bin/bash

# Check if correct arguments are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 <server_script> <client_script> <port>"
    exit 1
fi

SERVER_SCRIPT=$1
CLIENT_SCRIPT=$2
PORT=$3
# Get outfile name from server script and add /result folder path in front
OUTPUT_FILE="./results/$(echo $SERVER_SCRIPT | cut -d'.' -f1).txt"

# Function to start the server in the background
start_server() {
    echo "Starting server: $SERVER_SCRIPT..."
    python3 "$SERVER_SCRIPT" $PORT &
    SERVER_PID=$!
    sleep 2  # Give server time to start
}

# Function to stop the server
stop_server() {
    echo "Stopping server..."
    kill $SERVER_PID
    wait $SERVER_PID 2>/dev/null
}

# Remove old results file
rm -f $OUTPUT_FILE
echo "Clients,Execution Time (s)" > $OUTPUT_FILE  # Header for CSV file

# Start the server
start_server

# Run benchmarks with different concurrent client counts (10, 20, ..., 100)
for CLIENT_COUNT in {10..20..10}; do
    echo "Running $CLIENT_COUNT concurrent clients..."
    
    START_TIME=$(date +%s.%N)
    pids=()
    # Run multiple clients in parallel
    for ((i=1; i<=CLIENT_COUNT; i++)); do
        python3 "$CLIENT_SCRIPT" $PORT &  # Background execution
        pids+=($!)  # Store client PID
    done

    # Wait only for client processes
    for pid in "${pids[@]}"; do
        wait $pid
    done
    # wait  # Wait for all clients to finish

    END_TIME=$(date +%s.%N)
    EXEC_TIME=$(awk "BEGIN {print $END_TIME - $START_TIME}")  # Calculate execution time

    echo "$CLIENT_COUNT,$EXEC_TIME" >> $OUTPUT_FILE  # Save result
    echo "Completed $CLIENT_COUNT clients in $EXEC_TIME seconds."
    sleep 1
done

# Stop the server after all tests
stop_server

echo "Benchmarking complete! Results saved in $OUTPUT_FILE."
