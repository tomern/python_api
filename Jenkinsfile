pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                dir('web') {
                    script {
                         try {
                            sh 'docker rm -f app'
                         }
                         catch(exception){
                         }
                    }
                    sh 'docker build -t app .'
                    sh 'docker run -d -p 8083:5000 --name app app'
                }
            }
        }
        stage('Tests') {
            agent {
                dockerfile {
                    dir 'tests'
                    filename 'Dockerfile'
                    args '--link app'
                }
            }
            steps {
                dir('tests') {
                    sh 'pytest tests_api.py --junit-xml=reports/report.xml'
                }
            }
            post {
                always {
                    junit 'tests/reports/report.xml'
                }
            }
        }
    }
}