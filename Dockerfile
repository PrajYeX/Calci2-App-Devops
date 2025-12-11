# Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Install dependencies
COPY src/calculator/requirements.txt .
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy application code
COPY src/calculator/ ${LAMBDA_TASK_ROOT}

# Lambda handler
CMD [ "app.lambda_handler" ]
