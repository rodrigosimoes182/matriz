import subprocess, string

processo = subprocess.Popen("docker ps -a", shell=True, stdout=subprocess.PIPE)
processo =str(processo.stdout.read())
processo =  processo.split(" ")
processo =processo[-1]
processo=processo[0:-3]
print(processo)