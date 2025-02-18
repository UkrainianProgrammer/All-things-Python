import time
from queue import Queue
from threading import Thread

import requests

NUMBER_OF_THREADS = 5
q = Queue()

def download_image(download_location):
    '''
    Downloads an image from a given URL.
    '''

    global q

    while True:
        image_url = q.get()
        res = requests.get(image_url, stream=True, verify=False)
        filename = f'{download_location}/{image_url.split('/')[-1]}.jpg'

        with open(filename, 'wb') as f:
            for block in res.iter_content(1024):
                f.write(block)
        print('Image downloaded successfully.')
        q.task_done()

def download_images_with_threading(images):
    print('Starting function with multithreading')
    for image_url in images:
        q.put(image_url)
    
    for t in range(NUMBER_OF_THREADS):
        worker = Thread(target=download_image, args=('with_multithreading_images',))
        worker.daemon = True
        print('Starting ' + worker.name)
        worker.start()
    q.join()

def download_images_without_threading(images):
    print('Starting function without multithreading')
    for image_url in images:
        res = requests.get(image_url, stream=True, verify=False)
        filename = f'without_multithreading_images/{image_url.split('/')[-1]}.jpg'

        with open(filename, 'wb') as f:
            for block in res.iter_content(1024):
                f.write(block)
        print('Image downloaded successfully.')

def main():
    images = [
        'https://images.unsplash.com/photo-1428366890462-dd4baecf492b',
        'https://images.unsplash.com/photo-1541447271487-09612b3f49f7',
        'https://images.unsplash.com/photo-1560840067-ddcaeb7831d2',
        'https://images.unsplash.com/photo-1522069365959-25716fb5001a',
        'https://images.unsplash.com/photo-1533752125192-ae59c3f8c403',
    ]

    print("Downloading images from Internet.\n")

    start_time = time.time()
    download_images_with_threading(images)
    print('----With Multithreading took %s seconds----', time.time() - start_time)

    start_time = time.time()
    download_images_without_threading(images)
    print('----Without Multithreading took %s seconds----', time.time() - start_time)

if __name__ == '__main__':
    main()