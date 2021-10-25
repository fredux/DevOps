
pipeline{
    agent any
    environment {
        NAME_APP = "juice-shop"
        PORT_APP = "3033"
    }
    
    stages {
        stage('Build da imagem'){
            
            steps {
                git url: 'https://github.com/juice-shop/juice-shop'
                script {
                    docker.build "$NAME_APP:latest"
                }
            }
        }

        stage('Executando Container'){
            steps {
                sh '''
                    if [ ! "$(curl -s localhost:$PORT_APP &> /dev/null)" ]; then
                    docker run -d --name $NAME_APP -p $PORT_APP:3000 $NAME_APP:latest
                    fi
                '''
            } 
        }
    }

    post {
        always{
            chuckNorris()
        }
        success {
            echo "Pipeline executado com sucesso!!"
        }
        failure {
            echo "Pipeline falhou!"
        }
    }
}
