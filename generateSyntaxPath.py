import os
from pprint import pprint



# Input data
namiconventionA = """01KP_0080_ai_SRez_PreCompPrep_01_v001

            element

                        ai

                             png

                                   01KP_0080_ai_SRez_PreCompPrep_01_v001

                                                8192x8192

                                                           01KP_0080_ai_SRez_PreCompPrep_01_v001.%08d.png

                        reference

                                    01KP_0080_ai_SRez_PreCompPrep_01_v001.mp4

                        nuke

                                    01KP_0080_ai_SRez_PreCompPrep_01_v001.nk"""

namiconvention = """TSM_040_0095

     TSM_040_0095_mp01_roto_bot_v0001

                 TSM_040_0095_mp01_roto_bot_v0001.nk

                 TSM_040_0095_mp01_roto_bot_v0001

                             TSM_040_0095_mp01_roto_bot_v0001.####-####.exr"""




def is_folder(name):
    return not any(char in name for char in ['.', '%'])


def strip_line(namiconvention):
    return [line.strip() for line in namiconvention.splitlines() if line.strip()]

count = 1
filePathDict= {}
tempFolderList = []
for conventionName in strip_line(namiconvention):
    if is_folder(conventionName):
        tempFolderList.append(conventionName)
        # print(conventionName)
    else:
        ext_name = os.path.splitext(conventionName)[-1][1:]+"_file_path"
        filepath = "/".join(tempFolderList)+"/"+conventionName
        filePathDict.update({ext_name:filepath})


print(filePathDict)