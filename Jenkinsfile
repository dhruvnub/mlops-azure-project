pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\inYodreamzz\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat '"C:\\Users\\inYodreamzz\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" train.py'
            }
        }

        stage('Build Complete') {
            steps {
                echo 'Model training complete'
            }
        }
    }
}