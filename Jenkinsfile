pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        git(url: 'https://github.com/Mordr3d1/QA-training-rep', branch: 'main')
        sh 'apt install sudo'
        sh 'sudo su'
        sh '''apt-get install python3-pip



'''
        sh 'pip install fastapi'
        sh 'pip install "uvicorn[standard]'
      }
    }

  }
}