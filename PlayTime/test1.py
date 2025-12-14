import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from multiprocessing import Process, Queue, set_start_method
import time
import os
import queue

# Make sure to use 'spawn' to avoid CUDA reinitialization issues
try:
    set_start_method('spawn')
except RuntimeError:
    pass

# Dummy model and data (replace with your real model/data)
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(1024, 10)

    def forward(self, x):
        return self.fc(x)

# Worker function that runs on each GPU process
def worker_process(rank, world_size, task_queue, result_queue):
    """
    rank: process id (0 to world_size-1)
    task_queue: contains batches of data
    result_queue: collect results or losses
    """
    # Set device for this process
    device = torch.device(f"cuda:{rank % torch.cuda.device_count()}")
    print(f"Process {rank} using {device}")

    # Move model to GPU
    model = SimpleNet().to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    while True:
        try:
            # Get next batch (non-blocking with timeout)
            batch = task_queue.get(timeout=1)
        except queue.Empty:
            print(f"Process {rank} exiting: no more tasks")
            break

        x, y = batch
        x = x.to(device)
        y = y.to(device)

        optimizer.zero_grad()
        output = model(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()

        # Send result back (e.g., loss)
        result_queue.put((rank, loss.item()))

    print(f"Process {rank} finished")

def main():
    world_size = 4  # Number of parallel processes (adjust to your GPU count)
    num_batches = 100

    # Create dummy data
    x = torch.randn(10000, 1024)
    y = torch.randn(10000, 10)
    dataset = TensorDataset(x, y)
    dataloader = DataLoader(dataset, batch_size=128, shuffle=True)

    # Queues for task distribution and result collection
    task_queue = Queue()
    result_queue = Queue()

    # Fill task queue
    for i, batch in enumerate(dataloader):
        if i >= num_batches:
            break
        task_queue.put(batch)

    print(f"Enqueued {task_queue.qsize()} batches")

    # Start worker processes
    processes = []
    for rank in range(world_size):
        p = Process(target=worker_process, args=(rank, world_size, task_queue, result_queue))
        p.start()
        processes.append(p)

    # Collect results (optional)
    total_loss = 0
    count = 0
    start_time = time.time()

    while count < num_batches:
        try:
            rank, loss = result_queue.get(timeout=10)
            total_loss += loss
            count += 1
            if count % 20 == 0:
                print(f"Processed {count}/{num_batches} batches, avg loss: {total_loss/count:.4f}")
        except queue.Empty:
            break

    elapsed = time.time() - start_time
    print(f"\nFinished training in {elapsed:.2f} seconds")
    print(f"Final average loss: {total_loss/count:.4f}")

    # Clean up
    for p in processes:
        p.join()

if __name__ == "__main__":
    main()