import docker
print("GET container")
client = docker.from_env()
container_name="some-mysql"
container =  client.containers.get(container_name)
print(container.short_id)
print(container.name)
print(container.status)
print(container.logs())