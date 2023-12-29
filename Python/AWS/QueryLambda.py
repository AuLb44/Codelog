import boto3

def datesort(data):
    return data['InputDate']

def lambda_handler(event,context):

    Athena = boto3.client("athena")
    Done = "'Done'"
    Create = "'Create'"
    Query = 'SELECT DISTINCT * FROM "[INSERT DB.TABLE HERE]'
    string = event['rawQueryString']

    match string:
        case '0':
            Query += ' t1 WHERE col4 <> '+Create+' AND NOT EXISTS ( SELECT 1 FROM "[INSERT DB.TABLE HERE]" t2 WHERE t1.col2 = t2.col2 AND t2.col4 = '+Done+') ORDER BY col6 DESC'
        case '1':
            Query += ' WHERE col4='+Create+' ORDER BY col6 DESC;'
        case '2':
            Query += ' WHERE NOT col4 <> '+Create+' AND col4 <> '+Done+' ORDER BY col6 DESC;'
        case '9':
            Query += ' ORDER BY col6 DESC;'

    response = Athena.start_query_execution(
        QueryString = Query,
        QueryExecutionContext = {'Database': '[[INSERT DB HERE]]',},
        ResultConfiguration = {'OutputLocation':'[INSERT S3 LOCATION HERE]'}
    )

    QueryID = response[ "QueryExecutionId" ]
    State = "STARTED"
    
    while State != "SUCCEEDED" and State != "FAILED":
        State = Athena.get_query_execution(QueryExecutionId = QueryID)["QueryExecution"]["Status"]["State"]
        print("StateOf "+QueryID+" = "+State)

    if State != "FAILED":
        Results = Athena.get_query_results(QueryExecutionId = QueryID)["ResultSet"]
        data = []
        Date = ''
        for i in Results['Rows'][1:]:
            for field in i:
                if "GMT" in field:
                    """ Thu Oct 19 2023 13:29:19 GMT-0400 (Eastern Daylight Time) """
                    """ 0123456789 """
                    Date = field[field.index(' ')+1:field.index(':')-2].strip()
                    Date = datetime.strptime(Date,'%b %d %Y').date()
            try:
                x = {
                    "KitNum": i['Data'][0]['VarCharValue'],
                    "LotNum": i['Data'][2]['VarCharValue'],
                    "WONum": i['Data'][1]['VarCharValue'],
                    "ProcessStep": i['Data'][4]['VarCharValue'],
                    "QTY": i['Data'][3]['VarCharValue'],
                    "USER": i['Data'][7]['VarCharValue'],
                    "DEPT": i['Data'][8]['VarCharValue'],
                    "InputDate": str(Date),
                    "PSDate": i['Data'][5]['VarCharValue'],
                    "Comments": i['Data'][9]['VarCharValue'],
                    "TimeNeeded": i['Data'][10]['VarCharValue'],
                    "QuantityNeeded": i['Data'][11]['VarCharValue']
                }
            except:
                x = {
                    "KitNum": i['Data'][0]['VarCharValue'],
                    "LotNum": i['Data'][2]['VarCharValue'],
                    "WONum": i['Data'][1]['VarCharValue'],
                    "ProcessStep": i['Data'][4]['VarCharValue'],
                    "QTY": i['Data'][3]['VarCharValue'],
                    "USER": i['Data'][7]['VarCharValue'],
                    "DEPT": i['Data'][8]['VarCharValue'],
                    "InputDate": str(Date),
                    "PSDate": i['Data'][5]['VarCharValue'],
                    "Comments": i['Data'][9]['VarCharValue'],
                    "TimeNeeded": '',
                    "QuantityNeeded": ''
                }
            data.append(x)
        data.sort(key=datesort,reverse=True)
        return(data)
    return("Athena Exectuion Failed")