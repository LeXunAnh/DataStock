import json

from datapipe.src.process import insert_stock_list,get_all_symbols,insert_ohlc_data,insert_stock_industry
from src.db import get_connection, close_connection
from src.fetch import fetch_data_ohlc_daily, fetch_securities_hose,fetch_securities_hnx,fetch_intraday_stock_price,save_to_json,get_info_sercurities

if __name__ == "__main__":
    # testing
    symbol = "SSI"
    from_date = "01/08/2025"
    to_date = "01/08/2025"
    #
    print(f"📥 Fetching stock price for {symbol} from {from_date} to {to_date}")
    response = fetch_data_ohlc_daily(symbol, from_date, to_date)
    #response = fetch_securities()
    #save_to_json(response)
    print(response)
    # conn = get_connection()
    batch1 = [
        "AAA", "AAM", "AAT", "ABR", "ABS", "ABT", "ACB", "ACC", "ACG", "ACL", "ADG", "ADP", "ADS", "AGG", "AGM", "AGR",
        "ANV", "APG", "APH", "ASG", "ASM", "ASP", "AST", "BAF", "BBC", "BCE", "BCG", "BCM", "BFC", "BHN", "BIC", "BID",
        "BKG", "BMC", "BMI", "BMP", "BRC", "BSI", "BSR", "BTP", "BTT", "BVH", "BWE", "C32", "C47", "CCC", "CCI", "CCL",
        "CDC", "CHP", "CIG", "CII", "CKG", "CLC", "CLL", "CLW", "CMG", "CMV", "CMX", "CNG",
    ]
    batch2 = [
        "COM", "CRC", "CRE", "CSM", "CSV", "CTD", "CTF", "CTG", "CTI", "CTR", "CTS", "CVT", "D2D", "DAH", "DAT", "DBC", "DBD",
        "DBT", "DC4", "DCL", "DCM", "DGC", "DGW", "DHA", "DHC", "DHG", "DHM", "DIG", "DLG", "DMC", "DPG", "DPM", "DPR",
        "DQC", "DRC", "DRH", "DRL", "DSC", "DSE", "DSN", "DTA", "DTL", "DTT", "DVP", "DXG", "DXS", "DXV", "EIB", "ELC",
        "EVE", "EVF", "EVG", "FCM", "FCN", "FDC", "FIR", "FIT", "FMC",
    ]
    batch3 = [
        "FPT", "FRT", "FTS", "GAS", "GDT", "GEE", "GEG", "GEX", "GIL", "GMD", "GMH", "GSP", "GTA", "GVR", "HAG", "HAH", "HAP", "HAR",
        "HAS", "HAX", "HCD", "HCM", "HDB", "HDC", "HDG", "HHP", "HHS", "HHV", "HID", "HII", "HMC", "HNA", "HPG", "HPX",
        "HQC", "HRC", "HSG", "HSL", "HT1", "HTG", "HTI", "HTL", "HTN", "HTV", "HU1", "HUB", "HVH", "HVN", "HVX", "ICT",
        "IDI", "IJC", "ILB", "IMP", "ITC", "ITD", "JVC", "KBC", "KDC",
    ]
    batch4 = [
        "KDH", "KHG", "KHP", "KMR", "KOS", "KPF", "KSB", "L10", "LAF", "LBM", "LCG", "LDG", "LGC", "LGL", "LHG", "LIX", "LM8", "LPB",
        "LSS", "MBB", "MCM", "MCP", "MDG", "MHC", "MIG", "MSB", "MSH", "MSN", "MWG", "NAB", "NAF", "NAV", "NBB", "NCT",
        "NHA", "NHH", "NHT", "NKG", "NLG", "NNC", "NO1", "NSC", "NT2", "NTL", "NVL", "NVT", "OCB", "OGC", "OPC", "ORS",
        "PAC", "PAN", "PC1", "PDN", "PDR", "PET", "PGC", "PGD",
    ]
    batch5 = [
        "PGI", "PGV", "PHC", "PHR", "PIT", "PJT", "PLP", "PLX", "PMG", "PNC", "PNJ", "POW", "PPC", "PSH", "PTB", "PTC", "PTL", "PVD",
        "PVP", "PVT", "QCG", "QNP", "RAL", "REE", "RYG", "S4A", "SAB", "SAM", "SAV", "SBA", "SBG", "SBT", "SBV", "SC5",
        "SCR", "SCS", "SFC", "SFG", "SFI", "SGN", "SGR", "SGT", "SHA", "SHB", "SHI", "SHP", "SIP", "SJD", "SJS", "SKG",
        "SMA", "SMB", "SMC", "SPM", "SRC", "SRF", "SSB", "SSC",
    ]
    batch6 = [
        "SSI", "ST8", "STB", "STG", "STK", "SVC", "SVD", "SVI", "SVT", "SZC", "SZL", "TBC", "TCB", "TCD", "TCH", "TCI", "TCL", "TCM", "TCO",
        "TCR", "TCT", "TDC", "TDG", "TDH", "TDM", "TDP", "TDW", "TEG", "THG", "TIP", "TIX", "TLD", "TLG", "TLH", "TMP",
        "TMS", "TMT", "TN1", "TNC", "TNH", "TNI", "TNT", "TPB", "TPC", "TRA", "TRC", "TSC", "TTA", "TTE", "TTF", "TV2",
        "TVB", "TVS", "TVT", "TYA", "UIC", "VAF", "VCA", "VCB",
    ]
    batch7 = [
        "VCF", "VCG", "VCI", "VDP", "VDS", "VFG", "VGC", "VHC", "VHM", "VIB", "VIC", "VID", "VIP", "VIX", "VJC", "VMD", "VND", "VNE", "VNG",
        "VNL", "VNM", "VNS", "VOS", "VPB", "VPD", "VPG", "VPH", "VPI", "VPS", "VRC", "VRE", "VSC", "VSH", "VSI", "VTB",
        "VTO", "VTP", "YBM", "YEG"
    ]
    # for symbol in batch7:
    #     stock_industry_df = get_info_sercurities(symbol)
    #     if not stock_industry_df.empty:
    #         insert_stock_industry(stock_industry_df, conn)
    #         print(f"Data {symbol} has been inserted ")
    # else:
    #     print("⚠️ No OHLC data returned.")
    # close_connection(conn)

    #print(response.info())
    #
    # GET STOCK LIST
    # conn = get_connection()
    # if conn:
    #     df_stock_list_h = fetch_securities_hose()
    #     df_stock_list_x = fetch_securities_hnx()
    #     if not df_stock_list_h.empty:
    #         insert_stock_list(df_stock_list_h, conn)
    #         insert_stock_list(df_stock_list_x, conn)
    #     else:
    #         print("⚠️ No data fetched from API.")
    #     close_connection(conn)

    # conn = get_connection()
    # if conn:
    #     symbol="SSI"
    #     from_date = "15/08/2025"
    #     to_date = "20/08/2025"
    #
    #     #1 symbol
    #     # df_ohlc = fetch_data_ohlc_daily(symbol, from_date, to_date)
    #     # if not df_ohlc.empty:
    #     #     insert_ohlc_data(df_ohlc, conn)
    #     # else:
    #     #     print("⚠️ No OHLC data returned.")
    #
    #     #all symbol
    #     # symbol_list=['CII', 'VPB', 'VND',]
    #     #
    #     # for symbol in symbol_list:
    #     #     df_ohlc = fetch_data_ohlc_daily(symbol, from_date, to_date)
    #     #     if not df_ohlc.empty:
    #     #         insert_ohlc_data(df_ohlc, conn)
    #     #         print(f"Data {symbol} has been inserted ")
    #     # else:
    #     #     print("⚠️ No OHLC data returned.")
    #
    #     for symbol in get_all_symbols(conn):
    #         df_ohlc = fetch_data_ohlc_daily(symbol, from_date, to_date)
    #         if not df_ohlc.empty:
    #             insert_ohlc_data(df_ohlc, conn)
    #             print(f"Data {symbol} has been inserted ")
    #     else:
    #         print("⚠️ No OHLC data returned.")

        # close_connection(conn)

