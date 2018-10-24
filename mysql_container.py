import os
from container_manager import DockerContainerManager

class MysqlContainer(object):
	"""docstring for MysqlContainer"""
	def __init__(self, mysql_root_pass):
		super(MysqlContainer, self).__init__()
		self.container_manager = DockerContainerManager()
		self.container =  None
		self.image_name = 'mysql:5.6'
		self.mysql_container_config = {
			'container_ports': {'33061':'3306'},
			'container_environment': {'MYSQL_ROOT_PASSWORD':mysql_root_pass},	
			'volume_mode': 'rw',
			'container_volumes': {self.__from_path(): {'bind': self.__to_path(), 'mode': 'rw'}}
		} 

	def run(self, container_name):
		self.container = self.container_manager.run(self.image_name, container_name, **self.mysql_container_config)
		return self
	
	def get_container(self):
		return self.container 

	def print_container_info(self):
		print(self.container.short_id)
		print(self.container.name)
		print(self.container.status)

	def stop(self):
		self.container_manager.stop()

	@staticmethod
	def __from_path():
		return os.getcwd() + '/config/mysql'

	@staticmethod
	def __to_path():
		return '/docker-entrypoint-initdb.d'

	def set_config(self, config):
		## TODO validate config
		self.mysql_container_config  = config


