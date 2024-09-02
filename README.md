# Overview

This project aims to explore different concurrency models and their impact on the performance of DynamoDB's put_item operation. The objective is to compare synchronous, threading, asynchronous (using asyncio and aioboto3), and multiprocessing approaches, highlighting their strengths and weaknesses for I/O-bound tasks like database interactions.

Read full blog here: https://adityadubey.cloud/techniques-for-faster-api-calls-for-dynamodb-in-python

# Key Features

- The project includes code examples for each concurrency model, allowing you to run experiments and analyze the results.
- The blog post provides detailed performance comparisons and insights into the factors affecting execution time.
- Real-World Use Cases: Understand when to use different concurrency methods based on your specific requirements.
- Learn recommended practices for optimizing DynamoDB performance and minimizing latency.
    
Each of these methods has its own strengths and is best suited for different types of tasks. They mainly differ in how they handle I/O-bound and CPU-bound processes.


# Getting Started

### 1. Clone the Repository:
```
git clone https://github.com/your-username/concurrency-in-dynamodb.git
```

### 2. Install Dependencies
```
pip install boto3 aioboto3 asyncio
```

### 3. Configure AWS Credentials: Set your AWS credentials in your environment variables or configure them using the AWS CLI.


# Usage

- Run Experiments: Execute the Python scripts provided in the project to perform the concurrency tests.
- Review the output of the experiments to compare execution times and identify the most efficient concurrency model for your use case.

## Results

![Image.png](https://res.craft.do/user/full/3aa63f74-732e-6a57-0633-5367c08afcb6/doc/3F1DDAE1-67C3-4A80-863F-A853244975C1/F3D6D30B-ABCF-4AA2-96CE-67BEBF511479_2/ArucDxa39aySeaPvydEnejEd27nkdUtDihOcavKMWLsz/Image.png align="left")

Based on the results, we can say that asynchronous approaches, like aioboto3 and asyncio with boto3, significantly outperform both synchronous and threading methods for I/O-bound tasks such as DynamoDB interactions. Threading offers some performance improvement over synchronous execution but may be less efficient than asynchronous methods due to thread management overhead. On the other hand, multiprocessing offers true parallelism and excels with CPU-bound tasks, but it doesn’t provide the same performance benefits for I/O-bound problems.

# FAQs

### **Why Synchronous vs. Asynchronous Matters ?**

When it comes to managing tasks with a software application, the selection of either synchronous-al process or a non-synchronous process can either enhance or hinder efficiency and performance. For instance think of an online shop that consists of customers placing orders. In the synchronous method, each intermediate step related to the order such as clearing payment, reaching out to customers, sending confirmation email, or even updating the stocks happens one after another and not simultaneously. This order fixing cause unnecessary delays on the other tasks that might require quick responses hence seeing the whole order processing system take too long especially when there are many orders placed.

On the other hand, an asynchronous approach encourages the parallel execution of these tasks. While the payment confirmation is awaited, inventory can be updated and a confirmation message can be drafted ready for dispatch once the payment goes through. This method is advantageous as it frees the system to be active on several processes at the same time without hindering performance. Even with such an approach, there is a limitation that if certain activities will be postponed, other ones that are already in progress shall also be executed causing an earlier than expected completion of the order.

Nonetheless, just because asynchronous methods have some benefits, they can't be used for tasks that need to be done in order. For example, in financial transactions like transferring money from one account to another, each step depends on the previous one. Using an asynchronous method here would cause confusion. In such scenarios, high-velocity synchronous processing benefits all in that the activities done step by step.

### What is an example use case for asynchronous programming with AWS?

A prime example of asynchronous programming with AWS is processing and validating configuration changes across multiple AWS Lambda functions. Suppose you have a system that dynamically updates various configurations across different services, such as modifying security settings, updating resource limits, or changing application parameters.

In this scenario, you might need to validate these changes by triggering multiple Lambda functions in parallel, each responsible for checking a specific aspect of the configuration. Asynchronous programming allows you to invoke all these Lambda functions concurrently rather than waiting for each to complete sequentially. This parallel execution significantly reduces the total time required for validation and helps in quickly applying changes across your infrastructure. By leveraging AWS services like AWS Step Functions or AWS EventBridge for managing and orchestrating these asynchronous invocations, you can handle high concurrency efficiently and improve the overall responsiveness of your system.

[https://docs.aws.amazon.com/lambda/latest/api/API\_Invoke.html](https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html

https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/processing-events-asynchronously-with-amazon-api-gateway-and-amazon-dynamodb-streams.html

https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/processing-events-asynchronously-with-amazon-api-gateway-and-amazon-dynamodb-streams.html

# Resources

[Use the DynamoDB Enhanced Client API asynchronously - AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-async.html#:~:text=If%20your%20application%20requires%20non,you%20can%20use%20the%20DynamoDbEnhancedAsyncClient%20.)

[https://stackoverflow.com/questions/67092070/why-do-we-need-async-for-and-async-with](https://stackoverflow.com/questions/67092070/why-do-we-need-async-for-and-async-with)

[https://en.wikipedia.org/wiki/Async/await](https://en.wikipedia.org/wiki/Async/await)

[https://www.freecodecamp.org/news/asynchronous-programming-in-javascript/](https://www.freecodecamp.org/news/asynchronous-programming-in-javascript/)

# **Further Exploration**

Consider exploring techniques for optimizing CPU-bound tasks, such as using multiprocessing or GPU acceleration, to improve your application's performance in compute-intensive scenarios.

Check out asynchronous programming in other contexts. While this blog focuses on DynamoDB, asynchronous programming can benefit many applications beyond database interactions, such as handling web requests, file I/O, and other network operations.

Gain insights into the factors affecting DynamoDB latency and learn strategies for minimizing delays to enhance performance for both synchronous and asynchronous operations.

Review AWS's recommendations for effectively querying and scanning data in DynamoDB, focusing on maximizing performance and minimizing costs.

[Understanding Amazon DynamoDB latency | Amazon Web Services](https://aws.amazon.com/blogs/database/understanding-amazon-dynamodb-latency/)

[Use parallelism to optimize querying large amounts of data in Amazon DynamoDB | Amazon Web Services](https://aws.amazon.com/blogs/database/use-parallelism-to-optimize-querying-large-amounts-of-data-in-amazon-dynamodb/)

[Best practices for querying and scanning data - Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html)