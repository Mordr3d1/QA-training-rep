pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        git(url: 'https://github.com/Mordr3d1/QA-training-rep', branch: 'main')
        sh '''python3 test_api.py
'''
      }
    }

  }
}