import requests
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def request_to_docker_server(server_address, a, b):
    request = {
        'var_a': a,
        'var_b': b
        }
    response = requests.post(server_address+'/request', json=request, timeout=60)
    if response.status_code==200:
        result = json.loads(response.text)
        return result['var_c']
    else:
        logger.error(response.status_code)
        logger.error(response.text)
    return None


def main():
    a = 14
    b = 3

    # Plus
    server_address = 'http://localhost:42012'    
    plus_result = request_to_docker_server(server_address, a, b)
    logger.info(str(a)+' + '+str(b)+' = '+str(plus_result))

    # Minus
    server_address = 'http://localhost:42013'
    plus_result = request_to_docker_server(server_address, a, b)
    logger.info(str(a)+' - '+str(b)+' = '+str(plus_result))

    
if __name__ == "__main__":
    main()
