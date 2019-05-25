
import flask
import docker

blueprint = flask.Blueprint('docker', __name__)

connection = docker.DockerClient()

@blueprint.route('/docker', methods=[ 'GET' ])
def get_docker():    

	container = connection.containers.get('31dbb3401f5a')

	context = {
		'page': 'docker',
		'route': {
			'is_public': False
		},
		'container': container
	}

	return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/start', methods=[ 'GET' ])
def start_docker():

	container = connection.containers.get('31dbb3401f5a')

	if not container:
		flask.flash('Container não iniciado', 'danger')

	elif container.status != 'running':
		container.start()
		flask.flash('Container iniciado', 'sucess')

	else:
		flask.flash('Container já esta iniciado', 'info')

	return flask.redirect('/docker')

@blueprint.route('/docker/stop', methods=[ 'GET' ])
def stop_docker():

	container = connection.containers.get('31dbb3401f5a')

	if not container:
		flask.flash('Container não iniciado', 'danger')

	elif container.status == 'running':
		container.stop()
		flask.flash('Container iniciado', 'sucess')

	else:
		flask.flash('Container já esta parado', 'info')

	return flask.redirect('/docker')
