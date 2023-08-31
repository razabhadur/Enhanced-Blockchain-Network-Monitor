import requests
import random
import time


def check_node_health(node_url):
    try:
        response = requests.get(node_url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False

def simulate_transaction_analysis():
    transaction_volume = random.randint(1, 100)
    transaction_value = random.randint(1, 1000)
    return transaction_volume, transaction_value

def alert(message):
    print(f'ALERT: {message}')
    with open('blockchain_monitor.log', 'a') as log_file:
        log_file.write(f'{time.ctime()} - {message}\n')

if __name__ == '__main__':
    nodes = ['http://example1.com', 'http://example2.com', 'http://example3.com']
    while True:
        for node_url in nodes:
            if not check_node_health(node_url):
                alert(f'Node {node_url} is down!')
            transaction_volume, transaction_value = simulate_transaction_analysis()
            if transaction_volume > 90:
                alert(f'High transaction volume detected on node {node_url}!')
            if transaction_value > 900:
                alert(f'High transaction value detected on node {node_url}!')
        time.sleep(5)
