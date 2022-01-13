pipeline {
    agent any //{ docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('Testeo') {
            steps{
                echo 'Comenzamos los test...'
                sh 'coverage run -m pytest'
            }
        }
        stage('Lanza') {
            steps {
                echo 'Ejecutamos aplicación'
                sh 'export FLASK_APP=isew ; export FLASK_ENV=development ; flask run'
            }
        }
    }
}
