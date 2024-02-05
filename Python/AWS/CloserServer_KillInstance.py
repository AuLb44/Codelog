import json
import boto3

def lambda_handler(event, context):
    #Define the contents of your shell script
    script = """
    echo "Hello World!" > /home/ec2-user/helloworld.txt
    pwd >> /home/ec2-user/helloworld.txt
    """
        
    #Define ec2 and ssm clients
    ec2_client = boto3.client("ec2", region_name='us-east-1')
    ssm_client = boto3.client('ssm')   
    
    #Gather of instances with tag defined earlier
    filtered_instances = ec2_client.describe_instances()

    #Reservations in the filtered_instances
    reservations = filtered_instances['Reservations']
    
    print(reservations['State']['Name'])
        
    return