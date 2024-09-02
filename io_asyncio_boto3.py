# Asynscio Example with boto3

import asyncio
import boto3
import functools
from time import perf_counter

# Initialize boto3 DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-2')

def put_item(user_id):
    """Synchronously put an item in the DynamoDB table."""
    response = dynamodb.put_item(
        TableName='Orders1',
        Item={
            'user_id': {'S': user_id}
        }
    )
    return response

async def async_boto3_example() -> float:
    """Asynchronously perform DynamoDB put_item operations using asyncio with boto3."""
    loop = asyncio.get_running_loop()
    start_time = perf_counter()
    # Create a list of tasks to run in the executor
    tasks = [
        loop.run_in_executor(None, functools.partial(put_item, f"user_{i}"))
        for i in range(100) 
    ]
    # Execute all the tasks concurrently
    await asyncio.gather(*tasks)
    end_time = perf_counter()
    return end_time - start_time

def main():
    elapsed_time = asyncio.run(async_boto3_example())
    print(f"Asyncio with boto3; Execution time: {elapsed_time:.5f} seconds")

# Run the main function
if __name__ == "__main__":
    main()


'''
Uses asyncio with run_in_executor to offload synchronous boto3 calls to a separate thread pool.
put_item function is synchronous and executed in a thread pool.
Tasks are created using loop.run_in_executor, which allows running synchronous code asynchronously by executing it in a thread pool.
'''