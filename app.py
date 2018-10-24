import argparse
from mysql_container import MysqlContainer
from container_manager import DockerContainerManager


def get_container_manager(image, secret):
	if image == 'mysql':
		return MysqlContainer(secret)
	elif image == 'cassandra':
		return None
	else:
		return None

parser = argparse.ArgumentParser()
parser.add_argument("action", help="action to execute",choices=['run', 'info', 'stop', 'verify','pull'])
parser.add_argument("-i", "--image", help="image type", default='mysql',choices=['mysql', 'cassandra'])
parser.add_argument("-n", "--name", help="increase output verbosity")
parser.add_argument("-s", "--secret", help="increase output verbosity")

args = parser.parse_args()
manager = DockerContainerManager()

if args.action == 'run':
	print('run {}'.format(args.name))
	container_client = get_container_manager(args.image, args.secret)
	result = container_client.run(args.name)
	print(result)
elif args.action == 'info':
	print('info {}'.format(args.name))
	print(manager.get(args.name))
elif args.action == 'stop':
	print('stop {}'.format(args.name))
	manager.stop(args.name)
elif args.action == 'verify':
	print('verify image {}'.format(args.image))
	print(manager.check_image(args.image))
elif args.action == 'pull':
	print('pull image {}'.format(args.image))
	print(manager.pull(args.image))
else:
	print('error {}'.format(args.name))

