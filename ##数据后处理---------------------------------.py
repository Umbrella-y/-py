##数据后处理---------------------------------##
import pandas as pd
import os 
import warnings
import re
import shutil
warnings.filterwarnings("ignore")#忽略所有的警告，继续执行，主要是为了屏蔽pd.append要换为pd.concat的警告

def movefile(orifile,tardir):
    if os.path.isfile(orifile):#用于判断某一对象(需提供绝对路径)是否为文件
        shutil.copy(orifile, tardir)#shutil.copy函数放入原文件的路径文件全名  然后放入目标文件夹



filepath = r'E:\30nm实验数据汇总\2022.11.18.duoKjisuan\py后处理/'
print('cd {}'.format(filepath))
os.chdir('{}'.format(filepath))
os.system('mkdir jisuan total bash')
files = os.listdir(filepath)
for file in files:
    if re.findall(r'jisuan',file) and re.findall(r'转制',file):
        orifile = filepath + '/' + file
        dirfile = filepath +'/' + 'jisuan' +'/'
        movefile(orifile,dirfile)
    elif re.findall(r'total',file) and re.findall(r'转制',file):
        orifile = filepath + '/' + file
        dirfile = filepath +'/' + 'total' +'/'
        movefile(orifile,dirfile)
    else:
        orifile = filepath + '/' + file
        dirfile = filepath +'/' + 'bash' +'/'
        movefile(orifile,dirfile)
        bash = re.findall(r'/d+',file)
        print(bash)

#-----------------------------------文件分类完成---------------------##
#-----------------------------------Phase 1-------------------------##
os.chdir('jisuan')
data = pd.DataFrame()
files = os.listdir()
files.sort(key=lambda x:int(re.findall('\d+',x)[0]))
for file in files:
    df =pd.DataFrame()
    K = re.findall('\d+',file)[0]
    file = filepath + '/' + file
    df = pd.read_csv(file, skiprows=1)
    describe = df.describe(include='all')
    T_describe = pd.DataFrame(describe.values.T,index = describe.columns,columns=describe.index)
    #T_describe.to_csv(file+'后处理.csv')
    data['MeanK={}'.format(str(K))] = T_describe.loc[:,'mean']
    data['StdEK={}'.format(str(K))] = T_describe.loc[:,'std']
    print(data)
    os.chdir('{}'.format(filepath))
    data.to_csv('计算区域温度.csv')
#-----------------------------------Phase 2-------------------------##

os.chdir('total')
data = pd.DataFrame()
files = os.listdir()
files.sort(key=lambda x:int(re.findall('\d+',x)[0]))
for file in files:
    df =pd.DataFrame()
    K = re.findall('\d+',file)[0]
    file = filepath + '/' + file
    df = pd.read_csv(file, skiprows=1)
    describe = df.describe(include='all')
    T_describe = pd.DataFrame(describe.values.T,index = describe.columns,columns=describe.index)
    #T_describe.to_csv(file+'后处理.csv')
    data['MeanK={}'.format(str(K))] = T_describe.loc[:,'mean']
    data['StdEK={}'.format(str(K))] = T_describe.loc[:,'std']
    print(data)
    os.chdir('{}'.format(filepath))
    data.to_csv('全部区域温度.csv')
#-----------------------------------Phase 3-------------------------##