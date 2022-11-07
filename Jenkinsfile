pipeline {
    agent any

    environment {
        REGISTRY_URL = "352708296901.dkr.ecr.eu-west-1.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "ddady-jenkins-rep"
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                docker build -t $IMAGE_NAME .
                docker tag $IMAGE_NAME $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                 '''
            }

        }
        post {
            always {
                sh '''
                docker rmi $IMAGE_NAME $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }


    }
 }