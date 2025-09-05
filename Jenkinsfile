pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\acer\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Umed23/PythonSeleniumTest.git'
            }
        }

        stage('Setup Environment') {
            steps {
                bat """
                REM Check if Python exists
                if not exist "${PYTHON_PATH}" (
                    echo Python not found at ${PYTHON_PATH}
                    exit /b 1
                )

                REM Create virtual environment
                "${PYTHON_PATH}" -m venv venv

                REM Activate virtual environment and install dependencies
                call venv\\Scripts\\activate
                "${PYTHON_PATH}" -m pip install --upgrade pip
                "${PYTHON_PATH}" -m pip install -r requirements.txt
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
            echo "Archiving test reports..."
            junit 'report.xml'
            archiveArtifacts artifacts: '**/report.xml', fingerprint: true
        }
    }
}
