pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        git(url: 'https://github.com/Mordr3d1/QA-training-rep', branch: 'main')
        sh '''sudo apt-get install python3-pip



'''
        sh 'pip install fastapi'
        sh 'pip install "uvicorn[standard]'
      }
    }

  }
}