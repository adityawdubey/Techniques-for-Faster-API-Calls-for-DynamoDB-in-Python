# Threading Example with ThreadPoolExecutor

import boto3
from concurrent.futures import ThreadPoolExecutor
import time

# Initialize boto3 DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-2')

def put_item(user_id):
    response = dynamodb.put_item(
        TableName='Orders2',
        Item={
            'user_id': {'S': user_id}
        }
    )
    return response

def test_threading():
    start_time = time.time()

    # Using ThreadPoolExecutor to manage a pool of threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit multiple put_item tasks to the executor
        futures = [executor.submit(put_item, f"user_{i}") for i in range(100)]

        # Optionally, wait for all futures to complete and handle exceptions
        for future in futures:
            try:
                # Get the result of the future
                future.result()
            except Exception as e:
                print(f"An error occurred: {e}")

    end_time = time.time()
    print(f"Threading; Execution time: {end_time - start_time:.5f} seconds")

# Run the threading test
test_threading()
