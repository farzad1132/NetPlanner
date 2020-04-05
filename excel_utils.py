import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from Common_Object_def import Network

def export_excel(filename, network):
    """
    filename: example.xlsx
    NOTE: if filename is open executing this function will cause an error
    network: an instance of Common_Object_def
    """
    sources = []
    destinations = []
    wavelengths = []
    routed_types = []
    worst_working_snrs = []
    worst_protection_snrs = []
    working_path = []
    protection_path = []
    working_regens = []
    protection_regens = []
    # Building required lists for different fields
    for lightpath in network.LightPathDict.values():
        sources.append(lightpath.Source)
        destinations.append(lightpath.Destination)
        wavelengths.append(lightpath.WaveLength[0])
        routed_types.append(lightpath.Type)

        snr = lightpath.SNR_w[0]
        for snr_temp in lightpath.SNR_w:
          if snr>snr_temp:
            snr = snr_temp
        worst_working_snrs.append(snr)

        snr = lightpath.SNR_p[0]
        for snr_temp in lightpath.SNR_p:
          if snr>snr_temp:
            snr = snr_temp
        worst_protection_snrs.append(snr)

        working_path.append(lightpath.WorkingPath)
        protection_path.append(lightpath.ProtectionPath)
        working_regens.append(lightpath.RegeneratorNode_w)
        protection_regens.append(lightpath.RegeneratorNode_p)

    dictionary = {
    'Source Site' : sources,
    'Destination Site' : destinations,
    'Demand Type': routed_types,
    'Wavelength': wavelengths,
    'Working SNR': worst_working_snrs,
    'Protection SNR': worst_protection_snrs,
    'Working Path': working_path,
    'Working Regenerators': working_regens,
    'Protection Path': protection_path,
    'Protection Regenerators': protection_regens}

    df = pd.DataFrame(dictionary)
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Routed Demands')
    workbook  = writer.book
    worksheet = writer.sheets['Routed Demands']
    # Set column size (begininng, end, size)
    worksheet.set_column(1, 2 , 17)
    worksheet.set_column(3, 4 , 15)
    worksheet.set_column(5, 6, 17)
    worksheet.set_column(7, 7, 40)
    worksheet.set_column(8, 8, 20)
    worksheet.set_column(9, 9, 45)
    worksheet.set_column(10, 10, 20)

    # 3-color formatting for snrs
    lightpath_number = len(network.LightPathDict.keys())
    worksheet.conditional_format('F2:F' + str(lightpath_number+1), {'type': '3_color_scale'})
    worksheet.conditional_format('G2:G' + str(lightpath_number+1), {'type': '3_color_scale'})
    
    # Set example specific text and color for some headers
    color = "#FFC000"
    fmt = workbook.add_format()
    fmt = workbook.add_format({'bg_color': color})
    worksheet.write('B1', 'Source Site', fmt)
    worksheet.write('C1', 'Destination Site', fmt)
    
    color = "#FFFF64"
    fmt = workbook.add_format()
    fmt = workbook.add_format({'bg_color': color})
    worksheet.write('H1', 'Working Path', fmt)
    
    color = "#64FF00"
    fmt = workbook.add_format()
    fmt = workbook.add_format({'bg_color': color})
    worksheet.write('E1', 'Wavelength', fmt)
    writer.save()