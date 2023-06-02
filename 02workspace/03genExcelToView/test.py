import os
from datetime import datetime


outputPath = ".\\02workspace\\03genExcelToView\\Output"
nowTime = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
newFolderName = os.path.join(outputPath, nowTime)

EXCELPATH = fr"{newFolderName}\test1.xlsx"
print(EXCELPATH)

# os.makedirs(fr'{newFolderName}')
# os.startfile(fr'{newFolderName}')