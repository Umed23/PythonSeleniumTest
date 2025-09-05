pipeline {
    agent any

    environment {
        // Full path to your Python executable
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

                REM Activate virtual environment
                call venv\\Scripts\\activate

                REM Upgrade pip
                "${PYTHON_PATH}" -m pip install --upgrade pip

                REM Install dependencies; fail gracefully if conflicts occur
                "${PYTHON_PATH}" -m pip install -r requirements.txt || (
                    echo ERROR: pip install failed. Check for version conflicts.
                    exit /b 1
                )
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat """
                call venv\\Scripts\\activate
                pytest -v --maxfail=1 --disable-warnings --junitxml=report.xml || (
                    echo ERROR: Tests failed
                    exit /b 1
                )
                """
            }
        }
    }

    post {
        always {
            echo "Archiving test reports..."
            // Archive JUnit report
            junit allowEmptyResults: true, testResults: 'report.xml'
            archiveArtifacts artifacts: '**/report.xml', fingerprint: true
        }
    }
}
