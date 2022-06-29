import json
import random
from yb_generated_users.intrinio.Enums.TickerType import TickerType

TEN_BILLION = 10000000000
BILLION = 1000000000
PENNY = 300000000


def _get_all_tickers_from_file() -> list[object]:
    with open("./data/all_stocks.json", "r") as f:
        data = json.load(f)

    return data


def _get_top_100_tickers_from_file() -> list[str]:
    with open("./data/top_100_tickers.json", "r") as f:
        data = json.load(f)

    return data


def filter_ticker_types_by_industry(
    industries_filter: list[str] = [],
    all_ticker_objects: list[object] = [],
    filtered_ticker_objects: list[object] = [],
) -> list[object]:
    filtered_ticker_objects += list(
        filter(lambda x: x["industry"] in industries_filter, all_ticker_objects)
    )

    return filtered_ticker_objects


def get_tickers_from_files(
    ticker_type_list: list[TickerType] = [], num: int = 0
) -> list[str]:
    filtered_ticker_objects: list[object] = []
    all_ticker_objects: list[object] = _get_all_tickers_from_file()

    if TickerType.RETAIL in ticker_type_list:
        retail_industries = [
            "Apparel Retail",
            "Apparel Manufacturing",
            "Household Durables",
            "Hotels",
            "Restaurants & Leisure",
            "Household & Personal Products",
            "Grocery Stores",
            "Personal Products",
            "Multiline Retail",
            "Leisure Products",
            "Internet Retail",
            "Internet & Direct Marketing Retail",
            "Specialty Retail",
            "Restaurants",
            "Textiles",
            "Apparel & Luxury Goods",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=retail_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.SOFTWARE in ticker_type_list:
        software_industries = [
            "Electronic Gaming & Multimedia",
            "Information Technology Services",
            "IT Services",
            "Health Care Technology",
            "Internet Retail",
            "Internet & Direct Marketing Retail",
            "Interactive Media & Services",
            "Technology Hardware, Storage & Periph...",
            "Software-Infrastructure",
            "Software-Application",
            "Software",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=software_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.SEMICONDUCTORS in ticker_type_list:
        semiconductor_industries = [
            "Electronic Equipment",
            "Instruments & C...",
            "Computer Hardware",
            "Technology Hardware",
            "Storage & Periph...",
            "Semiconductors & Semiconductor Equipment",
            "Semiconductors",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=semiconductor_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.REAL_ESTATE in ticker_type_list:
        real_estate_industries = [
            "Building Products",
            "Equity Real Estate Investment Trusts ...",
            "Engineering & Construction",
            "Construction Materials",
            "Construction & Engineering",
            "Hotels",
            "Restaurants & Leisure",
            "Mortgage Real Estate Investment Trust...",
            "Real Estate Management & Development",
            "Real Estate Services",
            "REIT-Diversified",
            "REIT-Mortgage",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=real_estate_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.PHARMACEUTICALS in ticker_type_list:
        pharmaceuticals_industries = [
            "Biotechnology",
            "Drug Manufacturers-Specialty & Generic",
            "Drug Manufacturers-General",
            "Pharmaceuticals",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=pharmaceuticals_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.INSURANCE in ticker_type_list:
        insurance_industries = ["Insurance", "Banks", "Insurance Brokers"]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=insurance_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.ENERGY in ticker_type_list:
        energy_industries = [
            "Energy Equipment & Services",
            "Electrical Equipment & Parts",
            "Electrical Equipment",
            "Electric Utilities",
            "Independent Power and Renewable Elect...",
            "Gold",
            "Gas Utilities",
            "Other Precious Metals & Mining",
            "Oil",
            "Gas & Consumable Fuels",
            "Oil & Gas Equipment & Services",
            "Oil & Gas E&P",
            "Multi-Utilities",
            "Metals & Mining",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=energy_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.MEDICAL in ticker_type_list:
        medical_industries = [
            "Biotechnology",
            "Drug Manufacturers-Specialty & Generic",
            "Drug Manufacturers-General",
            "Diagnostics & Research",
            "Healthcare Plans",
            "Health Information Services",
            "Health Care Technology",
            "Health Care Providers & Services",
            "Medical Instruments & Supplies",
            "Medical Devices",
            "Medical Care Facilities",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=medical_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.MACHINERY in ticker_type_list:
        machinery_industries = [
            "Apparel Manufacturing",
            "Auto Components",
            "Auto Manufacturers",
            "Engineering & Construction",
            "Energy Equipment & Services",
            "Construction & Engineering",
            "Communications Equipment",
            "Metals & Mining",
            "Medical Instruments & Supplies",
            "Medical Devices",
            "Machinery",
            "Specialty Industrial Machinery",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=machinery_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.MEDIA in ticker_type_list:
        media_industries = [
            "Advertising Agencies",
            "Entertainment",
            "Electronic Gaming & Multimedia",
            "Education & Training Services",
            "Diversified Consumer Services",
            "Media",
            "Interactive Media & Services",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=media_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.FOOD in ticker_type_list:
        food_industries = [
            "Agricultural Inputs",
            "Beverages",
            "Beverages-Brewers",
            "Beverages-Non-Alcoholic",
            "Beverages-Wineries & Distilleries",
            "Grocery Stores",
            "Food Products",
            "Food & Staples Retailing",
            "Packaged Foods",
            "Restaurants",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=food_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.ELECTRONICS in ticker_type_list:
        electronics_industries = [
            "Electronic Equipment",
            "Instruments & C...",
            "Electronic Components",
            "Electrical Equipment & Parts",
            "Electrical Equipment",
            "Consumer Electronics",
            "Computer Hardware",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=electronics_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.COMMUNICATIONS in ticker_type_list:
        communications_industries = [
            "Air Freight & Logistics",
            "Electrical Equipment & Parts",
            "Electrical Equipment",
            "Diversified Telecommunication Services",
            "Communications Equipment",
            "Multi-Utilities",
            "Software-Infrastructure",
            "Road & Rail",
            "Wireless Telecommunication Services",
            "Telecom Services",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=communications_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.COMMERCIAL in ticker_type_list:
        commercial_industries = [
            "Containers & Packaging",
            "Air Freight & Logistics",
            "Auto Components",
            "Auto Manufacturers",
            "Auto Parts",
            "Commercial Services & Supplies",
            "Industrial Conglomerates",
            "Household Durables",
            "Packaging & Containers",
            "Trading Companies & Distributors",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=commercial_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.CHEMICALS in ticker_type_list:
        chemicals_industries = [
            "Biotechnology",
            "Diagnostics & Research",
            "Construction Materials",
            "Chemicals",
            "Life Sciences Tools & Services",
            "Specialty Chemicals",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=chemicals_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.BANKS in ticker_type_list:
        banks_industries = [
            "Asset Management",
            "Banks",
            "Banks-Diversified",
            "Banks-Regional",
            "Diversified Financial Services",
            "Credit Services",
            "Consumer Finance",
            "Capital Markets",
            "Insurance",
            "Thrifts & Mortgage Finance",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=banks_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.AEROSPACE in ticker_type_list:
        aerospace_industries = [
            "Aerospace & Defense",
            "Solar",
            "Security & Protection Services",
            "Road & Rail",
            "Transportation Infrastructure",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=aerospace_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.AIRLINES in ticker_type_list:
        airlines_industries = [
            "Air Freight & Logistics",
            "Airlines",
            "Airports",
            "Transportation Infrastructure",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=airlines_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    if TickerType.AUTO in ticker_type_list:
        auto_industries = [
            "Auto & Truck Dealerships",
            "Auto Components",
            "Auto Manufacturers",
            "Auto Parts",
            "Automobiles",
            "Transportation Infrastructure",
        ]

        filtered_ticker_objects = filter_ticker_types_by_industry(
            industries_filter=auto_industries,
            all_ticker_objects=all_ticker_objects,
            filtered_ticker_objects=filtered_ticker_objects,
        )

    # "VALUE" filters
    if TickerType.ALL in ticker_type_list:
        filtered_ticker_objects += all_ticker_objects

    if TickerType.TEN_BILLION in ticker_type_list:
        if not filtered_ticker_objects:
            filtered_ticker_objects += [
                item for item in all_ticker_objects if item["market_cap"] >= TEN_BILLION
            ]
        else:
            filtered_ticker_objects = list(
                filter(
                    lambda x: x["market_cap"] >= TEN_BILLION, filtered_ticker_objects
                )
            )

    if TickerType.ONE_BILLION in ticker_type_list:
        if not filtered_ticker_objects:
            filtered_ticker_objects += [
                item for item in all_ticker_objects if item["market_cap"] >= BILLION
            ]
        else:
            filtered_ticker_objects = list(
                filter(lambda x: x["market_cap"] >= BILLION, filtered_ticker_objects)
            )

    if TickerType.PENNY in ticker_type_list:
        if not filtered_ticker_objects:
            filtered_ticker_objects += [
                item for item in all_ticker_objects if item["market_cap"] <= PENNY
            ]
        else:
            filtered_ticker_objects = list(
                filter(lambda x: x["market_cap"] <= PENNY, filtered_ticker_objects)
            )

    if TickerType.TOP_HUNDRED in ticker_type_list:
        top_hundred_tickers = _get_top_100_tickers_from_file()

        if not filtered_ticker_objects:
            filtered_ticker_objects += list(
                filter(lambda x: x["symbol"] in top_hundred_tickers, all_ticker_objects)
            )
        else:
            filtered_ticker_objects = list(
                filter(
                    lambda x: x["symbol"] in top_hundred_tickers,
                    filtered_ticker_objects,
                )
            )

    return list(set([x["symbol"] for x in random.sample(filtered_ticker_objects, num)]))
