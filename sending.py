import sys
import os
import requests

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # post to server
        url = sys.argv[1]
        print("-------------------------------------------------")
        print("send to server...")
        if url[0:4] != "http":
            url = "http://localhost:8080/meals/test"
            requests.post(url, data={"testStr": "Hello World!"})
        else:
            img_root_dir = 'img'
            img_ext = 'jpg'
            for img_filename in os.listdir(img_root_dir):
                if img_filename.split('.')[-1] != img_ext:
                    continue
                img_path = os.path.join(img_root_dir, img_filename)
                print(img_path)
                
                img = {'media': open(img_path, 'rb')}
                response = requests.post(url, files=img)
                print(response)
                print()
        print("-------------------------------------------------")
    else:
        print("-------------------------------------------------")
        print("you nee to specify server ip and port!")
        print()
        print("-------------------------------------------------")
