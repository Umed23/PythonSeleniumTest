pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\acer\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        VENV_DIR = "venv"
        REPORT_DIR = "reports"
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
                REM Check Python
                if not exist "${PYTHON_PATH}" (
                    echo Python not found at ${PYTHON_PATH}
                    exit /b 1
                )

                REM Create virtual environment
                "${PYTHON_PATH}" -m venv ${VENV_DIR}

                REM Activate virtual environment
                call ${VENV_DIR}\\Scripts\\activate

                REM Upgrade pip
                python -m pip install --upgrade pip

                REM Install dependencies; ignore errors for packages that fail
                echo Installing requirements with fallback for build failures...
                for /f "tokens=*" %%i in (requirements.txt) do (
                    echo Installing %%i
                    python -m pip install %%i || (
                        echo WARNING: Failed to install %%i, continuing...
                    )
                )
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat """
                REM Activate virtual environment
                call ${VENV_DIR}\\Scripts\\activate

                REM Run pytest and generate JUnit XML report
                pytest --junitxml=${REPORT_DIR}\\test-results.xml || (
                    echo WARNING: Some tests failed
                )
                """
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: "${REPORT_DIR}/test-results.xml"
                }
            }
        }
    }

    post {
        always {
            echo "Archiving artifacts and test reports..."
            archiveArtifacts artifacts: '**/test-results.xml', fingerprint: true
        }
    }
}
