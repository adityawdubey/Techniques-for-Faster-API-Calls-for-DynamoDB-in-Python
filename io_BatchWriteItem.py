import boto3
from boto3.dynamodb.conditions import Key
import time

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Orders1')

# Function to generate sample data
def generate_sample_data(start_index, end_index):
    """
    Generates a list of dictionaries representing sample data to insert into DynamoDB.
    """
    return [{'user_id': f'user{i}', 'data': f'some_data_{i}'} for i in range(start_index, end_index)]

def batch_write(table, items):
    """
    Batch writes multiple items to a DynamoDB table.
    """
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)
    print(f'Successfully wrote {len(items)} items to the table.')

def main():
    start_time = time.time()

    # Perform 4 batch write operations
    total_operations = 4
    batch_size = 25  # Maximum number of items in a batch write
    for i in range(total_operations):
        # Generate a batch of 25 items for each operation
        items_to_insert = generate_sample_data(i * batch_size + 1, (i + 1) * batch_size + 1)
        batch_write(table, items_to_insert)

    end_time = time.time()
    print(f"4 Batch Write Operations Completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
