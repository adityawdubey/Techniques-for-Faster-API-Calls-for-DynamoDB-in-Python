# Non Concurrent

import boto3
import time

# Initialize boto3 DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-2')

def put_item(user_id):
    response = dynamodb.put_item(
        TableName='Orders1',
        Item={
            'user_id': {'S': user_id}
        }
    )
    return response

def test():
    start_time = time.time()
    
    for i in range(100):
        put_item(f"user_{i}")
    
    end_time = time.time()
    print(f"Synchronous; Execution time: {end_time - start_time:.5f} seconds")

# Run the synchronous test
test()
