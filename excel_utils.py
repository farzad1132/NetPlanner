import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from Common_Object_def import Network

def export_excel(filename, network, IdNodeMap, cluster_view = True):
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
    unprotected_indices = []
    # Building required lists for different fields
    for lightpath in network.LightPathDict.values():
        sources.append(IdNodeMap[lightpath.Source])
        destinations.append(IdNodeMap[lightpath.Destination])
        wavelengths.append(lightpath.WaveLength)
        routed_types.append(lightpath.Type)

        working_path.append(list(map(lambda x: IdNodeMap[x], lightpath.WorkingPath)))
        working_regens.append(list(map(lambda x : IdNodeMap[x], lightpath.RegeneratorNode_w)))
        snr = lightpath.SNR_w[0]
        for snr_temp in lightpath.SNR_w:
            if snr>snr_temp:
                snr = snr_temp
        worst_working_snrs.append(snr)
        try:
            snr = lightpath.SNR_p[0]
            for snr_temp in lightpath.SNR_p:
                if snr>snr_temp:
                    snr = snr_temp
            worst_protection_snrs.append(snr)
            protection_path.append(list(map(lambda x: IdNodeMap[x], lightpath.ProtectionPath)))
            protection_regens.append(list(map(lambda x : IdNodeMap[x], lightpath.RegeneratorNode_p)))
        except:
            worst_protection_snrs.append(None)
            protection_path.append([])
            protection_regens.append([])
            unprotected_indices.append(len(worst_protection_snrs))

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
    center_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
    snr_format = workbook.add_format({'num_format': '0.00', 'align': 'center'})
    worksheet.set_column(1, 2 , 17,center_format)
    worksheet.set_column(3, 4 , 15,center_format)
    worksheet.set_column(5, 6, 17,snr_format)
    worksheet.set_column(7, 7, 40)
    worksheet.set_column(8, 8, 20)
    worksheet.set_column(9, 9, 45)
    worksheet.set_column(10, 10, 20)

    for index in unprotected_indices:
        color = "#D1D1D1"
        fmt = workbook.add_format()
        fmt = workbook.add_format({'bg_color': color})
        worksheet.set_row(index, cell_format = fmt)
        fmt = workbook.add_format()
        fmt = workbook.add_format({'align': 'center', 'bg_color': color})
        worksheet.write('B'+str(index+1), dictionary['Source Site'][index-1], fmt)
        worksheet.write('C'+str(index+1), dictionary['Destination Site'][index-1], fmt)
        worksheet.write('D'+str(index+1), dictionary['Demand Type'][index-1], fmt)
        worksheet.write('E'+str(index+1), dictionary['Wavelength'][index-1], fmt)
      
    # 3-color formatting for snrs
    lightpath_number = len(network.LightPathDict.keys())
    worksheet.conditional_format('F2:F' + str(lightpath_number+1), {'type': '3_color_scale'})
    worksheet.conditional_format('G2:G' + str(lightpath_number+1), {'type': '3_color_scale'})
    
    # Set example specific text and color for some headers
    color = "#FFC000"
    fmt = workbook.add_format()
    fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
    worksheet.write('B1', 'Source Site', fmt)
    worksheet.write('C1', 'Destination Site', fmt)
    
    color = "#FFFF64"
    fmt = workbook.add_format()
    fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
    worksheet.write('H1', 'Working Path', fmt)
    
    color = "#64FF00"
    fmt = workbook.add_format()
    fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
    worksheet.write('E1', 'Wavelength', fmt)

    #### Link Stats #######
    wavelength_number_on_links = []
    all_link_states = []
    for link in list(network.PhysicalTopology.LinkDict.keys()):
        wavelength_number_on_links.append(len(network.PhysicalTopology.LinkDict[link].LinkState))
        all_link_states.append(network.PhysicalTopology.LinkDict[link].LinkState)
    dictionary2 = {
    'Links' : list(map(lambda x : (IdNodeMap[x[0]], IdNodeMap[x[1]]), list(network.PhysicalTopology.LinkDict.keys()))),
    'Used Wavelengths' : all_link_states,
    'Wavelength Number': wavelength_number_on_links
    }
    link_number = len(list(network.PhysicalTopology.LinkDict.keys()))
    df2 = pd.DataFrame(dictionary2)
    df2.to_excel(writer, sheet_name='Link State')
    worksheet2 = writer.sheets['Link State']
    worksheet2.conditional_format('D2:D'+ str(link_number+1),  {'type': '3_color_scale',
                                         'min_color': "green",
                                         'mid_color': "yellow",
                                         'max_color': "red"})
    worksheet2.set_column(1, 1 , 12,center_format)
    worksheet2.set_column(2, 2, 52)
    worksheet2.set_column(3, 3, 18,center_format)

    #### Node Stats #######
    wavelength_number_on_nodes = []
    all_node_states = []
    for node in list(network.PhysicalTopology.NodeDict.keys()):
        wavelength_number_on_nodes.append(len(network.PhysicalTopology.NodeDict[node].NodeState))
        all_node_states.append(network.PhysicalTopology.NodeDict[node].NodeState)
    dictionary3 = {
    'Nodes' : list(map(lambda x : IdNodeMap[x], list(network.PhysicalTopology.NodeDict.keys()))),
    'Used Wavelengths' : all_node_states,
    'Wavelength Number': wavelength_number_on_nodes
    }
    node_number = len(list(network.PhysicalTopology.NodeDict.keys()))
    df3 = pd.DataFrame(dictionary3)
    df3.to_excel(writer, sheet_name='Node State')
    worksheet3 = writer.sheets['Node State']
    worksheet3.conditional_format('D2:D'+ str(node_number+1),  {'type': '3_color_scale',
                                         'min_color': "green",
                                         'mid_color': "yellow",
                                         'max_color': "red"})
    worksheet3.set_column(1, 1 , 12,center_format)
    worksheet3.set_column(2, 2, 52)
    worksheet3.set_column(3, 3, 18,center_format)
    
    # Restorations
    
    sources = []
    destinations = []
    wavelengths = []
    routed_types = []
    worst_working_snrs = []
    worst_protection_snrs = []
    working_path = []
    working_regens = []
    unprotected_indices = []
    unrestored_indices = []
    restored_indices = []
    failed_links = []
    second_failed_links = []
    protection_path = []
    need_restoration_sheet = False
    # Building required lists for different fields
    for lightpath in network.LightPathDict.values():
        if lightpath.restorationType is not None:
            need_restoration_sheet = True
            sources.append(IdNodeMap[lightpath.Source])
            destinations.append(IdNodeMap[lightpath.Destination])
            wavelengths.append(lightpath.WaveLength)
            routed_types.append(lightpath.Type)
            failed_links.append('-')
            second_failed_links.append('-')

            working_path.append(list(map(lambda x: IdNodeMap[x], lightpath.WorkingPath)))
            working_regens.append(list(map(lambda x : IdNodeMap[x], lightpath.RegeneratorNode_w)))
            snr = lightpath.SNR_w[0]
            for snr_temp in lightpath.SNR_w:
                if snr>snr_temp:
                    snr = snr_temp
            worst_working_snrs.append(snr)
            try:
                snr = lightpath.SNR_p[0]
                protection_path.append(list(map(lambda x: IdNodeMap[x], lightpath.ProtectionPath)))
            except:
                protection_path.append([])
                unprotected_indices.append(len(protection_path))

            if lightpath.restorationPathList:
                restored_indices.append(len(worst_working_snrs))
                for restoration_id, restoration_option in enumerate(lightpath.restorationPathList):
                    if restoration_option is None:
                        pass
                    elif any(isinstance(restoration_option[i], list) for i in range(len(restoration_option))):
                        for second_id, second_restoration in enumerate(restoration_option):
                            if second_restoration is not None:
                                sources.append(IdNodeMap[lightpath.Source])
                                destinations.append(IdNodeMap[lightpath.Destination])
                                wavelengths.append(lightpath.WaveLength)
                                routed_types.append(f"R {lightpath.Type}")
                                fail1 = [lightpath.restorationFailedLinks[restoration_id][second_id][0],
                                        lightpath.restorationFailedLinks[restoration_id][second_id][1]]
                                fail2 = [lightpath.restorationFailedLinks[restoration_id][second_id][2],
                                        lightpath.restorationFailedLinks[restoration_id][second_id][3]]
                                failed_links.append([IdNodeMap[fail1[0]], IdNodeMap[fail1[1]]])
                                second_failed_links.append([IdNodeMap[fail2[0]], IdNodeMap[fail2[1]]])

                                working_path.append(second_restoration)
                                working_regens.append(lightpath.restorationPathRegenerators[restoration_id][second_id])
                                worst_working_snrs.append(lightpath.restorationSNRs[restoration_id][second_id])
                                protection_path.append('-')
                    else:
                        sources.append(IdNodeMap[lightpath.Source])
                        destinations.append(IdNodeMap[lightpath.Destination])
                        wavelengths.append(lightpath.WaveLength)
                        routed_types.append(f"R {lightpath.Type}")
                        failed_links.append([IdNodeMap[lightpath.restorationFailedLinks[restoration_id][0]], IdNodeMap[lightpath.restorationFailedLinks[restoration_id][1]]])
                        second_failed_links.append('all')

                        working_path.append(restoration_option)
                        working_regens.append(list(map(lambda x : IdNodeMap[x], lightpath.restorationPathRegenerators[restoration_id])))
                        worst_working_snrs.append(lightpath.restorationSNRs[restoration_id])
                        protection_path.append('-')
            else:
                unrestored_indices.append(len(worst_working_snrs))

    dictionary = {
    'Source Site' : sources,
    'Destination Site' : destinations,
    'Demand Type': routed_types,
    'Working Failed Link': failed_links,
    'Protection Failed Link': second_failed_links,
    'Wavelength': wavelengths,
    'Path': working_path,
    'Regenerators': working_regens,
    'SNR': worst_working_snrs,
    'Protection Path': protection_path}

    if need_restoration_sheet:
        df4 = pd.DataFrame(dictionary)
        df4.to_excel(writer, sheet_name='Restoration')
        workbook  = writer.book
        worksheet4 = writer.sheets['Restoration']

        

        # Set column size (begininng, end, size)
        center_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
        snr_format = workbook.add_format({'num_format': '0.00', 'align': 'center'})
        worksheet4.set_column(1, 2 , 17,center_format)
        worksheet4.set_column(3, 3 , 15,center_format)
        worksheet4.set_column(4, 5 , 25,center_format)
        worksheet4.set_column(6, 6 , 15,center_format)
        worksheet4.set_column(7, 7, 50)
        worksheet4.set_column(8, 8, 20)
        worksheet4.set_column(9, 9, 17,snr_format)
        worksheet4.set_column(10, 10, 45)

        # for index in unprotected_indices:
        #     color = "#D1D1D1"
        #     fmt = workbook.add_format()
        #     fmt = workbook.add_format({'bg_color': color})
        #     worksheet4.set_row(index, cell_format = fmt)
        #     fmt = workbook.add_format()
        #     fmt = workbook.add_format({'align': 'center', 'bg_color': color})
        #     worksheet4.write('B'+str(index+1), dictionary['Source Site'][index-1], fmt)
        #     worksheet4.write('C'+str(index+1), dictionary['Destination Site'][index-1], fmt)
        #     worksheet4.write('D'+str(index+1), dictionary['Demand Type'][index-1], fmt)
        #     # worksheet4.write('E'+str(index+1), dictionary['Wavelength'][index-1], fmt)

        for index in unrestored_indices:
            color = "#FCDADD"
            fmt = workbook.add_format()
            fmt = workbook.add_format({'bg_color': color})
            worksheet4.set_row(index, cell_format = fmt)
            fmt = workbook.add_format()
            fmt = workbook.add_format({'align': 'center', 'bg_color': color})
            worksheet4.write('B'+str(index+1), dictionary['Source Site'][index-1], fmt)
            worksheet4.write('C'+str(index+1), dictionary['Destination Site'][index-1], fmt)
            worksheet4.write('D'+str(index+1), dictionary['Demand Type'][index-1], fmt)
            worksheet4.write('E'+str(index+1), dictionary['Working Failed Link'][index-1], fmt)
            worksheet4.write('F'+str(index+1), dictionary['Protection Failed Link'][index-1], fmt)
            worksheet4.write('G'+str(index+1), dictionary['Wavelength'][index-1], fmt)
            worksheet4.write('J'+str(index+1), dictionary['SNR'][index-1], snr_format)

        for index in restored_indices:
            color = "#DCFEE3"
            fmt = workbook.add_format()
            fmt = workbook.add_format({'bg_color': color})
            worksheet4.set_row(index, cell_format = fmt)
            fmt = workbook.add_format()
            fmt = workbook.add_format({'align': 'center', 'bg_color': color})
            worksheet4.write('B'+str(index+1), dictionary['Source Site'][index-1], fmt)
            worksheet4.write('C'+str(index+1), dictionary['Destination Site'][index-1], fmt)
            worksheet4.write('D'+str(index+1), dictionary['Demand Type'][index-1], fmt)
            worksheet4.write('E'+str(index+1), dictionary['Working Failed Link'][index-1], fmt)
            worksheet4.write('F'+str(index+1), dictionary['Protection Failed Link'][index-1], fmt)
            worksheet4.write('G'+str(index+1), dictionary['Wavelength'][index-1], fmt)
            worksheet4.write('J'+str(index+1), dictionary['SNR'][index-1], snr_format)

        
        # 3-color formatting for snrs
        lightpath_number = len(network.LightPathDict.keys())
        # worksheet4.conditional_format('F2:F' + str(lightpath_number+1), {'type': '3_color_scale'})
        worksheet4.conditional_format('J2:J' + str(lightpath_number+1), {'type': '3_color_scale'})
        
        # Set example specific text and color for some headers
        color = "#FFC000"
        fmt = workbook.add_format()
        fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
        worksheet4.write('B1', 'Source Site', fmt)
        worksheet4.write('C1', 'Destination Site', fmt)
        
        color = "#FFFF64"
        fmt = workbook.add_format()
        fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
        worksheet4.write('H1', 'Restoration Path', fmt)
        
        color = "#64FF00"
        fmt = workbook.add_format()
        fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
        worksheet4.write('J1', 'SNR', fmt)
    #################################################

    if cluster_view:
        for cluster_id in network.PhysicalTopology.ClusterDict.keys():
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
                if lightpath.ClusterNum == int(cluster_id):
                    sources.append(IdNodeMap[lightpath.Source])
                    destinations.append(IdNodeMap[lightpath.Destination])
                    wavelengths.append(lightpath.WaveLength[0])
                    routed_types.append(lightpath.Type)

                    working_path.append(list(map(lambda x: IdNodeMap[x], lightpath.WorkingPath)))
                    working_regens.append(lightpath.RegeneratorNode_w)
                    snr = lightpath.SNR_w[0]
                for snr_temp in lightpath.SNR_w:
                    if snr>snr_temp:
                        snr = snr_temp
                worst_working_snrs.append(snr)
                try:
                    snr = lightpath.SNR_p[0]
                    for snr_temp in lightpath.SNR_p:
                        if snr>snr_temp:
                            snr = snr_temp
                    worst_protection_snrs.append(snr)
                    protection_path.append(list(map(lambda x: IdNodeMap[x], lightpath.ProtectionPath)))
                    protection_regens.append(lightpath.RegeneratorNode_p)
                except:
                    worst_protection_snrs.append([])
                    protection_path.append([])
                    protection_regens.append([])
            if sources:
                dictionary4 = {
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

                df4 = pd.DataFrame(dictionary4)
                df4.to_excel(writer, sheet_name='Cluster '+str(cluster_id))
                worksheet = writer.sheets['Cluster '+str(cluster_id)]
                # Set column size (begininng, end, size)
                center_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
                snr_format = workbook.add_format({'num_format': '0.00', 'align': 'center'})
                worksheet.set_column(1, 2 , 17,center_format)
                worksheet.set_column(3, 4 , 15,center_format)
                worksheet.set_column(5, 6, 17,snr_format)
                worksheet.set_column(7, 7, 40)
                worksheet.set_column(8, 8, 20)
                worksheet.set_column(9, 9, 45)
                worksheet.set_column(10, 10, 20)

                # 3-color formatting for snrs
                lightpath_number = len(sources)
                worksheet.conditional_format('F2:F' + str(lightpath_number+1), {'type': '3_color_scale'})
                worksheet.conditional_format('G2:G' + str(lightpath_number+1), {'type': '3_color_scale'})
                
                # Set example specific text and color for some headers
                color = "#FFC000"
                fmt = workbook.add_format()
                fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
                worksheet.write('B1', 'Source Site', fmt)
                worksheet.write('C1', 'Destination Site', fmt)
                
                color = "#FFFF64"
                fmt = workbook.add_format()
                fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
                worksheet.write('H1', 'Working Path', fmt)
                
                color = "#64FF00"
                fmt = workbook.add_format()
                fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
                worksheet.write('E1', 'Wavelength', fmt)

    writer.save()
    writer.close()

