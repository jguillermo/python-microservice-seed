#!/usr/bin/env groovy

pipeline {
  agent any
  parameters {
    booleanParam(
      name: 'REGISTRY',
      defaultValue: false,
      description: "Requiere construir o no Registry in ECR")
    booleanParam(
      name: 'MIGRATIONS',
      defaultValue: false,
      description: "Indica si se ejecutaran las migraciones de DB")
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Set Enviroment') {
      steps {
        script {

          if (fileExists("./cloudformation/parameters/${GIT_BRANCH}.yml")) {
            def configFile = readYaml file: "./cloudformation/parameters/${GIT_BRANCH}.yml"
            println "config ==> ${configFile}"
            for (var in configFile.environment) {
              env[var.key] = var.value
            }
            echo "${ENV}"
            echo "${DEPLOY_REGION}"
          }
          else {
            error("No existe la configuracion para la rama ${GIT_BRANCH}")
          }
        }
      }
    }
    stage('Create Registry') {
      steps {
        script {
          if ("${params.REGISTRY}" == "true") {
            sh 'make create-registry'
          }
        }
      }
    }
    stage('login AWS DEV') {
      steps {
        sh 'make login-aws-dev'
      }
    }
    stage('Install') {
      steps {
        sh 'make install'
      }
    }
    stage('Test') {
      steps {
        sh 'make tests'
      }
    }
    stage('login AWS DEPLOY') {
      steps {
        sh 'make login-aws'
      }
    }
    stage('Sync CloudFormation Resources') {
      steps {
        sh 'make sync-cloudformation'
      }
    }
    stage('Build') {
      steps {
        sh 'make build-latest'
      }
    }
    stage('Publish') {
      steps {
        sh 'make publish'
      }
    }
    stage('DB Migrations') {
      steps {
        script {
          if ("${params.MIGRATIONS}" == "true") {
            sh 'make migrate'
          } else {
            echo 'no se ejecutaron las migraciones'
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        sh 'make update-service'
      }
    }
  }
  post {
    always {
      junit 'app/nosetests.xml'
      sh 'make chown'
    }
    success {
      sh '''
        make slack-notify SLACK_TITLE="Deploy realizado con éxito" SLACK_LINK=${JOB_URL} SLACK_TEXT="Se realizo de manera correcta el deploy del proyecto ${JOB_NAME} en la rama ${BRANCH_NAME}"
        '''
    }
    failure {
      sh '''
        make slack-notify SLACK_TITLE="Error de deploy" SLACK_LINK=${JOB_URL} SLACK_TEXT="Se presento un problema mientras se desplegaba el proyecto ${JOB_NAME} en la rama ${BRANCH_NAME}"
        '''
    }
  }
}
