

def adjusted_current_ratio(cash: float, non_cash_current_assets: float, current_liabilities) -> float:
    return (cash + (0.80 * non_cash_current_assets)) / current_liabilities


def adjusted_tangible_stock_equity(cash: float, non_cash_tangible_assets: float, total_liabilities: float) -> float:
    return cash + (0.90 * non_cash_tangible_assets) - total_liabilities


def initial_floor_price(adj_tngb_stock_eqty: float, shares_outstanding: int) -> float:
    return adj_tngb_stock_eqty / shares_outstanding


def adjusted_floor_price(initial_floor_price: float, year_eps: float) -> float:
    return initial_floor_price + year_eps
