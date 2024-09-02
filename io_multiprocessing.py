# Multiprocessing Example

import boto3
import multiprocessing
import time

# Function to put an item using a new DynamoDB client
def put_item_process(user_id):
    dynamodb = boto3.client('dynamodb', region_name='us-east-2')
    dynamodb.put_item(
        TableName='Orders1',
        Item={
            'user_id': {'S': user_id}
        }
    )

def test_multiprocessing():
    start_time = time.time()
    
    # Create a pool of processes and map the put_item function to each user_id
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(put_item_process, [f"user_{i}" for i in range(100)])

    end_time = time.time()
    print(f"Multiprocessing; Execution time: {end_time - start_time:.5f} seconds")

# Run the multiprocessing test
if __name__ == '__main__':
    test_multiprocessing()
