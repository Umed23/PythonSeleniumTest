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

                REM Create virtual environment if it doesn't exist
                if not exist "venv" (
                    "${PYTHON_PATH}" -m venv venv
                )

                REM Activate virtual environment
                call venv\\Scripts\\activate

                REM Upgrade pip
                python -m pip install --upgrade pip

                REM Install dependencies; fail gracefully if conflicts occur
                python -m pip install -r requirements.txt || (
                    echo ERROR: pip install failed. Check for version conflicts.
                    exit /b 1
                )
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat """
                REM Ensure reports folder exists
                if not exist reports mkdir reports

                REM Activate virtual environment
                call venv\\Scripts\\activate

                REM Run pytest with JUnit XML output
                python -m pytest --junitxml=reports\\test-results.xml
                """
            }
            post {
                always {
                    // Archive JUnit report
                    junit 'reports/test-results.xml'
                    archiveArtifacts artifacts: 'reports/test-results.xml', fingerprint: true
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}
