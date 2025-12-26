# Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Install dependencies from the root of the project
COPY requirements.txt .
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy application code while preserving the 'calculator' module structure
COPY src/calculator/ ${LAMBDA_TASK_ROOT}/calculator/

# Set the updated Lambda handler path
CMD [ "calculator.app.lambda_handler" ]
