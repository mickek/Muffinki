from itty import *
import subprocess


@get('/deploy')
def index(request):
    subprocess.call(['./server_script.sh'])
    return '0'

run_itty(config = "server_config")
