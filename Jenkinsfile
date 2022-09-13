pipeline{
  agent any
  environment {
        imageName = "docker-image"
        registryCredentials = "nexus"
        registry = "54.166.219.95:8085/"
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
    stage('Uploading to Nexus') {
     steps{  
         script {
            <configuration>
        <serverId>nexus</serverId>
        <nexusUrl>http://http://54.166.219.95:8081//nexus/</http://54.166.219.95:8081/repository/pipeline21/>
      </configuration> 
           </script>
           {
             dockerImage.push('latest')
          }
        }
      }
    }
  }
}
