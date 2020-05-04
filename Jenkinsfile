pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.8-slim-buster' 
                }
            }
            steps {
                // // sh 'sudo -H pip3 install mock'
                // sh 'sudo -H pip3 install --upgrade pip'
                // sh 'sudo -H pip3 install networkx'
                // sh 'sudo -H pip3 install numpy'
                sh 'export PYTHONPATH=$WORKSPACE:$PYTHONPATH'
                sh 'pip3 install -e ./networkx'
                sh 'pip3 install -e ./numpy'
                sh 'python -m py_compile sources/Node.py sources/NodeFailure.py sources/Path.py sources/sim.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                // sh 'pip3 install --upgrade pip'
                // sh 'pip3 install networkx'
                sh 'py.test --junit-xml test-reports/results.xml sources/PathTest.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}