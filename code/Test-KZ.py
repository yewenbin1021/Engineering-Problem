import xlrd
import numpy as np
from sklearn.model_selection import KFold
from smt.surrogate_models import KRG
from smt.surrogate_models import QP
from smt.surrogate_models import RBF

def read_excel(path):
    workbook = xlrd.open_workbook(path)
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    excel = []
    for i in range(sheet1.nrows):
        rows = sheet1.row_values(i) 
        excel.append(rows)
    return excel
   
Input_path = 'Input.xlsx'
Output_path = 'Output.xlsx'
#inputs = read_excel(Input_path)
#inputs = np.array(inputs)
#outputs = read_excel(Output_path)
#outputs = np.array(outputs)
inputs = x
outputs = y


gerror = []
kf = KFold(n_splits=5)
for train_index, test_index in kf.split(outputs):
    x_train = inputs[train_index]
    y_train = outputs[train_index]
    x_test = inputs[test_index]
    y_test = outputs[test_index]
    

    sm = RBF(d0=5)
    sm.set_training_values(x_train, y_train)
    sm.train()
    
#    sm = KRG(theta0=[1e-2,1e-2,1e-2,1e-2,1e-2])
#    sm.set_training_values(x_train, y_train)
#    sm.train()
##
#    sm = QP()
#    sm.set_training_values(x_train, y_train)
#    sm.train()

#    num = 100
#    x = np.linspace(0, 4, num)
    y_pre = sm.predict_values(x_test)
    for i in range(len(y_pre)):
        ge = (y_pre[i]-y_test[i])/y_test[i]
        gerror.append(ge)
result = np.mean(np.abs(gerror))
result2 = np.abs(gerror)
print(y_pre)
print(result)

