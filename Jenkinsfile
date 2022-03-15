pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {  
                sh'''rm -rf change
                git clone https://github.com/Gautham-kukutla/gitchanges.git change
                '''
            }}
        stage('Git Modification Check') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'gittoken', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {

                sh'''pip install --upgrade autopep8
                cd change
                pwd
                git config --global user.email "gautham.kukutla@gmail.com"
                git config --global user.name "Gautham-kukutla"
                chmod +x script.sh
                ./script.sh
                
                '''
                }}
        }
    }
}
