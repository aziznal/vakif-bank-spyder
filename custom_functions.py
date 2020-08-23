from VakifBankSpyder import VakifBankSpyder
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def make_spyder():
    
    url = 'https://subesizbankacilik.vakifbank.com.tr/gunlukfinans/SubesizBankacilik/GunlukDovizKurlari.aspx'

    options = FirefoxOptions()
    options.headless = False

    spyder = VakifBankSpyder(url=url, options=options)

    return spyder
