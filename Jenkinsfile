pipeline {
  agent any
  stages {
    stage('Checkout + test') {
      steps {
        sh 'git clone https://github.com/Mordr3d1/QA-training-rep.git'
        git(url: 'https://github.com/Mordr3d1/QA-training-rep', branch: 'main')
        sh 'pytest'
      }
    }

  }
}