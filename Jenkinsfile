pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    def branchName = 'main'  // Change to the branch you want to build
                    git branch: branchName, url: 'https://github.com/009MHz/lab_wright.git', credentialsId: 'github-credentials-main'
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                    python -m venv venv
                    venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    venv\\Scripts\\activate
                    pytest .\tests\ --headless
                '''
            }
        }
    }

    post {
        always {
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
