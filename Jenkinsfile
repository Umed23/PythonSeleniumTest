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
                REM Check if Python is available
                python --version
                if %ERRORLEVEL% NEQ 0 (
                    echo Python is not installed or not in PATH
                    exit /b 1
                )

                REM Create virtual environment
                python -m venv venv

                REM Activate virtual environment and install dependencies
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                python -m pip install -r requirements.txt
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
