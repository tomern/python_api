pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                dir('web') {
                    sh 'docker build -t app .'
                    sh 'docker run -d -p 5000:5000 --name app app'
                }
            }
        }
        stage('Tests') {
            agent {
                dockerfile {
                    dir 'tests'
                    filename 'Dockerfile'
                }
            }
            steps {
                dir('tests') {
                    sh 'pytest -vv --junit-xml=reports/report.xml'
                }
            }
            post {
                always {
                    junit tests/reports/report.xml
                    sh 'docker rm -f app'
                }
            }
        }
    }
}