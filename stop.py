import docker
print("STOP container")
client = docker.from_env()
container_name="some-mysql"
container =  client.containers.get(container_name)
print(container)
container.stop()