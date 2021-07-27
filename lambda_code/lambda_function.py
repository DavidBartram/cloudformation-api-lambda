import json

def lambda_handler(event, context):

    try:
        message = f"Thank you for submitting data. You submitted the following. Location was {event['location']}, number of red widgets sold was {event['red_sold']}, number of blue widgets sold was {event['blue_sold']}, number of green widgets sold was {event['green sold']}"
    
    except:
        returnData = {"Notes":"Failed to receive data"}
                
    
    return returnData
