# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 14:10:56 2024

@author: Administrator
"""

import pandas as pd 
import os 
file_path_1=[]
file_path_2=[]
file_path_list=[]
file_path=r'C:\Users\Administrator\Desktop\脑机接口\脑机接口数据'
for i in range(1,8):
    folder_path=os.path.join(file_path,f'S0{i:01}')
    print(f'当前文件夹路径：{folder_path}')
    if i <=3:
        num_files=3
    else:
        num_files=4
    person_file=[]
    for j in range (1,num_files+1):
        file_name=f'S0{i:01}-{j:01}.xlsx'
        full_file_path=os.path.join(folder_path,file_name)
        person_file.append(full_file_path)
        print(f'发现文件：{full_file_path}')
    try:
        person_data=pd.concat([pd.read_excel(file,header=None) for file in person_file],ignore_index=True)
        print(person_data)
        print(f'成功整合文件夹 S0{i:01}的数据')
    except Exception as e:
        print(f'整合文件夹 S0{i:01}的数据出错：{e}')
        continue #如果出错，跳过当前文件夹
    output_file=os.path.join(folder_path,f'S0{i:01}_data.xlsx')
    try:
        person_data.to_excel(output_file,index=False,engine='openpyxl')
        print(f'成功保存 S0{i:01}的数据到文件：{output_file}')
    except Exception as e:
        print(f'保存文件 S0{i:01}_data.xlsx时出错：{e}')
    
    
    
    