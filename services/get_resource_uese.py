import psutil

def get_resource_status():
    try:
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        load_avg = psutil.getloadavg()

        return {
            "load_avg_1m": round(load_avg[0],2),
            "load_avg_5m": round(load_avg[1],2),
            "load_avg_15m": round(load_avg[2],2),
            "cpu_percent": cpu,
            "memory_percent": memory.percent,
            "memory_total_gb": round(memory.total / 1073741824, 2),
            "memory_used_gb": round(memory.used / 1073741824, 2),
            "memory_available_gb": round(memory.available / 1073741824, 2),
            "disk_total_gb": round(disk.total / 1073741824, 2),
            "disk_used_gb": round(disk.used / 1073741824, 2),
            "disk_free_gb": round(disk.free / 1073741824, 2),
            "disk_percent": disk.percent,
        }

    except Exception as e:
        return {"error": str(e)}
