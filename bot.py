import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 

configs = [("http://yvonnemcguinness.com?st_bot_panel_id=1", "chrome", 1),
("https://www.luxxmakeup.com.br/adesivo-de-borboleta-sortido-fn-fan-nails?st_bot_panel_id=1", "chrome", 1),
("https://www.protothema.gr/greece/article/1394156/lasithi-parti-se-prostateumeno-arhaiologiko-horo-deite-video-kai-fotografies?st_bot_panel_id=1", "chrome", 1),
("https://mcpedl.com/ruins-addon?st_bot_panel_id=1", "chrome", 1),
("https://alexanriverside.com/floorplan/bohemian?move\u003d?st_bot_panel_id=1", "chrome", 1),
("https://www.myexcelonline.com/blog/excel-number-formats-thousands-millions?st_bot_panel_id=1", "chrome", 1),
("https://gre4ka.info/suspilstvo/74931-namahavsia-perebihty-kordon-na-zakarpatti-prykordonnyky-zatrymaly-19-richnoho-kropyvnychanyna-foto?st_bot_panel_id=1", "chrome", 1),
("https://kingmodapk.net/resso-mod-apk?download?st_bot_panel_id=1", "chrome", 1),
("https://videos.waploaded.com?st_bot_panel_id=1", "chrome", 1),
("https://www.dlsph.utoronto.ca?st_bot_panel_id=1", "chrome", 1),
("https://www.swadeshpratidin.com/details.php?id\u003d93529?st_bot_panel_id=1", "chrome", 1),
("https://docs.aglasem.com/view/8381c2e4-73f8-11ea-b956-02f21f5619c4?st_bot_panel_id=1", "chrome", 1),
("https://veerbhuminews.com/VeerBhumi/news/2196?st_bot_panel_id=1", "chrome", 1),
("https://gomovies.sx/watch-tv/watch-how-i-met-your-mother-gomovies-39439.4877566?st_bot_panel_id=1", "chrome", 1),
("https://cricketpakistan.com.pk/en/news/detail/pakistans-updated-future-tours-programme-2023-2025?st_bot_panel_id=1", "chrome", 1),
("https://www.governmentjobs.com/careers/wvdot?st_bot_panel_id=1", "chrome", 1),
("https://cdnondemand.org/prod/goto.html?lu\u003dhttps%3A%2F%2Ftrack.hereisthemoment.com%2F15GVMV%3Fsubid%3D6726308%26country%3DUY%26affid%3D97988%26cost%3D%7Bpayout%7D%26external_id%3D168980644609990TUYTV62800Ra4R1aacR300Rd91fRb522R5677R6f3c6Vbad26?st_bot_panel_id=1", "chrome", 1),
("https://edollarearn.to/threads/103050-Barry-Robinson-240-Rounds-of-a-Million-Styles-Boxing-Drills?st_bot_panel_id=1", "chrome", 1),
("https://sattamatkaz.com/guessing/sridevi?st_bot_panel_id=1", "chrome", 1),
("https://tq.explorefast-2.com/filter?q\u003d\u0026i\u003dcQzhM6di1j0_0\u0026ci\u003d-20050370838211910\u0026t\u003d458603838\u0026h\u003d23?st_bot_panel_id=1", "chrome", 1)]

chrome_driver_path = sys.argv[1]
chrome_user_data_path = sys.argv[2]

def crawl(url):
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'--user-data-dir=' + chrome_user_data_path)
    chrome_options.add_argument('--profile-directory=chrome_profile')
    
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    
    try:
        # timeout if hang
        driver.set_page_load_timeout(5)

        driver.get(url)
    
        driver.delete_cookie("fpestid")
        driver.add_cookie({"name": "fpestid", "value": "st_bot_panel_id=1"})
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
      crawl(config[0])

if __name__ == "__main__":
    main()