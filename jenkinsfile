pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9' // Adjust as needed
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Use the correct credentialsId for the GitHub Personal Access Token
                git url: 'https://github.com/009MHz/lab_wright.git', credentialsId: 'github-credentials-main'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Setup a Python virtual environment and install dependencies
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Activate the virtual environment and run the tests
                sh '''
                    . venv/bin/activate
                    pytest --headless --maxfail=3 --disable-warnings --start-maximized
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
