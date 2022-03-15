pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {  
                sh'''rm -rf change
                git clone https://github.com/Gautham-kukutla/jenkinspost.git change
                '''
            }}
        stage ('test') {
        when {
            branch 'origin/main'
        }
        steps {
             echo 'Test stage main is executed.'
        }
    }
        stage ('Deploy') {
        when {
            branch 'origin/master'
        }
        steps {
             echo 'Test stage Master is executed.'
        }
    }
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
            }}
post { 
        always { 
            echo 'This is post always'
        }
    failure { 
            echo 'This is post failure'
        }
    unsuccessful{
        echo 'this is post unsuccessful'
    }
    success { 
            echo 'This is post success'
        }}
}
