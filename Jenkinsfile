pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Umed23/PythonSeleniumTest.git'
            }
        }

        stage('Setup Environment') {
            steps {
                bat """
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat """
                call venv\\Scripts\\activate
                pytest -v --maxfail=1 --disable-warnings --junitxml=report.xml
                """
            }
        }
    }

    post {
        always {
            junit 'report.xml'
            archiveArtifacts artifacts: '**/report.xml', fingerprint: true
        }
    }
}
