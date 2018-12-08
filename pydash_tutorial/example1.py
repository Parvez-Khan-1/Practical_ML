from pydash_tutorial import data
import pydash.collections as collection
import time

pharmacy_data = data.pharmacy_data


def first_way():
    start_time = time.time()
    all_locations = pharmacy_data['location']
    result = collection.find(all_locations, {'id': "a5bad7a6-7111-4bfb-9c9d-29363db57731"})
    if result is not None:
        print(result['service'])
    print("Time Required : ", (time.time()-start_time))


def second_way():
    start_time = time.time()
    for location in pharmacy_data['location']:
        if location['id'] == "a5bad7a6-7111-4bfb-9c9d-29363db57731":
            service = location.get("service")
            print(service)
            break
    print("Time Required : ", (time.time()-start_time))


if __name__ == '__main__':
    first_way()
    second_way()