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
                    export PYTHONPATH=${WORKSPACE}/src
                    python3 -m pytest
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
                withEnv(['PATH+SAM=/usr/local/bin']) {
                    sh 'sam build'
                }
            }
        }

        stage('SAM Deploy') {
            steps {
                withCredentials([aws(credentialsId: 'aws-credentials')]) {
                    sh '''
                        sam deploy \
                            --stack-name $STACK_NAME \
                            --capabilities CAPABILITY_IAM \
                            --resolve-s3 \
                            --resolve-image-repos \
                            --no-confirm-changeset \
                            --no-fail-on-empty-changeset
                    '''
                }
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
