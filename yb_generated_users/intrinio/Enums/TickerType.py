from enum import Enum


class TickerType(Enum):
    ALL = 1
    TOP_HUNDRED = 2
    ONE_BILLION = 3
    TEN_BILLION = 4
    PENNY = 5
    RETAIL = 6  # Apparel Retail, Apparel Manufacturing, 	Household Durables, 	Hotels, Restaurants & Leisure, Household & Personal Products, 	Grocery Stores, Personal Products, 	Multiline Retail, Leisure Products, 	Internet Retail, 	Internet & Direct Marketing Retail, Specialty Retail, Restaurants, Textiles, Apparel & Luxury Goods
    SOFTWARE = 7  # Electronic Gaming & Multimedia, Information Technology Services, IT Services, 	Health Care Technology, Internet Retail, 	Internet & Direct Marketing Retail, 	Interactive Media & Services, Technology Hardware, Storage & Periph...	, Software-Infrastructure, Software-Application, Software
    SEMICONDUCTORS = 8  # Electronic Equipment, Instruments & C..., Computer Hardware, Technology Hardware, Storage & Periph...	, Semiconductors & Semiconductor Equipment	, Semiconductors
    REAL_ESTATE = 9  # Building Products, Equity Real Estate Investment Trusts ..., Engineering & Construction, Construction Materials, Construction & Engineering, 	Hotels, Restaurants & Leisure, Mortgage Real Estate Investment Trust...	, 	Real Estate Management & Development, Real Estate Services, REIT-Diversified, REIT-Mortgage
    PHARMACEUTICALS = 10  # Biotechnology, Drug Manufacturers-Specialty & Generic, Drug Manufacturers-General, Pharmaceuticals
    INSURANCE = 11  # Insurance, Banks, 	Insurance Brokers
    ENERGY = 12  # Energy Equipment & Services, Electrical Equipment & Parts, Electrical Equipment, Electric Utilities, Independent Power and Renewable Elect..., Gold, 	Gas Utilities, 	Other Precious Metals & Mining, Oil, Gas & Consumable Fuels, Oil & Gas Equipment & Services, Oil & Gas E&P, 	Multi-Utilities, 	Metals & Mining
    MEDICAL = 13  # Biotechnology, Drug Manufacturers-Specialty & Generic, Drug Manufacturers-General, 	Diagnostics & Research, Healthcare Plans,  Health Information Services, 	Health Care Technology, Health Care Providers & Services, Medical Instruments & Supplies, Medical Devices, Medical Care Facilities
    MACHINERY = 14  # Apparel Manufacturing, Auto Components, Auto Manufacturers, Engineering & Construction, Energy Equipment & Services, Construction & Engineering, 	Communications Equipment, 	Metals & Mining, Medical Instruments & Supplies, Medical Devices, Machinery, Specialty Industrial Machinery
    MEDIA = 15  # Advertising Agencies, Entertainment, 	Electronic Gaming & Multimedia, Education & Training Services, 	Diversified Consumer Services, Media, 	Interactive Media & Services
    FOOD = 16  # Agricultural Inputs, Beverages, Beverages-Brewers, Beverages-Non-Alcoholic, Beverages-Wineries & Distilleries, 	Grocery Stores	, Food Products, Food & Staples Retailing, 	Packaged Foods, Restaurants
    ELECTRONICS = 17  # Electronic Equipment, Instruments & C..., Electronic Components, Electrical Equipment & Parts, 	Electrical Equipment, Consumer Electronics, Computer Hardware
    COMMUNICATIONS = 18  # Air Freight & Logistics, 	Electrical Equipment & Parts, 	Electrical Equipment, 	Diversified Telecommunication Services, 	Communications Equipment, 	Multi-Utilities, Software-Infrastructure, Road & Rail, 	Wireless Telecommunication Services, 	Telecom Services
    COMMERCIAL = 19  # Containers & Packaging, Air Freight & Logistics, Auto Components, Auto Manufacturers, Auto Parts, 	Commercial Services & Supplies, Industrial Conglomerates, 	Household Durables, Packaging & Containers, 	Trading Companies & Distributors
    CHEMICALS = 20  # Biotechnology, 	Diagnostics & Research, Construction Materials, Chemicals, 	Life Sciences Tools & Services, Specialty Chemicals
    BANKS = 21  # Asset Management, Banks, Banks-Diversified, Banks-Regional, Diversified Financial Services, Credit Services, Consumer Finance, Capital Markets, Insurance, 	Thrifts & Mortgage Finance
    AEROSPACE = 22  # Aerospace & Defense, Solar, 	Security & Protection Services, Road & Rail, Transportation Infrastructure
    AIRLINES = (
        23  # Air Freight & Logistics, Airlines, Airports, Transportation Infrastructure
    )
    AUTO = 24  # Auto & Truck Dealerships, 	Auto Components, Auto Manufacturers, Auto Parts, Automobiles, Transportation Infrastructure
