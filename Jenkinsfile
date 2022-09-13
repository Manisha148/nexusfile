stage('Build ImG From Docker file'){
    sh 'docker build -t python .'
}
stage('Push Docker Images to Nexus Registry'){
    sh 'docker push http://54.166.219.95:8081/repository/pipeline21/'
}
stage('Docker Nexus Auth'){
    sh 'docker login -u admin -p verma12345 http://54.166.219.95:8085/'
}
