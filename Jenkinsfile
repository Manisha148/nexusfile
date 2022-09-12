stage('Build ImG From Docker file'){
    sh 'docker build -t name .'
}
stage('Push Docker Images to Nexus Registry'){
    sh 'docker push http://54.211.84.17:8081/repository/demorep/'
}
stage('Docker Nexus Auth'){
    sh 'docker login -u admin -p verma12345 http://54.211.84.17:8085/'
}
