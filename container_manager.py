import docker

class DockerContainerManager(object):
	"""docstring for DockerContainerManager"""
	def __init__(self, client=None):
		super(DockerContainerManager, self).__init__()

		self.client = client if client else docker.from_env()
		self.image_name = None
		self.container_name = None
		self.container_ports = None
		self.container_volumes = None
		self.container = None
		self.image = None


	def check_image(self, image_name):
		return self.client.images.list(name=image_name)


	def pull(self, image_name):
		print("Pull {}".format(image_name))
		image = self.client.images.pull(image_name)
		return image

	def run(self, image_name, container_name,**kwargs):

		self.image_name = image_name
		self.container_name = container_name
		self.container_volumes = kwargs['container_volumes']
		self.container_environment = kwargs['container_environment']
		self.container_ports = kwargs['container_ports']

		print("$ docker run -v {} -e {} -p {} --name {} -d {} ".format(self.container_volumes,
															self.container_environment,
															self.container_ports,
															self.container_name,
															self.image_name))
		self.container =  self.client.containers.run(image=self.image_name, 
									name=self.container_name,
									volumes=self.container_volumes,
									environment=self.container_environment,
									remove=True,
									detach=True)
		return self.container

	def get(self, container):
		return self.container if self.container else self.client.containers.get(container)


	def stop(self, container_name):
		container = self.container if self.container else self.get(container_name)
		container.stop()

