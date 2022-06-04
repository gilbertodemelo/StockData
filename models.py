
class Stock:
    def __init__(self, symbol, balance_sheets, income_statements = None,cash_flows = None):
        self.symbol = symbol
        self.balance_sheets = balance_sheets
        self.income_statements = income_statements
        self.cash_flows = cash_flows

    def get_current_cash(self) -> float:
        return float(self.balance_sheets['quarterlyReports'][0]['cashAndShortTermInvestments'])

    def get_noncash_current_assets(self) -> float:

        # Get an amount for goodwill
        if self.balance_sheets['quarterlyReports'][0]['goodwill'] == 'None':
            goodwill = 0.0
        else:
            goodwill = float(self.balance_sheets['quarterlyReports'][0]['goodwill'])

        # Get an amount for intangible assets
        if self.balance_sheets['quarterlyReports'][0]['intangibleAssets'] == 'None':
            intangible_assets = 0
        else:
            intangible_assets = float(self.balance_sheets['quarterlyReports'][0]['intangibleAssets'])

        return float(self.balance_sheets['quarterlyReports'][0]['totalCurrentAssets']) - goodwill - intangible_assets

