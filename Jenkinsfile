pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = "ap-south-1"
        STACK_NAME = "jenkins-sam-pipeline"
    }

    stages {

        stage('Checkout Repo') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/PrajYeX/Calci2-App-Devops.git'
            }
        }

        stage('Run Tests') {
            steps {
                // Use python3 -m pip for safer path resolution
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                    python3 -m pip install pytest
                    python3 -m pytest src/tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t sam-app .
                '''
            }
        }

        stage('SAM Build') {
            steps {
                sh 'sam build'
            }
        }

        stage('SAM Deploy') {
            steps {
                sh '''
                    sam deploy \
                        --stack-name $STACK_NAME \
                        --capabilities CAPABILITY_IAM \
                        --resolve-s3 \
                        --no-confirm-changeset \
                        --no-fail-on-empty-changeset
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully 🚀'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
