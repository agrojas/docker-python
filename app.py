import docker
import os

client = docker.from_env()
image_name = 'mysql:5.6'
container_name="some-mysql"
image = None
container_ports = {'33061':'3306'}

container_environment={'MYSQL_ROOT_PASSWORD':'mysql'}

from_path = os.getcwd() + '/config/mysql'
to_path = '/docker-entrypoint-initdb.d'
mode = 'rw'
container_volumes= {from_path: {'bind': to_path, 'mode': mode}}


image_list = client.images.list(name=image_name)
print("Image_list {}".format(image_list))
if not image_list:
	print("Pull {}".format(image_name))
	image = client.images.pull(image_name)


print("$ docker run -v {} -e {} -p {}--name {} -d {} ".format(container_volumes,
															container_environment,
															container_ports,
															container_name,
															image_name))
container =  client.containers.run(image=image_name, 
									name=container_name,
									volumes=container_volumes,
									environment=container_environment,
									detach=True)


print(container)