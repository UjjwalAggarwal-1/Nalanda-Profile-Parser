base  = "https://nalanda-aws.bits-pilani.ac.in/user/profile.php?id="
session_id = "r8167r085lrefcu1n3dmn378gm"
SLEEP_TIME = 0.2

import time
import requests
from bs4 import BeautifulSoup 

# def get_id_self(text):
#     soup = BeautifulSoup(text, "html.parser")
#     target_element = soup.select("#region-main > div > div > div > section:nth-child(1) > div > ul > li:nth-child(5) > dl > dd")
#     if target_element:
#         element_text = target_element[0].get_text()
#         return ("Extracted element text:"+ element_text)
#     else:
#         return ("Element not found.")

# def get_id_not_self(text):
#     soup = BeautifulSoup(text, "html.parser")
#     target_element = soup.select("#region-main > div > div > div > section:nth-child(1) > div > ul > li:nth-child(3) > dl > dd")
#     if target_element:
#         element_text = target_element[0].get_text()
#         return ("Extracted element text:"+ element_text)
#     else:
#         return ("Element not found.")

def get_id_helper(text):
    soup = BeautifulSoup(text, "html.parser")
    target_element = soup.select("#region-main > div > div > div > section:nth-child(1) > div > ul > li" ) # > li:nth-child(5) > dl > dd")
    # print(target_element)
    if not target_element:
        return ("Element not found.")
    for element in target_element:
        # print(element)
        element_text = element.select("dl")
        # print("dl",element_text)
        if not element_text:
            continue
        element_text = element_text[0].select("dt")
        # print("DT", element_text)
        if not element_text:
            continue
        element_text = element_text[0].get_text()
        if element_text != ("BITS_STUDENT_ID"):
            continue
        element_text = element.select("dd")
        # print("DD", element_text)
        return ("Extracted element text:"+ element_text[0].get_text())
    return ("Element not found.")
        

def get_id(id):
    url = base + str(id)
    r = requests.get(url, cookies={"MoodleSession":session_id})
    if not r.status_code == 200:
        return ("Not found: " + url)
    # with open("ujju.html", "w") as f:
    #     f.write(r.text)
    # if id == 10848:
    #     return get_id_self(r.text)
    # else:
    #     return get_id_not_self(r.text)
    return( get_id_helper(r.text))

for id in range(1000, 11500):
    print(id)
    with open("id.txt", "a") as f:
        f.write(str(id) + " ")
        f.write(get_id(id) + "\n")
    time.sleep(SLEEP_TIME)
    
# sample call
# print(get_id(10503))
