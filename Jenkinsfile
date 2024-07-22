pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/009MHz/lab_wright.git', credentialsId: 'github-credentials-main'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --headless
                '''
            }
        }
    }

    post {
        always {
            // Archive test reports and artifacts
            archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
            junit 'reports/**/*.xml'
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed.'
        }
    }
}
