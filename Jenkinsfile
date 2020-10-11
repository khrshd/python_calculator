// # this is default file recognized by its name and is groovie file which has different commenting convention where // is commenting
// agent any - means running on all machines
// indentation is not necessary but is good for eyes and visually attractive
pipeline {
	agent any
	stages {
		stage("Run the code!") {
			steps {
				sh """
					python calculator.py
				"""
			} //steps
		} //stage
		stage("Run unit tests") {
			steps {
				sh """
					pytest
				"""
			} //steps
		} //stage
	} //stages
} //pipeline
