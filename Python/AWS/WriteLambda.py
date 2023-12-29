import boto3

def lambda_handler(event, context):
    # create a boto3 client for Athena
    athena = boto3.client('athena')
    
    string = event['rawQueryString']
    string = string.replace("%20", " ")
    components = string.split("&")
    
    KitNum = components[0].split("=")[1]
    LotNum = components[1].split("=")[1]
    WONum = components[2].split("=")[1]
    ProcessStep = components[3].split("=")[1]
    qty = components[4].split("=")[1]
    user = components[5].split("=")[1]
    dept = components[6].split("=")[1]
    InputDate = components[7].split("=")[1]
    PSDate = components[8].split("=")[1]
    Comments = components[9].split("=")[1]
    TimeNeeded = components[10].split("=")[1]
    QuantityNeeded = components[11].split("=")[1]

    # set the Athena query string
    query = "INSERT INTO [INSERT DB HERE] VALUES ('"+KitNum+"', '"+LotNum+"', '"+WONum+"', '"+qty+"', '"+ProcessStep+"', '"+PSDate+"', '"+InputDate+"', '"+user+"', '"+dept+"', '"+Comments+"', '"+TimeNeeded+"', '"+QuantityNeeded+"')"    
        
    print(query)
        
    # execute the Athena query
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': '[INSERT DB HERE]'
        },
        ResultConfiguration={
            'OutputLocation': '[INSERT S3 LOCATION HERE]'
        }
    )
    
    QueryID = response[ "QueryExecutionId" ]
    State = "STARTED"

    while State != "SUCCEEDED" and State != "FAILED":
        response = athena.get_query_execution(QueryExecutionId = QueryID)
        State = response["QueryExecution"]["Status"]["State"]
        print("StateOf "+QueryID+" = "+State)
    if State != "FAILED":
        print( "Athena Write Succeeded")
    return{
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "message": State
        }
    }