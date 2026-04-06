import psutil
def top_processes():
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        procs.append(p.info)

    procs = sorted(procs, key=lambda x: x['cpu_percent'], reverse=True)
    return procs[:10]

for p in top_processes():
    print(f"{p['pid']} {p['name']} {p['cpu_percent']}%")
