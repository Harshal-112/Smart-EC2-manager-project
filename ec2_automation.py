import boto3
from botocore.exceptions import ClientError,WaiterError

ec2 = boto3.client('ec2', region_name='ap-south-1')

def stopped_instances():
    try:
        result = []
        response = ec2.describe_instances(Filters=[{'Name':'instance-state-name','Values':['stopped']}])

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                result.append(instance_id)
            
        return result
    except ClientError as e:
        print(f"Error Code: {e.response['Error']['Code']}")
        print(f"Error Message: {e.response['Error']['Message']}")
        return []
    
def start_instance(instances):
    try:
        if not instances:
            return "No stopped instances found"
        else:
            for index,instance_id in enumerate(instances):
                print(f"{index+1}. {instance_id}")

            try:
                cho = int(input("Enter the number of the instance to start: "))
                selected_id = instances[cho-1]
                print(f"Starting {selected_id}...")
                ec2.start_instances(InstanceIds=[selected_id])
            except ValueError:
                return "[ERROR] Please enter a valid number not text"
            except IndexError:
                return "[ERROR] Number is not in a list"
            
            try:
                waiter = ec2.get_waiter('instance_running')
                waiter.wait(InstanceIds=[selected_id])
            except WaiterError as e:
                print(e)

            return "[SUCCESS] Selected instance is running"
        
    except ClientError as e:
        print(f"Error Code: {e.response['Error']['Code']}")
        print(f"Error Message: {e.response['Error']['Message']}")
        return []
    
def running_instances():
    try:
        result = []
        response = ec2.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}])

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                public_ip = instance.get('PublicIpAddress','No Public Ip')
                result.append((instance_id,state,public_ip))
        return result

    except ClientError as e:
        print(f"Error Code: {e.response['Error']['Code']}")
        print(f"Error Message: {e.response['Error']['Message']}")
        return []

def stop_instances(instances):
    try:
        if not instances:
            return "No running instances found"
        else:
            for index,instance_id in enumerate(instances):
                print(f"{index+1}. {instance_id}")
            try:
                cho = int(input("Enter the number of the instance to stop: "))
                selected_id = instances[cho-1]
                print(f"Stopping {selected_id}...")
                ec2.stop_instances(InstanceIds=[selected_id])
            except ValueError:
                return "[ERROR] Please enter a valid number not text"
            except IndexError:
                return "[ERROR] Number is not in a list"
            
            try:
                waiter = ec2.get_waiter('instance_stopped')
                waiter.wait(InstanceIds=[selected_id])
            except WaiterError as e:
                print(e)

            return "[SUCCESS] Selected instance is stopped"
            
    except ClientError as e:
        print(f"Error Code: {e.response['Error']['Code']}")
        print(f"Error Message: {e.response['Error']['Message']}")
        return []
    
while True:
    print("\n1. Show stopped instances")
    print("\n2. Start instances")
    print("\n3. Show running instances")
    print("\n4. Stop instance")
    print("\n5. Exit")
    ch = input("Enter your choice: ")
    
    if ch == '1':
        stopped = stopped_instances()
        if not stopped:
            print("No stopped instances found")
        else:
            for i in stopped:
                print(f"- {i}")

    elif ch == '2':
        stopped = stopped_instances()
        if not stopped:
            print("No stopped instances found")
        else:
            print(start_instance(stopped))
    

    elif ch == '3':
        instances = running_instances()
        if not instances:
            print("No running instances found")
        else:
            for inst in instances:
                print(f"ID: {inst[0]}, State: {inst[1]}, IP: {inst[2]}")

    elif ch == '4':
        instance_ids = [inst[0] for inst in running_instances()]
        if not instance_ids:
            print("No running instances found")
        else:
            print(stop_instances(instance_ids))
                

    elif ch == '5':
        break

    else:
        print("Enter valid choice")