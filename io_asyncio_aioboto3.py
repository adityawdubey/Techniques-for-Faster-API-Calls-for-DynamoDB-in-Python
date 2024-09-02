# Asyncio Example with aioboto3

import asyncio
import aioboto3
import time

# Function to perform asynchronous DynamoDB put_item
async def put_item_async(client, user_id):
    response = await client.put_item(
        TableName='Orders3',
        Item={
            'user_id': {'S': user_id}
        }
    )
    return response

# Asynchronous function to test the asyncio implementation
async def test_asyncio():
    session = aioboto3.Session()  # Create an aioboto3 session
    start_time = time.time()
    async with session.client('dynamodb', region_name='us-east-2') as client:
        tasks = [put_item_async(client, f"user_{i}") for i in range(100)]
        await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Asyncio with aioboto3; Execution time: {end_time - start_time:.5f} seconds")

# Run the asyncio test
if __name__ == "__main__":
    asyncio.run(test_asyncio())

