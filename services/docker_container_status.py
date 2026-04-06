import docker

client = docker.from_env()
container = client.containers.get("your_container_name")

stats = container.stats(stream=False, decode=True)

memory_usage = stats["memory_stats"]["usage"]
cpu_total = stats["cpu_stats"]["cpu_usage"]["total_usage"]

print(f"Memory Usage: {memory_usage}")
print(f"CPU Usage: {cpu_total}")