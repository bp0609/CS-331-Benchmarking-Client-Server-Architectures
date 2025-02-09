#!/bin/bash

SERVER_SCRIPTS=("single_process_server.py" "multi_threaded_server.py" "multi_process_server.py")
CLIENT_SCRIPT="client.py"
PORT=8020
for i in {0..2}; do
    SERVER_SCRIPT=${SERVER_SCRIPTS[$i]}
    # Call benchmark.sh for each server script with port number
    ./benchmark.sh $SERVER_SCRIPT $CLIENT_SCRIPT $(($PORT + $i))
done

# Plot the results
python3 plot_results.py

echo "Benchmarking complete! Results saved in results folder."
