def lambda_handler(event, context):

    message = f"Thank you for submitting data. You submitted the following. Date {event['date']} at location {event['location']}, number of red widgets sold was {event['red_sold']}, number of blue widgets sold was {event['blue_sold']}, number of green widgets sold was {event['green_sold']}."

    return {"Notes": message}
