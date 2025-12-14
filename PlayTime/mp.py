from multiprocessing import Pool

def square(x):
    """A simple function to be executed in parallel."""
    return x * x

if __name__ == '__main__':
    # Create a Pool with a specified number of worker processes (e.g., 4)
    with Pool(processes=4) as p:
        # Define the input data
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Use map to apply the 'square' function to each item in 'data'
        results = p.map(square, data)

        print(f"Original data: {data}")
        print(f"Squared results: {results}")