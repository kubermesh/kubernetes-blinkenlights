import kubernetes
import os
import time

NAMESPACES = os.environ['LIGHT_NAMESPACES'].split(',')
NODE_NAME = os.environ['LIGHT_NODE_NAME']

RED = '#ff0000'
GREEN = '#00aa00'
WHITE = '#aaaaaa'

kubernetes.config.load_incluster_config()

v1 = kubernetes.client.CoreV1Api()


def pulse(colour):
    return ",%s,0.2,1,#000000,0.2,1" % colour

while True:
    rgb_line = pulse(WHITE)
    for pod in v1.list_pod_for_all_namespaces().items:
        if pod.spec.node_name != NODE_NAME:
            continue
        if pod.metadata.namespace not in NAMESPACES:
            continue
        if all(status.ready for status in pod.status.container_statuses):
            # All ready, green light!
            rgb_line += pulse(GREEN)
        else:
            # Sad face :(
            rgb_line += pulse(RED)

    command_line = "blink1-tool --playpattern '1,#00aa00,0,2,#000000,0,1%s'\n" % rgb_line
    with open('/target/command-line', 'w') as fobj:
        fobj.write(command_line)
    time.sleep(10)
