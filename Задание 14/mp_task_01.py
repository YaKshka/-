import threading
import time
import multiprocessing
import math
import requests


# список url
urls = ['https://genshin-info.ru'] * 10


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequence():
    start_time = time.perf_counter()
    for url in urls:
        fetch_url(url)

    end_time = time.perf_counter()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    start_time = time.perf_counter()
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, ))
        threads.append(thread)
        thread.start()

    for thread in threads:
            thread.join()

    end_time = time.perf_counter()
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    start_time = time.perf_counter()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    end_time = time.perf_counter()
    print(f'processes time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    #sequence()
    #threads()
    processes()
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        sequence time:  1.55

        threads time:  0.21
        
        processes time:  0.60
    """
