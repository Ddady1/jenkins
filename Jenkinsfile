pipeline {
    agent any

//    environment {
//        REGISTRY_URL = "352708296901.dkr.ecr.eu-west-1.amazonaws.com"
//        IMAGE_TAG = "0.0.$BUILD_NUMBER"
//        IMAGE_NAME = "ddady-jenkins-rep"
//    }

    stages {
        stage('Build') {
            steps {
                sh '''
                aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 352708296901.dkr.ecr.eu-west-1.amazonaws.com
                docker build -t ddady-jenkins-rep .
                docker tag ddady-jenkins-rep 352708296901.dkr.ecr.eu-west-1.amazonaws.com/ddady-jenkins-rep:0.0.$BUILD_NUMBER
                docker push 352708296901.dkr.ecr.eu-west-1.amazonaws.com/ddady-jenkins-rep:0.0.$BUILD_NUMBER
                 '''
            }

        }


    }
 }