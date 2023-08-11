import sys
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 

# process input
path_to_json = '/Users/yuyangdong/Downloads/input/'
# path_to_json = '/home/ubuntu/input/'
json_files = [f_json for f_json in os.listdir(path_to_json) if f_json.endswith('.json')]
configs = []
for json_file in json_files:
    config = json.load(open('/Users/yuyangdong/Downloads/input/' + json_file))
    # config = json.load(open('/home/ubuntu/input/' + json_file))
    configs += config

for config in configs:
    if config["url"][-1] == "/":
        config["url"] = config["url"][:-1]
    config["url"] = config["url"] + "?st_bot_panel_id=" + config["estid"]

chrome_driver_path = sys.argv[1]
chrome_user_data_path = sys.argv[2]

def crawl(config):

    url = config["url"]
    estid = config["estid"]
    ts_offset = int(config["ts_offset"])

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'--user-data-dir=' + chrome_user_data_path)
    chrome_options.add_argument('--profile-directory=chrome_profile')
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    print(f"sleeping... will return in {ts_offset}s")
    time.sleep(ts_offset)

    try:
        # timeout if hang
        driver.set_page_load_timeout(1)

        driver.get(url)

        driver.delete_cookie("fpestid")
        driver.add_cookie({"name": "fpestid", "value": f"st_bot_panel_id={estid}"})
        cookie = driver.get_cookie("fpestid")["value"]
        print("pview done: " + url)
        print("cookie modified to: " + cookie)

    except TimeoutException:
        print(f"pview done: {url} [TIMEOUT]")
    except Exception as e:
        print(f"An error occurred while visiting {url}:", e)
    finally:
        driver.quit()

def main():
    for config in configs:
      crawl(config)

if __name__ == "__main__":
    main()