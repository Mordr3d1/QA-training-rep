pipeline {
  agent any
  stages {
    stage('Checkout + test') {
      steps {
        git(url: 'https://github.com/Mordr3d1/QA-training-rep', branch: 'main')
        sh 'git clone https://github.com/Mordr3d1/QA-training-rep.git'
        sh 'git fetch https://github.com/Mordr3d1/QA-training-rep.git'
        sh 'pytest'
        cleanWs(cleanWhenAborted: true, cleanWhenFailure: true, cleanWhenNotBuilt: true, cleanWhenSuccess: true, cleanWhenUnstable: true, cleanupMatrixParent: true, deleteDirs: true, disableDeferredWipeout: true)
      }
    }

  }
}