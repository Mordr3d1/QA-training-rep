pipeline {
  agent any
  stages {
    stage('Checkout + test') {
      steps {
        git(url: 'https://github.com/Mordr3d1/QA-training-rep', branch: 'main')
        sh 'git pull https://github.com/Mordr3d1/QA-training-rep.git'
        sh 'pytest'
      }
    }

  }
}