pipeline {
  agent any
  stages {
    stage('Checkout + test') {
      steps {
        git(url: 'https://github.com/Mordr3d1/QA-training-rep', branch: 'main')
        sh 'pytest test_api.py'
        cleanWs(cleanWhenAborted: true, cleanWhenFailure: true, cleanWhenNotBuilt: true, cleanWhenSuccess: true, cleanWhenUnstable: true, cleanupMatrixParent: true, deleteDirs: true, disableDeferredWipeout: true)
      }
    }

  }
}
