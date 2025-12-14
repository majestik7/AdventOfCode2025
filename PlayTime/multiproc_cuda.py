import multiprocessing
import os

def gpu_worker(gpu_id, data):
    # Set the CUDA_VISIBLE_DEVICES environment variable for this process
    os.environ['CUDA_VISIBLE_DEVICES'] = str(gpu_id)
    print(gpu_id)
    # Import GPU-aware libraries (e.g., PyTorch, TensorFlow) AFTER setting the env variable
    import torch
    
    # Perform GPU computation using the assigned GPU
    device = torch.device(f"cuda:{gpu_id}") 
    tensor_data = torch.tensor(data).to(device)
    result = tensor_data * 2 # Example operation
    print(f"Process on GPU {gpu_id} processed data: {result.cpu().numpy()}")
    return result.cpu().numpy()

if __name__ == '__main__':
    num_gpus = 2 # Assuming 2 GPUs are available
    all_data = [[1, 2, 3], [4, 5, 6]] # Data for each process

    with multiprocessing.Pool(num_gpus) as pool:
        # Map each data chunk to a GPU worker process
        results = pool.starmap(gpu_worker, [(i, all_data[i]) for i in range(num_gpus)])
    
    print("All results:", results)