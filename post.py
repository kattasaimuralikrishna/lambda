import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('murali')

def lambda_handler(event, context):
    movies=event['movies']
    director=event['director']
    actress=event['actress']
    actor= event ['actor']
    language=event['language']
    try:
        table.put_item(Item={
            "movies":movies,
            "director" : director,
            "actress" : actress,
            "actor" : actor,
            "language":language
            
        })
        return "done"
    except:
        raise