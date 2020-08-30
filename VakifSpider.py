from BankSpider import BankSpider
from CustomExceptions import *


class VakifSpider(BankSpider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_currency_table(self):
        all_elements = self.page_soup.findChildren('tbody', recursive=True)

        for element in all_elements:
            element_children = element.findChildren('tr', recursive=False)
            tr_count = len(element_children)

            if tr_count == 13:
                return element_children

        raise TableNotFoundException("Could not find table containing rates")

    def _get_rates_list(self):
        rates_list = self._get_currency_table()

        # Skip first row because it's column names
        return rates_list[1:]

    @staticmethod
    def _get_currency_name(row):
        raw_name_ = row[0].text
        name_ = raw_name_.split(' ')[0]

        return name_

    @staticmethod
    def _get_bank_rates(row):

        bank_buys = row[1].text.replace(',', '.')
        bank_sells = row[2].text.replace(',', '.')

        return float(bank_buys), float(bank_sells)

    def _extract_values(self, rates_list):

        extracted_values = []

        for row in rates_list:

            row_children = row.findChildren('td')
            
            currency_name = self._get_currency_name(row_children)
            bank_buys, bank_sells = self._get_bank_rates(row_children)
            
            values_tuple = (currency_name, bank_buys, bank_sells)

            extracted_values.append(values_tuple)

        return extracted_values

    def _get_usd_value(self, values):
        for value in values:
            if value[0] == 'USD':
                return value

        raise CurrencyNotFoundException("The Currency USD was not found in the scraped results")

    def get_single_reading(self):
        rates_list = self._get_rates_list()

        extracted_values = self._extract_values(rates_list)

        usd_value = self._get_usd_value(extracted_values)

        return usd_value