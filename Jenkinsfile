pipeline{
  agent any
  environment {
        imageName = "docker-image"
        registryCredentials = "nexus"
        registry = "http://54.166.219.95:8085/"
        dockerImage = ''
    }
  stages{
    stage('checkout'){
      steps{
         checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/Manisha148/nexusfile.git']]])
      }
    }
     stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imageName
        }
      }
    }
  }
}
stage('Push Docker Images to Nexus Registry'){
    sh 'docker push http://54.166.219.95:8081/repository/pipeline21/'
}
stage('Docker Nexus Auth'){
    sh 'docker login -u admin -p verma12345 http://54.166.219.95:8085/'
}
