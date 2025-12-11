# app.py - for local testing or packaging as lambda handler

from calculator.core import add, sub, mul

def lambda_handler(event, context):
    # expects JSON: {"op": "add"|"sub"|"mul", "a": int, "b": int}
    op = event.get("op")
    a = event.get("a")
    b = event.get("b")
    if op == "add":
        result = add(a, b)
    elif op == "sub":
        result = sub(a, b)
    elif op == "mul":
        result = mul(a, b)
    else:
        return {"statusCode": 400, "body": {"error": "unknown op"}}
    return {"statusCode": 200, "body": {"result": result}}
