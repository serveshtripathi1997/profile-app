pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        DEPLOY_PATH = "/home/serveshtripathi/profile-app"
        IMAGE_NAME = "profile-app:latest"
        CONTAINER_NAME = "profile-app"
    }

    stages {

        stage('Sync Code to Deploy Folder') {
            steps {
                sh """
                    sudo rm -rf ${DEPLOY_PATH}
                    sudo mkdir -p ${DEPLOY_PATH}
                    sudo cp -r * ${DEPLOY_PATH}/
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    cd ${DEPLOY_PATH}
                    sudo docker build -t ${IMAGE_NAME} .
                """
            }
        }

        stage('Stop Old Container') {
            steps {
                sh """
                    sudo docker stop ${CONTAINER_NAME} || true
                    sudo docker rm ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Deploy New Container') {
            steps {
                sh """
                    sudo docker run -d --name ${CONTAINER_NAME} -p 9000:5000 ${IMAGE_NAME}
                """
            }
        }
    }

    post {
        success {
            echo "🚀 Deployment successful → http://localhost:9000/"
        }
        failure {
            echo "❌ Deployment failed."
        }
    }
}
