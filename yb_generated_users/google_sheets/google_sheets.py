import pygsheets
from pygsheets import Spreadsheet, Worksheet

pyg = pygsheets.authorize(
    service_file="./yb_generated_users/google_sheets/generated-users-2609be92366f.json"
)


def create_sheets_data(sheet_id: str = "", trades: list[object] = []):
    print("\nAdding to Google Sheet")
    spreadsheet: Spreadsheet = pyg.open_by_key(sheet_id)

    if len(trades) == 0:
        print("No trades")
        return

    trades_worksheet: Worksheet = spreadsheet.worksheet_by_title("Trades")
    google_sheets_trades = [
        [
            trade["date"].strftime("%Y-%m-%d"),
            trade["ticker"],
            trade["type"],
            trade["quantity"],
            trade["price"],
        ]
        for trade in trades
    ]

    trades_worksheet.append_table(google_sheets_trades)


# def get_holdings_from_sheet(user: User):
#     spreadsheet: Spreadsheet = pyg.open_by_key(user.google_sheets_id)

#     holdings_wksht: Worksheet = spreadsheet.worksheet_by_title("Holdings")
#     rows = holdings_wksht.get_all_values()

#     realize_holdings: List[RealizePosition] = []

#     is_data = False
#     for row in rows:
#         if is_data:
#             if row[0] == "" or not row[0]:
#                 continue

#             realize_holdings.append(RealizePosition.from_google_sheet_row(row, user))

#         # Skip the header rows
#         if row[0].lower() == "ticker":
#             is_data = True

#     return realize_holdings


# def get_transactions_from_sheet(user: User):
#     spreadsheet: Spreadsheet = pyg.open_by_key(user.google_sheets_id)

#     trades_wksht: Worksheet = spreadsheet.worksheet_by_title("Trades")
#     trade_rows = trades_wksht.get_all_values()

#     realize_trades: List[RealizeTrade] = []

#     is_data = False
#     for row in trade_rows:
#         if is_data:
#             if row[0] == "" or not row[0]:
#                 continue

#             realize_trades.append(RealizeTrade.from_google_sheet_row(row, user))

#         # Skip the header rows
#         if row[0].lower() == "date":
#             is_data = True

#     transactions_wksht: Worksheet = spreadsheet.worksheet_by_title("Transactions")
#     tx_rows = transactions_wksht.get_all_values()

#     realize_transactions: List[RealizeTransaction] = []

#     is_data = False
#     for row in tx_rows:
#         if is_data:
#             if row[0] == "" or not row[0]:
#                 continue

#             realize_transactions.append(
#                 RealizeTransaction.from_google_sheet_row(row, user)
#             )

#         # Skip the header rows
#         if row[0].lower() == "date":
#             is_data = True

#     combined_transactions = realize_trades + realize_transactions
#     combined_transactions.sort(key=lambda r: r.transaction_date)

#     return combined_transactions
