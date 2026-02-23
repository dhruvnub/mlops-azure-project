pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Build Complete') {
            steps {
                echo 'Model training complete'
            }
        }
    }
}