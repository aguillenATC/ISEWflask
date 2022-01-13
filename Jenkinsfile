pipeline {
    agent any //{ docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('Testeo') {
            sh 'coverage run -m pytest'
        }
        stage('Lanza') {
            steps {
                sh 'export FLASK_APP=isew ; export FLASK_ENV=development ; flask run'
            }
        }
    }
}
