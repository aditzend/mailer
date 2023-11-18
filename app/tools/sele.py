from selenium import webdriver

msg = "https://web.whatsapp.com/send?phone=5491160134585&text=Hola+este+es+un+reminder+de+que+faltan+x+dias+para+la+SAIA+conf"
home = "https://web.whatsapp.com/"
browser = webdriver.Firefox()
browser.get(home)
