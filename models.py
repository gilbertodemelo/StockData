
class Stock:
    def __init__(self, symbol, balance_sheets, income_statements = None,cash_flows = None):
        self.symbol = symbol
        self.balance_sheets = balance_sheets
        self.income_statements = income_statements
        self.cash_flows = cash_flows

    def get_current_cash(self) -> float:
        """Get the amount of cash and cash-like assets."""
        return float(self.balance_sheets['quarterlyReports'][0]['cashAndShortTermInvestments'])

    def get_noncash_current_assets(self) -> float:
        """Get the amount of non-cash current assets.

        To be according to the book's formula, goodwill and
        non-tangible assets are not included in the calculation.
        """
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

    def get_noncash_tangible_assets(self) -> float:
        """Get the total non-cash tangible assets.

        The function will get amounts for both current and
        non-current assets, minus intangible ones.
        """
        non_cash_current_assets = self.get_noncash_current_assets()
        non_current_assets = self.balance_sheets['quarterlyReports'][0]['totalNonCurrentAssets']
        return float(non_current_assets + non_cash_current_assets)

    def get_current_liabilities(self) -> float:
        return float(self.balance_sheets['quarterlyReports'][0]['totalCurrentLiabilities'])

    def get_total_liabilities(self) -> float:
        return float(self.balance_sheets['quarterlyReports'][0]['totalLiabilities'])

    def get_number_shares_outstanding(self) -> int:
        """Get the number of shares outstanding."""
        return int(self.balance_sheets['quarterlyReports'][0]['commonStockSharesOutstanding'])

    def get_year_eps(self) -> float:
        pass

    def get_adjusted_current_ratio(self, cash: float, non_cash_current_assets: float, current_liabilities) -> float:
        """Get the adjusted current ratio for this stock.

        The adjusted current ratio is the current ratio where
        non-cash current assets are discounted 20% to compensate for
        risks (ex: an accounts receivable that is not paid).
        """
        return (self.get_current_cash() + (0.80 * self.get_noncash_current_assets())) / self.get_current_liabilities()

    def get_adjusted_tangible_stock_equity(self) -> float:
        """Get the adjusted tangible stock equity.

        The adjusted stock equity is the stock equity calculation where
        non-cash tangible assets are discounted 10% to compensate for
        risks.
        """
        return self.get_current_cash() + (0.90 * self.get_noncash_current_assets()) - self.get_total_liabilities()

    def get_initial_floor_price(self) -> float:
        """Get the initial floor price for the stock.

        The initial floor price (or lower) is the what the investor should be
        willing to currently pay for the stock.
        """
        return self.get_adjusted_tangible_stock_equity() / self.get_number_shares_outstanding()

    def get_adjusted_floor_price(self) -> float:
        """Get the adjusted floor price for the stock.

        The adjusted floor price is the initial floor price plus the EPS (estimated
        or TTM). A negative EPS will lower the initial floor price while a positive
        one will have the contrary effect.
        """
        return self.get_initial_floor_price() + self.get_year_eps()




