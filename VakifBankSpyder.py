from BankSpyder import BankSpyder
from CustomExceptions import *


class VakifBankSpyder(BankSpyder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_single_reading(self):
        pass