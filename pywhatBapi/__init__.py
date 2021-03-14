import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

def sendwhatmsgs(csv_file):
    Messages = pd.read_csv(csv_file)
    Messages_dict = Messages.to_dict('list')
    Mobile_Numbers = Messages_dict['Mobile_Number']
    messages = Messages_dict['Message']
    Number_Message = zip(Mobile_Numbers,messages)
    first = True
    for Mobile_Numbers,message in Number_Message:
        time.sleep(5)
        web.open("https://api.whatsapp.com/send?phone="+Mobile_Numbers+"&text="+message)
        if first:
            time.sleep(8)
            first=True
        width,height = pg.size()
        pg.click(width/2,height/2)
        time.sleep(8)
        pg.press('enter')
        time.sleep(5)
        pg.hotkey('alt','f4') 
        pg.hotkey('ctrl','w')
    return ("Messages sent Succesfully.")
