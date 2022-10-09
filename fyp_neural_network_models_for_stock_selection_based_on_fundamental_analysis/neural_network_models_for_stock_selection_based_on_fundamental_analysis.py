#!/usr/bin/env python
# coding: utf-8

# # Import libraries
# 
# [Paper reference](https://ieeexplore.ieee.org.remotexs.ntu.edu.sg/stamp/stamp.jsp?tp=&arnumber=8861550&tag=1)

# In[1]:


import pandas as pd
from tqdm.notebook import tqdm_notebook as pb

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:99% !important; }</style>"))


# # Get the dataset required

# ## Automating data download

# In[40]:


stock_ticker = [
'A - Agilent Technol...: XLS, CSV',
'AAL - American Airlin...: XLS, CSV',
'AAN - Aaron’s, Inc.: XLS, CSV',
'AAP - Advance Auto Pa...: XLS, CSV',
'AAPL - Apple Inc.: XLS, CSV',
'ABBV - AbbVie Inc.: XLS, CSV',
'ABC - AmerisourceBerg...: XLS, CSV',
'ABI - Applied Biosyst...: XLS, CSV',
'ABMD - ABIOMED, Inc.: XLS, CSV',
'ABT - Abbott Laborato...: XLS, CSV',
'ACAS - American Capita...: XLS, CSV',
'ACC - American Campus...: XLS, CSV',
'ACIW - ACI Worldwide, ...: XLS, CSV',
'ACM - AECOM: XLS, CSV',
'ACN - Accenture plc: XLS, CSV',
'ACS - Affiliated Comp...: XLS, CSV',
'ACV - Alberto-Culver ...: XLS, CSV',
'ACXM - Acxiom Corporation: XLS, CSV',
'ADBE - Adobe Systems I...: XLS, CSV',
'ADCT - ADC Telecommuni...: XLS, CSV',
'ADI - Analog Devices,...: XLS, CSV',
'ADM - Archer-Daniels-...: XLS, CSV',
'ADP - Automatic Data ...: XLS, CSV',
'ADS - Alliance Data S...: XLS, CSV',
'ADSK - Autodesk, Inc.: XLS, CSV',
'ADT - The ADT Corpora...: XLS, CSV',
'AEE - Ameren Corporation: XLS, CSV',
'AEO - American Eagle ...: XLS, CSV',
'AEP - American Electr...: XLS, CSV',
'AES - The AES Corpora...: XLS, CSV',
'AET - Aetna Inc.: XLS, CSV',
'AFG - American Financ...: XLS, CSV',
'AFL - Aflac Incorporated: XLS, CSV',
'AGCO - AGCO Corporation: XLS, CSV',
'AGN - Allergan Inc: XLS, CSV',
'AGN - Allergan plc: XLS, CSV',
'AHL - Aspen Insurance...: XLS, CSV',
'AIG - American Intern...: XLS, CSV',
'AIV - Apartment Inves...: XLS, CSV',
'AIZ - Assurant, Inc.: XLS, CSV',
'AJG - Arthur J. Galla...: XLS, CSV',
'AKAM - Akamai Technolo...: XLS, CSV',
'AKRX - Akorn, Inc.: XLS, CSV',
'ALB - Albemarle Corpo...: XLS, CSV',
'ALEX - Alexander & Bal...: XLS, CSV',
'ALGN - Align Technolog...: XLS, CSV',
'ALK - Alaska Air Grou...: XLS, CSV',
'ALL - The Allstate Co...: XLS, CSV',
'ALLE - Allegion plc: XLS, CSV',
'ALTR - Altera Corporation: XLS, CSV',
'ALXN - Alexion Pharmac...: XLS, CSV',
'AMAT - Applied Materia...: XLS, CSV',
'AMBC - Ambac Financial...: XLS, CSV',
'AMCX - AMC Networks Inc.: XLS, CSV',
'AMD - Advanced Micro ...: XLS, CSV',
'AME - AMETEK, Inc.: XLS, CSV',
'AMG - Affiliated Mana...: XLS, CSV',
'AMGN - Amgen Inc.: XLS, CSV',
'AMP - Ameriprise Fina...: XLS, CSV',
'AMSC - American Superc...: XLS, CSV',
'AMT - American Tower ...: XLS, CSV',
'AMZN - Amazon.com, Inc.: XLS, CSV',
'AN - AutoNation, Inc.: XLS, CSV',
'ANDV - Andeavor: XLS, CSV',
'ANDW - Andrew Corporation: XLS, CSV',
'ANF - Abercrombie & F...: XLS, CSV',
'ANR - Alpha Natural R...: XLS, CSV',
'ANSS - ANSYS, Inc.: XLS, CSV',
'ANTM - Anthem, Inc.: XLS, CSV',
'AON - Aon plc: XLS, CSV',
'AOS - A. O. Smith Cor...: XLS, CSV',
'APA - Apache Corporation: XLS, CSV',
'APC - Anadarko Petrol...: XLS, CSV',
'APD - Air Products an...: XLS, CSV',
'APH - Amphenol Corpor...: XLS, CSV',
'APOL - Apollo Educatio...: XLS, CSV',
'APU - AmeriGas Partne...: XLS, CSV',
'ARE - Alexandria Real...: XLS, CSV',
'ARG - Airgas, Inc.: XLS, CSV',
'ARNC - Arconic Inc.: XLS, CSV',
'ARRS - ARRIS Internati...: XLS, CSV',
'ARW - Arrow Electroni...: XLS, CSV',
'ASH - Ashland Inc.: XLS, CSV',
'ATGE - Adtalem Global ...: XLS, CSV',
'ATI - Allegheny Techn...: XLS, CSV',
'ATVI - Activision Bliz...: XLS, CSV',
'AVB - AvalonBay Commu...: XLS, CSV',
'AVGO - Broadcom Limited: XLS, CSV',
'AVP - Avon Products, ...: XLS, CSV',
'AVY - Avery Dennison ...: XLS, CSV',
'AW - Allied Waste In...: XLS, CSV',
'AWK - American Water ...: XLS, CSV',
'AXP - American Expres...: XLS, CSV',
'AYE - Allegheny Energ...: XLS, CSV',
'AYI - Acuity Brands, ...: XLS, CSV',
'AZO - AutoZone, Inc.: XLS, CSV',
'BA - The Boeing Company: XLS, CSV',
'BAC - Bank of America...: XLS, CSV',
'BAX - Baxter Internat...: XLS, CSV',
'BBBY - Bed Bath & Beyo...: XLS, CSV',
'BBT - BB&T Corporation: XLS, CSV',
'BBY - Best Buy Co., Inc.: XLS, CSV',
'BC - Brunswick Corpo...: XLS, CSV',
'BCR - C. R. Bard, Inc.: XLS, CSV',
'BDK - Black & Decker ...: XLS, CSV',
'BDX - Becton, Dickins...: XLS, CSV',
'BEAM - Beam Inc: XLS, CSV',
'BEN - Franklin Resour...: XLS, CSV',
'BF.A - Brown-Forman Co...: XLS, CSV',
'BHF - Brighthouse Fin...: XLS, CSV',
'BHI - Baker Hughes In...: XLS, CSV',
'BIG - Big Lots, Inc.: XLS, CSV',
'BIIB - Biogen Inc.: XLS, CSV',
'BJS - BJ Services Com...: XLS, CSV',
'BK - The Bank of New...: XLS, CSV',
'BKE - The Buckle, Inc.: XLS, CSV',
'BLK - BlackRock, Inc.: XLS, CSV',
'BLL - Ball Corporation: XLS, CSV',
'BMC - BMC Software Inc: XLS, CSV',
'BMS - Bemis Company, ...: XLS, CSV',
'BMY - Bristol-Myers S...: XLS, CSV',
'BNI - Burlington Nort...: XLS, CSV',
'BRCM - Broadcom Corpor...: XLS, CSV',
'BRK.A - Berkshire Hatha...: XLS, CSV',
'BRL - Barr Pharmaceut...: XLS, CSV',
'BRLI - Bio-Reference L...: XLS, CSV',
'BSC - Bear Stearns Co...: XLS, CSV',
'BSX - Boston Scientif...: XLS, CSV',
'BTU - Peabody Energy ...: XLS, CSV',
'BUD - Anheuser-busch ...: XLS, CSV',
'BWA - BorgWarner Inc.: XLS, CSV',
'BXP - Boston Properti...: XLS, CSV',
'C - Citigroup Inc: XLS, CSV',
'CA - CA, Inc.: XLS, CSV',
'CAG - ConAgra Foods, ...: XLS, CSV',
'CAH - Cardinal Health...: XLS, CSV',
'CAM - Cameron Interna...: XLS, CSV',
'CAT - Caterpillar Inc.: XLS, CSV',
'CB - Chubb Limited: XLS, CSV',
'CB - Chubb Corp: XLS, CSV',
'CBE - Cooper Industri...: XLS, CSV',
'CBG - CBRE Group, Inc.: XLS, CSV',
'CBOE - CBOE Holdings, ...: XLS, CSV',
'CBS - CBS Corporation: XLS, CSV',
'CCE - [Former] Coca-C...: XLS, CSV',
'CCE - Coca-Cola Enter...: XLS, CSV',
'CCI - Crown Castle In...: XLS, CSV',
'CCL - Carnival Corpor...: XLS, CSV',
'CCU - Clear Channel C...: XLS, CSV',
'CDNS - Cadence Design ...: XLS, CSV',
'CEG - Constellation E...: XLS, CSV',
'CELG - Celgene Corpora...: XLS, CSV',
'CERN - Cerner Corporation: XLS, CSV',
'CF - CF Industries H...: XLS, CSV',
'CFC - Countrywide Fin...: XLS, CSV',
'CFG - Citizens Financ...: XLS, CSV',
'CFN - CareFusion Corp...: XLS, CSV',
'CHD - Church & Dwight...: XLS, CSV',
'CHK - Chesapeake Ener...: XLS, CSV',
'CHRW - C.H. Robinson W...: XLS, CSV',
'CI - Cigna Corporation: XLS, CSV',
'CIEN - Ciena Corporation: XLS, CSV',
'CINF - Cincinnati Fina...: XLS, CSV',
'CIT - CIT Group Inc.: XLS, CSV',
'CL - Colgate-Palmoli...: XLS, CSV',
'CLF - Cliffs Natural ...: XLS, CSV',
'CLX - The Clorox Company: XLS, CSV',
'CMA - Comerica Incorp...: XLS, CSV',
'CMCSA - Comcast Corpora...: XLS, CSV',
'CME - CME Group Inc.: XLS, CSV',
'CMG - Chipotle Mexica...: XLS, CSV',
'CMI - Cummins Inc.: XLS, CSV',
'CMS - CMS Energy Corp...: XLS, CSV',
'CMVT - Comverse Techno...: XLS, CSV',
'CNC - Centene Corpora...: XLS, CSV',
'CNO - CNO Financial G...: XLS, CSV',
'CNP - CenterPoint Ene...: XLS, CSV',
'CNX - CONSOL Energy Inc: XLS, CSV',
'COF - Capital One Fin...: XLS, CSV',
'COG - Cabot Oil & Gas...: XLS, CSV',
'COH - Coach, Inc.: XLS, CSV',
'COL - Rockwell Collin...: XLS, CSV',
'COO - The Cooper Comp...: XLS, CSV',
'COP - ConocoPhillips: XLS, CSV',
'COST - Costco Wholesal...: XLS, CSV',
'COTY - Coty Inc.: XLS, CSV',
'COV - Covidien plc: XLS, CSV',
'CPB - Campbell Soup C...: XLS, CSV',
'CPN - Calpine Corpora...: XLS, CSV',
'CPWR - Compuware Corpo...: XLS, CSV',
'CR - Crane Co.: XLS, CSV',
'CRA - Celera Corporation: XLS, CSV',
'CRM - salesforce.com,...: XLS, CSV',
'CRVL - CorVel Corporation: XLS, CSV',
'CSCO - Cisco Systems, ...: XLS, CSV',
'CSRA - CSRA Inc.: XLS, CSV',
'CSX - CSX Corporation: XLS, CSV',
'CTAS - Cintas Corporation: XLS, CSV',
'CTL - CenturyLink, Inc.: XLS, CSV',
'CTSH - Cognizant Techn...: XLS, CSV',
'CTX - Centex Corporation: XLS, CSV',
'CTXS - Citrix Systems,...: XLS, CSV',
'CVC - Cablevision Sys...: XLS, CSV',
'CVG - Convergys Corpo...: XLS, CSV',
'CVH - Coventry Health...: XLS, CSV',
'CVS - CVS Health Corp...: XLS, CSV',
'CVX - Chevron Corpora...: XLS, CSV',
'CXO - Concho Resource...: XLS, CSV',
'D - Dominion Resour...: XLS, CSV',
'DAL - Delta Air Lines...: XLS, CSV',
'DCI - Donaldson Compa...: XLS, CSV',
'DD - E. I. Du Pont D...: XLS, CSV',
'DDR - DDR Corp.: XLS, CSV',
'DDS - Dillard, Inc.: XLS, CSV',
'DE - Deere & Company: XLS, CSV',
'DELL - Dell Inc.: XLS, CSV',
'DF - Dean Foods Company: XLS, CSV',
'DFS - Discover Financ...: XLS, CSV',
'DG - Dollar General ...: XLS, CSV',
'DGX - Quest Diagnosti...: XLS, CSV',
'DHI - D.R. Horton, Inc.: XLS, CSV',
'DHR - Danaher Corpora...: XLS, CSV',
'DIS - The Walt Disney...: XLS, CSV',
'DISCA - Discovery Commu...: XLS, CSV',
'DISH - DISH Network Co...: XLS, CSV',
'DLPH - Delphi Automoti...: XLS, CSV',
'DLR - Digital Realty ...: XLS, CSV',
'DLTR - Dollar Tree, Inc.: XLS, CSV',
'DNB - Dun & Bradstree...: XLS, CSV',
'DNR - Denbury Resourc...: XLS, CSV',
'DO - Diamond Offshor...: XLS, CSV',
'DOV - Dover Corporation: XLS, CSV',
'DPS - Dr Pepper Snapp...: XLS, CSV',
'DRE - Duke Realty Cor...: XLS, CSV',
'DRI - Darden Restaura...: XLS, CSV',
'DTE - DTE Energy Company: XLS, CSV',
'DTV - DIRECTV: XLS, CSV',
'DUK - Duke Energy Cor...: XLS, CSV',
'DVA - DaVita HealthCa...: XLS, CSV',
'DVN - Devon Energy Co...: XLS, CSV',
'DWDP - DowDuPont Inc.: XLS, CSV',
'DXC - DXC Technology ...: XLS, CSV',
'DYN - Dynegy Inc.: XLS, CSV',
'EA - Electronic Arts...: XLS, CSV',
'EBAY - eBay Inc.: XLS, CSV',
'ECL - Ecolab Inc.: XLS, CSV',
'ED - Consolidated Ed...: XLS, CSV',
'EDS - Electronic Data...: XLS, CSV',
'EFX - Equifax Inc.: XLS, CSV',
'EIX - Edison Internat...: XLS, CSV',
'EL - The Estée Laude...: XLS, CSV',
'EMC - EMC Corporation: XLS, CSV',
'EMN - Eastman Chemica...: XLS, CSV',
'EMR - Emerson Electri...: XLS, CSV',
'ENDP - Endo Internatio...: XLS, CSV',
'EOG - EOG Resources, ...: XLS, CSV',
'EP - El Paso Corpora...: XLS, CSV',
'EQ - Embarq Corporation: XLS, CSV',
'EQIX - Equinix, Inc.: XLS, CSV',
'EQR - Equity Residential: XLS, CSV',
'EQT - EQT Corporation: XLS, CSV',
'ES - Eversource Energy: XLS, CSV',
'ESRX - Express Scripts...: XLS, CSV',
'ESS - Essex Property ...: XLS, CSV',
'ESV - Ensco plc: XLS, CSV',
'ETFC - E*TRADE Financi...: XLS, CSV',
'ETN - Eaton Corporati...: XLS, CSV',
'ETR - Entergy Corpora...: XLS, CSV',
'EW - Edwards Lifesci...: XLS, CSV',
'EXC - Exelon Corporation: XLS, CSV',
'EXPD - Expeditors Inte...: XLS, CSV',
'EXPE - Expedia, Inc.: XLS, CSV',
'EXR - Extra Space Sto...: XLS, CSV',
'F - Ford Motor Company: XLS, CSV',
'FAST - Fastenal Company: XLS, CSV',
'FB - Facebook, Inc.: XLS, CSV',
'FBHS - Fortune Brands ...: XLS, CSV',
'FCX - Freeport-McMoRa...: XLS, CSV',
'FDO - Family Dollar S...: XLS, CSV',
'FDS - FactSet Researc...: XLS, CSV',
'FDX - FedEx Corporation: XLS, CSV',
'FE - FirstEnergy Corp.: XLS, CSV',
'FFIV - F5 Networks, Inc.: XLS, CSV',
'FHN - First Horizon N...: XLS, CSV',
'FII - Federated Inves...: XLS, CSV',
'FIS - Fidelity Nation...: XLS, CSV',
'FISV - Fiserv, Inc.: XLS, CSV',
'FITB - Fifth Third Ban...: XLS, CSV',
'FL - Foot Locker, Inc.: XLS, CSV',
'FLIR - FLIR Systems, Inc.: XLS, CSV',
'FLR - Fluor Corporation: XLS, CSV',
'FLS - Flowserve Corpo...: XLS, CSV',
'FMC - FMC Corporation: XLS, CSV',
'FMCC - Federal Home Lo...: XLS, CSV',
'FNMA - Federal Nationa...: XLS, CSV',
'FOSL - Fossil Group, Inc.: XLS, CSV',
'FOX - Twenty-First Ce...: XLS, CSV',
'FRT - Federal Realty ...: XLS, CSV',
'FRX - Forest Laborato...: XLS, CSV',
'FSLR - First Solar, Inc.: XLS, CSV',
'FTI - FMC Technologie...: XLS, CSV',
'FTR - Frontier Commun...: XLS, CSV',
'FTV - Fortive Corpora...: XLS, CSV',
'GAS - Nicor Inc: XLS, CSV',
'GAS - AGL Resources Inc.: XLS, CSV',
'GCI - Gannett Co., Inc.: XLS, CSV',
'GD - General Dynamic...: XLS, CSV',
'GE - General Electri...: XLS, CSV',
'GENZ - Genzyme Corp: XLS, CSV',
'GGP - General Growth ...: XLS, CSV',
'GGP - General Growth ...: XLS, CSV',
'GHC - Graham Holdings...: XLS, CSV',
'GILD - Gilead Sciences...: XLS, CSV',
'GIS - General Mills, ...: XLS, CSV',
'GLAD - Gladstone Capit...: XLS, CSV',
'GLW - Corning Incorpo...: XLS, CSV',
'GM - General Motors ...: XLS, CSV',
'GM - Motors Liquidat...: XLS, CSV',
'GME - GameStop Corp.: XLS, CSV',
'GNW - Genworth Holdin...: XLS, CSV',
'GOOG - Alphabet Inc.: XLS, CSV',
'GPC - Genuine Parts C...: XLS, CSV',
'GPN - Global Payments...: XLS, CSV',
'GPS - The Gap, Inc.: XLS, CSV',
'GR - Goodrich Corpor...: XLS, CSV',
'GRA - W. R. Grace & Co.: XLS, CSV',
'GRMN - Garmin Ltd.: XLS, CSV',
'GS - The Goldman Sac...: XLS, CSV',
'GT - The Goodyear Ti...: XLS, CSV',
'GWW - W.W. Grainger, ...: XLS, CSV',
'HAL - Halliburton Com...: XLS, CSV',
'HAR - Harman Internat...: XLS, CSV',
'HAS - Hasbro, Inc.: XLS, CSV',
'HBAN - Huntington Banc...: XLS, CSV',
'HBI - Hanesbrands Inc.: XLS, CSV',
'HCA - HCA Holdings, Inc.: XLS, CSV',
'HCBK - Hudson City Ban...: XLS, CSV',
'HCN - Welltower Inc.: XLS, CSV',
'HCP - HCP, Inc.: XLS, CSV',
'HD - The Home Depot,...: XLS, CSV',
'HES - Hess Corporation: XLS, CSV',
'HIBB - Hibbett Sports,...: XLS, CSV',
'HIG - The Hartford Fi...: XLS, CSV',
'HLT - Hilton Worldwid...: XLS, CSV',
'HNZ - H. J. Heinz Com...: XLS, CSV',
'HOG - Harley-Davidson...: XLS, CSV',
'HOLX - Hologic, Inc.: XLS, CSV',
'HON - Honeywell Inter...: XLS, CSV',
'HOT - Starwood Hotel ...: XLS, CSV',
'HP - Helmerich & Pay...: XLS, CSV',
'HPC - Hercules Incorp...: XLS, CSV',
'HPE - Hewlett Packard...: XLS, CSV',
'HPQ - HP Inc.: XLS, CSV',
'HRB - H&R Block, Inc.: XLS, CSV',
'HRL - Hormel Foods Co...: XLS, CSV',
'HRS - Harris Corporation: XLS, CSV',
'HSH - The Hillshire B...: XLS, CSV',
'HSIC - Henry Schein, Inc.: XLS, CSV',
'HSP - Hospira Inc.: XLS, CSV',
'HST - Host Hotels & R...: XLS, CSV',
'HSY - The Hershey Com...: XLS, CSV',
'HUM - Humana Inc.: XLS, CSV',
'IAC - IAC/InterActive...: XLS, CSV',
'IBM - International B...: XLS, CSV',
'ICE - Intercontinenta...: XLS, CSV',
'ICE - NYSE Euronext: XLS, CSV',
'IDXX - IDEXX Laborator...: XLS, CSV',
'IFF - International F...: XLS, CSV',
'IGT - International G...: XLS, CSV',
'ILMN - Illumina, Inc.: XLS, CSV',
'INCY - Incyte Corporation: XLS, CSV',
'INFO - IHS Markit Ltd.: XLS, CSV',
'INTC - Intel Corporation: XLS, CSV',
'INTU - Intuit Inc.: XLS, CSV',
'IP - International P...: XLS, CSV',
'IPG - The Interpublic...: XLS, CSV',
'IQV - IQVIA Holdings ...: XLS, CSV',
'IR - Ingersoll-Rand plc: XLS, CSV',
'IRM - Iron Mountain I...: XLS, CSV',
'ISRG - Intuitive Surgi...: XLS, CSV',
'IT - Gartner, Inc.: XLS, CSV',
'ITT - ITT Corporation: XLS, CSV',
'ITW - Illinois Tool W...: XLS, CSV',
'IVZ - Invesco Ltd.: XLS, CSV',
'JAVA - Sun Microsystem...: XLS, CSV',
'JBHT - J.B. Hunt Trans...: XLS, CSV',
'JBL - Jabil Circuit, ...: XLS, CSV',
'JCI - Johnson Control...: XLS, CSV',
'JCP - J. C. Penney Co...: XLS, CSV',
'JEC - Jacobs Engineer...: XLS, CSV',
'JNJ - Johnson & Johnson: XLS, CSV',
'JNPR - Juniper Network...: XLS, CSV',
'JNS - Janus Capital G...: XLS, CSV',
'JNY - The Jones Group...: XLS, CSV',
'JPM - JPMorgan Chase ...: XLS, CSV',
'JWN - Nordstrom Inc: XLS, CSV',
'K - Kellogg Company: XLS, CSV',
'KATE - Kate Spade & Co...: XLS, CSV',
'KBH - KB Home: XLS, CSV',
'KEY - KeyCorp: XLS, CSV',
'KG - King Pharmaceut...: XLS, CSV',
'KHC - The Kraft Heinz...: XLS, CSV',
'KIM - Kimco Realty Co...: XLS, CSV',
'KLAC - KLA-Tencor Corp...: XLS, CSV',
'KMB - Kimberly-Clark ...: XLS, CSV',
'KMI - Kinder Morgan, ...: XLS, CSV',
'KMX - CarMax, Inc.: XLS, CSV',
'KO - The Coca-Cola C...: XLS, CSV',
'KODK - Eastman Kodak C...: XLS, CSV',
'KORS - Michael Kors Ho...: XLS, CSV',
'KR - The Kroger Co.: XLS, CSV',
'KRFT - Kraft Foods Gro...: XLS, CSV',
'KSS - Kohl Corporation: XLS, CSV',
'KSU - Kansas City Sou...: XLS, CSV',
'L - Loews Corporation: XLS, CSV',
'LB - L Brands, Inc.: XLS, CSV',
'LDOS - Leidos Holdings...: XLS, CSV',
'LEG - Leggett & Platt...: XLS, CSV',
'LEH - Lehman Brothers...: XLS, CSV',
'LEN - Lennar Corporation: XLS, CSV',
'LH - Laboratory Corp...: XLS, CSV',
'LIFE - Life Technologi...: XLS, CSV',
'LKQ - LKQ Corporation: XLS, CSV',
'LLL - L-3 Communicati...: XLS, CSV',
'LLTC - Linear Technolo...: XLS, CSV',
'LLY - Eli Lilly and C...: XLS, CSV',
'LM - Legg Mason, Inc.: XLS, CSV',
'LMT - Lockheed Martin...: XLS, CSV',
'LNC - Lincoln Nationa...: XLS, CSV',
'LNKD - LinkedIn Corpor...: XLS, CSV',
'LNT - Alliant Energy ...: XLS, CSV',
'LOW - Lowe’s Companie...: XLS, CSV',
'LRCX - Lam Research Co...: XLS, CSV',
'LSI - LSI Corp: XLS, CSV',
'LSTR - Landstar System...: XLS, CSV',
'LUK - Leucadia Nation...: XLS, CSV',
'LUV - Southwest Airli...: XLS, CSV',
'LVLT - Level 3 Communi...: XLS, CSV',
'LXK - Lexmark Interna...: XLS, CSV',
'LYB - LyondellBasell ...: XLS, CSV',
'M - Macy, Inc: XLS, CSV',
'MA - MasterCard Inco...: XLS, CSV',
'MAA - Mid-America Apa...: XLS, CSV',
'MAC - The Macerich Co...: XLS, CSV',
'MAR - Marriott Intern...: XLS, CSV',
'MAS - Masco Corporation: XLS, CSV',
'MAT - Mattel, Inc.: XLS, CSV',
'MBI - MBIA Inc.: XLS, CSV',
'MCD - McDonald Corp...: XLS, CSV',
'MCHP - Microchip Techn...: XLS, CSV',
'MCK - McKesson Corpor...: XLS, CSV',
'MCO - Moody’s Corpora...: XLS, CSV',
'MDLZ - Mondelez Intern...: XLS, CSV',
'MDP - Meredith Corpor...: XLS, CSV',
'MDT - Medtronic Publi...: XLS, CSV',
'MED - Medifast, Inc.: XLS, CSV',
'MER - Merrill Lynch &...: XLS, CSV',
'MET - MetLife, Inc.: XLS, CSV',
'MFE - McAfee, Inc.: XLS, CSV',
'MGM - MGM Resorts Int...: XLS, CSV',
'MHK - Mohawk Industri...: XLS, CSV',
'MHS - Medco Health So...: XLS, CSV',
'MI - Marshall & Ilsl...: XLS, CSV',
'MIL - Millipore Corpo...: XLS, CSV',
'MJN - Mead Johnson Nu...: XLS, CSV',
'MKC - McCormick & Com...: XLS, CSV',
'MLM - Martin Marietta...: XLS, CSV',
'MMC - Marsh & McLenna...: XLS, CSV',
'MMM - 3M Company: XLS, CSV',
'MNK - Mallinckrodt plc: XLS, CSV',
'MNST - Monster Beverag...: XLS, CSV',
'MO - Altria Group, Inc.: XLS, CSV',
'MOLX - Molex Incorporated: XLS, CSV',
'MON - Monsanto Company: XLS, CSV',
'MOS - The Mosaic Company: XLS, CSV',
'MPC - Marathon Petrol...: XLS, CSV',
'MRK - Merck & Co., Inc.: XLS, CSV',
'MRO - Marathon Oil Co...: XLS, CSV',
'MS - Morgan Stanley: XLS, CSV',
'MSFT - Microsoft Corpo...: XLS, CSV',
'MSI - Motorola Soluti...: XLS, CSV',
'MTB - M&T Bank Corpor...: XLS, CSV',
'MTD - Mettler-Toledo ...: XLS, CSV',
'MTG - MGIC Investment...: XLS, CSV',
'MTW - The Manitowoc C...: XLS, CSV',
'MU - Micron Technolo...: XLS, CSV',
'MUR - Murphy Oil Corp...: XLS, CSV',
'MWV - MeadWestvaco Co...: XLS, CSV',
'MWW - Monster Worldwi...: XLS, CSV',
'MYL - Mylan N.V.: XLS, CSV',
'NAV - Navistar Intern...: XLS, CSV',
'NAVI - Navient Corpora...: XLS, CSV',
'NBL - Noble Energy, Inc.: XLS, CSV',
'NBR - Nabors Industri...: XLS, CSV',
'NCC - National City C...: XLS, CSV',
'NCLH - Norwegian Cruis...: XLS, CSV',
'NDAQ - Nasdaq, Inc.: XLS, CSV',
'NE - Noble Corporation: XLS, CSV',
'NEE - NextEra Energy,...: XLS, CSV',
'NEM - Newmont Mining ...: XLS, CSV',
'NFLX - Netflix, Inc.: XLS, CSV',
'NFX - Newfield Explor...: XLS, CSV',
'NI - NiSource Inc.: XLS, CSV',
'NILE - Blue Nile, Inc.: XLS, CSV',
'NKE - NIKE, Inc.: XLS, CSV',
'NLSN - Nielsen Holding...: XLS, CSV',
'NOC - Northrop Grumma...: XLS, CSV',
'NOV - National Oilwel...: XLS, CSV',
'NOVL - Novell, Inc.: XLS, CSV',
'NRG - NRG Energy, Inc.: XLS, CSV',
'NSC - Norfolk Souther...: XLS, CSV',
'NSM - National Semico...: XLS, CSV',
'NTAP - NetApp, Inc.: XLS, CSV',
'NTRS - Northern Trust ...: XLS, CSV',
'NUE - Nucor Corporation: XLS, CSV',
'NUS - Nu Skin Enterpr...: XLS, CSV',
'NVDA - NVIDIA Corporation: XLS, CSV',
'NVLS - Novellus System...: XLS, CSV',
'NWL - Newell Rubberma...: XLS, CSV',
'NWS - News Corporation: XLS, CSV',
'NYT - The New York Ti...: XLS, CSV',
'O - Realty Income C...: XLS, CSV',
'ODP - Office Depot, Inc.: XLS, CSV',
'OFLX - Omega Flex, Inc.: XLS, CSV',
'OI - Owens-Illinois,...: XLS, CSV',
'OKE - ONEOK, Inc.: XLS, CSV',
'OMC - Omnicom Group Inc.: XLS, CSV',
'OMX - OfficeMax Incor...: XLS, CSV',
'ORCL - Oracle Corporation: XLS, CSV',
'ORLY - OReilly Automo...: XLS, CSV',
'OXY - Occidental Petr...: XLS, CSV',
'PAYX - Paychex, Inc.: XLS, CSV',
'PBCT - People’s United...: XLS, CSV',
'PBG - The Pepsi Bottl...: XLS, CSV',
'PBI - Pitney Bowes Inc.: XLS, CSV',
'PCAR - PACCAR Inc: XLS, CSV',
'PCG - PG&E Corporation: XLS, CSV',
'PCL - Plum Creek Timb...: XLS, CSV',
'PCLN - The Priceline G...: XLS, CSV',
'PCP - Precision Castp...: XLS, CSV',
'PDCO - Patterson Compa...: XLS, CSV',
'PEG - Public Service ...: XLS, CSV',
'PEP - PepsiCo, Inc.: XLS, CSV',
'PETM - PetSmart, Inc: XLS, CSV',
'PETS - PetMed Express,...: XLS, CSV',
'PFE - Pfizer Inc.: XLS, CSV',
'PFG - Principal Finan...: XLS, CSV',
'PFIE - Profire Energy,...: XLS, CSV',
'PG - The Procter & G...: XLS, CSV',
'PGN - Progress Energy...: XLS, CSV',
'PGR - The Progressive...: XLS, CSV',
'PH - Parker-Hannifin...: XLS, CSV',
'PHM - PulteGroup, Inc.: XLS, CSV',
'PKG - Packaging Corpo...: XLS, CSV',
'PKI - PerkinElmer, Inc.: XLS, CSV',
'PLD - [] ProLogis: XLS, CSV',
'PLD - Prologis, Inc.: XLS, CSV',
'PLL - Pall Corp: XLS, CSV',
'PM - Philip Morris I...: XLS, CSV',
'PNC - The PNC Financi...: XLS, CSV',
'PNR - Pentair plc: XLS, CSV',
'PNW - Pinnacle West C...: XLS, CSV',
'POM - Pepco Holdings Inc: XLS, CSV',
'PPG - PPG Industries,...: XLS, CSV',
'PPL - PPL Corporation: XLS, CSV',
'PRGO - Perrigo Company...: XLS, CSV',
'PRU - Prudential Fina...: XLS, CSV',
'PSA - Public Storage: XLS, CSV',
'PSX - Phillips 66: XLS, CSV',
'PTC - PTC Inc.: XLS, CSV',
'PTV - Pactiv Corporation: XLS, CSV',
'PVH - PVH Corp.: XLS, CSV',
'PWR - Quanta Services...: XLS, CSV',
'PX - Praxair, Inc.: XLS, CSV',
'PXD - Pioneer Natural...: XLS, CSV',
'PYPL - PayPal Holdings...: XLS, CSV',
'Q - Qwest Communica...: XLS, CSV',
'QCOM - QUALCOMM Incorp...: XLS, CSV',
'QLGC - QLogic Corporation: XLS, CSV',
'QRVO - Qorvo, Inc.: XLS, CSV',
'QSII - Quality Systems...: XLS, CSV',
'R - Ryder System, Inc.: XLS, CSV',
'RAD - Rite Aid Corpor...: XLS, CSV',
'RAI - Reynolds Americ...: XLS, CSV',
'RAVN - Raven Industrie...: XLS, CSV',
'RCL - Royal Caribbean...: XLS, CSV',
'RDC - Rowan Companies...: XLS, CSV',
'RE - Everest Re Grou...: XLS, CSV',
'REG - Regency Centers...: XLS, CSV',
'REGN - Regeneron Pharm...: XLS, CSV',
'RF - Regions Financi...: XLS, CSV',
'RHI - Robert Half Int...: XLS, CSV',
'RHT - Red Hat, Inc.: XLS, CSV',
'RIG - Transocean Ltd.: XLS, CSV',
'RJF - Raymond James F...: XLS, CSV',
'RL - Ralph Lauren Co...: XLS, CSV',
'RMD - ResMed Inc.: XLS, CSV',
'ROH - Rohm and Haas C...: XLS, CSV',
'ROK - Rockwell Automa...: XLS, CSV',
'ROP - Roper Technolog...: XLS, CSV',
'ROST - Ross Stores, Inc.: XLS, CSV',
'RRC - Range Resources...: XLS, CSV',
'RRD - R.R. Donnelley ...: XLS, CSV',
'RSG - Republic Servic...: XLS, CSV',
'RSH - RadioShack Corp...: XLS, CSV',
'RTN - Raytheon Company: XLS, CSV',
'RX - IMS Health Inco...: XLS, CSV',
'S - Sprint Corporation: XLS, CSV',
'SAF - Safeco Corporation: XLS, CSV',
'SAM - The Boston Beer...: XLS, CSV',
'SANM - Sanmina Corpora...: XLS, CSV',
'SAPE - Sapient Corp: XLS, CSV',
'SBAC - SBA Communicati...: XLS, CSV',
'SBL - Symbol Technolo...: XLS, CSV',
'SBUX - Starbucks Corpo...: XLS, CSV',
'SCG - SCANA Corporation: XLS, CSV',
'SCHW - The Charles Sch...: XLS, CSV',
'SE - Spectra Energy ...: XLS, CSV',
'SEE - Sealed Air Corp...: XLS, CSV',
'SGP - Schering-Plough...: XLS, CSV',
'SHLD - Sears Holdings ...: XLS, CSV',
'SHW - The Sherwin-Wil...: XLS, CSV',
'SIAL - Sigma-Aldrich C...: XLS, CSV',
'SIG - Signet Jewelers...: XLS, CSV',
'SII - Smith Internati...: XLS, CSV',
'SJM - The J. M. Smuck...: XLS, CSV',
'SLB - Schlumberger Li...: XLS, CSV',
'SLG - SL Green Realty...: XLS, CSV',
'SLM - SLM Corporation: XLS, CSV',
'SNA - Snap-on Incorpo...: XLS, CSV',
'SNDK - Sandisk Corp: XLS, CSV',
'SNI - Scripps Network...: XLS, CSV',
'SNPS - Synopsys, Inc.: XLS, CSV',
'SO - The Southern Co...: XLS, CSV',
'SOV - Sovereign Banco...: XLS, CSV',
'SPG - Simon Property ...: XLS, CSV',
'SPGI - S&P Global Inc.: XLS, CSV',
'SPLS - Staples, Inc.: XLS, CSV',
'SRCL - Stericycle, Inc.: XLS, CSV',
'SRE - Sempra Energy: XLS, CSV',
'SSP - The E. W. Scrip...: XLS, CSV',
'STI - SunTrust Banks,...: XLS, CSV',
'STJ - St. Jude Medica...: XLS, CSV',
'STR - Questar Corpora...: XLS, CSV',
'STT - State Street Co...: XLS, CSV',
'STX - Seagate Technol...: XLS, CSV',
'STZ - Constellation B...: XLS, CSV',
'SUN - Sunoco Inc: XLS, CSV',
'SUNEQ - SunEdison, Inc.: XLS, CSV',
'SVU - SUPERVALU INC.: XLS, CSV',
'SWK - Stanley Black &...: XLS, CSV',
'SWKS - Skyworks Soluti...: XLS, CSV',
'SWN - Southwestern En...: XLS, CSV',
'SWY - Safeway Inc.: XLS, CSV',
'SYF - Synchrony Finan...: XLS, CSV',
'SYK - Stryker Corpora...: XLS, CSV',
'SYMC - Symantec Corpor...: XLS, CSV',
'SYNT - Syntel, Inc.: XLS, CSV',
'SYY - Sysco Corporation: XLS, CSV',
'T - AT&T Inc.: XLS, CSV',
'TAP - Molson Coors Br...: XLS, CSV',
'TDC - Teradata Corpor...: XLS, CSV',
'TDG - TransDigm Group...: XLS, CSV',
'TE - TECO Energy, Inc.: XLS, CSV',
'TEG - Integrys Energy...: XLS, CSV',
'TEL - TE Connectivity...: XLS, CSV',
'TER - Teradyne, Inc.: XLS, CSV',
'TEX - Terex Corporation: XLS, CSV',
'TGNA - TEGNA Inc.: XLS, CSV',
'TGT - Target Corporation: XLS, CSV',
'THC - Tenet Healthcar...: XLS, CSV',
'TIE - Titanium Metals...: XLS, CSV',
'TIF - Tiffany & Co.: XLS, CSV',
'TIN - Temple-Inland Inc.: XLS, CSV',
'TJX - The TJX Compani...: XLS, CSV',
'TKR - The Timken Company: XLS, CSV',
'TLAB - Tellabs, Inc.: XLS, CSV',
'TMK - Torchmark Corpo...: XLS, CSV',
'TMO - Thermo Fisher S...: XLS, CSV',
'TRIP - TripAdvisor, Inc.: XLS, CSV',
'TROW - T. Rowe Price G...: XLS, CSV',
'TRV - The Travelers C...: XLS, CSV',
'TSCO - Tractor Supply ...: XLS, CSV',
'TSLA - Tesla Motors, Inc.: XLS, CSV',
'TSN - Tyson Foods, Inc.: XLS, CSV',
'TSS - Total System Se...: XLS, CSV',
'TT - Trane Inc: XLS, CSV',
'TWC - Time Warner Cab...: XLS, CSV',
'TWTR - Twitter, Inc.: XLS, CSV',
'TWX - Time Warner Inc.: XLS, CSV',
'TXN - Texas Instrumen...: XLS, CSV',
'TXT - Textron Inc.: XLS, CSV',
'TYC - Tyco Internatio...: XLS, CSV',
'UA - Under Armour, Inc.: XLS, CSV',
'UAL - United Continen...: XLS, CSV',
'UDR - UDR, Inc.: XLS, CSV',
'UG - United-Guardian...: XLS, CSV',
'UHS - Universal Healt...: XLS, CSV',
'UIS - Unisys Corporation: XLS, CSV',
'ULTA - Ulta Salon, Cos...: XLS, CSV',
'UNH - UnitedHealth Gr...: XLS, CSV',
'UNM - Unum Group: XLS, CSV',
'UNP - Union Pacific C...: XLS, CSV',
'UPS - United Parcel S...: XLS, CSV',
'URBN - Urban Outfitter...: XLS, CSV',
'URI - United Rentals,...: XLS, CSV',
'USB - U.S. Bancorp: XLS, CSV',
'UST - UST Inc.: XLS, CSV',
'UTX - United Technolo...: XLS, CSV',
'V - Visa Inc.: XLS, CSV',
'VAR - Varian Medical ...: XLS, CSV',
'VFC - V.F. Corporation: XLS, CSV',
'VIA - Viacom, Inc.: XLS, CSV',
'VIAV - Viavi Solutions...: XLS, CSV',
'VIVO - Meridian Biosci...: XLS, CSV',
'VLO - Valero Energy C...: XLS, CSV',
'VMC - Vulcan Material...: XLS, CSV',
'VNO - Vornado Realty ...: XLS, CSV',
'VRSK - Verisk Analytic...: XLS, CSV',
'VRSN - VeriSign, Inc.: XLS, CSV',
'VRTX - Vertex Pharmace...: XLS, CSV',
'VTR - Ventas Inc: XLS, CSV',
'VZ - Verizon Communi...: XLS, CSV',
'WAG - Walgreen Co: XLS, CSV',
'WAT - Waters Corporation: XLS, CSV',
'WB - Wachovia Corpor...: XLS, CSV',
'WBA - Walgreens Boots...: XLS, CSV',
'WDC - Western Digital...: XLS, CSV',
'WDR - Waddell & Reed ...: XLS, CSV',
'WEC - WEC Energy Grou...: XLS, CSV',
'WEN - The Wendy Com...: XLS, CSV',
'WFC - Wells Fargo & C...: XLS, CSV',
'WFM - Whole Foods Mar...: XLS, CSV',
'WFT - Weatherford Int...: XLS, CSV',
'WHR - Whirlpool Corpo...: XLS, CSV',
'WIN - Windstream Hold...: XLS, CSV',
'WINA - Winmark Corpora...: XLS, CSV',
'WLTW - Willis Towers W...: XLS, CSV',
'WM - Waste Managemen...: XLS, CSV',
'WM - Washington Mutu...: XLS, CSV',
'WMB - The Williams Co...: XLS, CSV',
'WMT - Wal-Mart Stores...: XLS, CSV',
'WPX - WPX Energy, Inc.: XLS, CSV',
'WRK - WestRock Company: XLS, CSV',
'WU - The Western Uni...: XLS, CSV',
'WWY - Wm. Wrigley Jr....: XLS, CSV',
'WY - Weyerhaeuser Co...: XLS, CSV',
'WYE - Wyeth: XLS, CSV',
'WYN - Wyndham Worldwi...: XLS, CSV',
'WYNN - Wynn Resorts, L...: XLS, CSV',
'X - United States S...: XLS, CSV',
'XEC - Cimarex Energy Co.: XLS, CSV',
'XEL - Xcel Energy Inc.: XLS, CSV',
'XL - XL Group plc: XLS, CSV',
'XLNX - Xilinx, Inc.: XLS, CSV',
'XOM - Exxon Mobil Cor...: XLS, CSV',
'XRAY - DENTSPLY Intern...: XLS, CSV',
'XRX - Xerox Corporation: XLS, CSV',
'XTO - XTO Energy Inc: XLS, CSV',
'XYL - Xylem Inc.: XLS, CSV',
'YHOO - Yahoo! Inc.: XLS, CSV',
'YUM - YUM! Brands, Inc.: XLS, CSV',
'ZBH - Zimmer Biomet H...: XLS, CSV',
'ZION - Zions Bancorpor...: XLS, CSV',
'ZTS - Zoetis Inc.: XLS, CSV',]


# In[41]:


stock_ticker_formatted = []
for st in stock_ticker:
    stock_ticker_formatted.append(st.split('-')[0].split(' ')[0])


# In[44]:


# automate downloading of files using requests library
import requests
import pickle
import csv

tickers_not_retrieved = [] # may be file name error
financial_data_by_tickers = []
total_tickers = len(stock_ticker_formatted)

for n, st in enumerate(stock_ticker_formatted):
    url = f"https://web.archive.org/web/20180809015717/http://www.stockpup.com/data/{st}_quarterly_financial_data.csv"

    with requests.Session() as s:
        try:
            download = s.get(url)
            decoded_content = download.content.decode('utf-8')
            csv_lines = list(csv.reader(decoded_content.splitlines(), delimiter=','))
            df_financial_data_per_ticker = pd.DataFrame(csv_lines, columns=csv_lines[0]).drop(index=0)
            df_financial_data_per_ticker['ticker'] = st
            financial_data_by_tickers.append(df_financial_data_per_ticker)
            print(f'financial data of {n}/{total_tickers} retrieved')
        except Exception as e:
            print(f'financial data of {n}/{total_tickers} NOT RETRIEVED', 'error:', e)
            tickers_not_retrieved.append(n)


# In[45]:


tickers_not_retrieved


# In[50]:


# output file
with open('financial_dataframes.pkl', 'wb') as file:
    pickle.dump(financial_data_by_tickers, file)


# In[ ]:




