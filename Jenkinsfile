pipeline {
    agent any

    triggers {
        githubPush()     // <--- THIS ENABLES GITHUB WEBHOOKS
    }

    environment {
        REPO_URL = "https://github.com/serveshtripathi1997/profile-app.git"
        DEPLOY_PATH = "/home/serveshtripathi/profile-app"
        IMAGE_NAME = "profile-app:latest"
        CONTAINER_NAME = "profile-app"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git url: "${REPO_URL}",
                    branch: 'main',
                    credentialsId: 'github-creds'
            }
        }

        stage('Sync Code to Deploy Folder') {
            steps {
                sh """
                    rm -rf ${DEPLOY_PATH}
                    mkdir -p ${DEPLOY_PATH}
                    cp -r * ${DEPLOY_PATH}/
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    cd ${DEPLOY_PATH}
                    docker build -t ${IMAGE_NAME} .
                """
            }
        }

        stage('Stop Old Container') {
            steps {
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Deploy New Container') {
            steps {
                sh """
                    docker run -d --name ${CONTAINER_NAME} -p 9000:5000 ${IMAGE_NAME}
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
