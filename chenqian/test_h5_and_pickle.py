import os
import sys
import pandas as pd
import numpy as np
import pickle
import tables as ts



# hdf5
'''
# 详情请参考这个
https://pandas.pydata.org/pandas-docs/stable/reference/io.html#hdfstore-pyts-hdf5
'''

class h5_helper():

    def __init__(self,store_path):
        if os.path.exists(store_path):
            print('目标路径存在文件......')
        else:
            # 写入模式创新的数据集
            ts.open_file(store_path, mode="w")

        self.store_path = store_path

    def get_table(self,table_name):
        '''
        读全表的时候用这个方法,拿数据的都是get_node
        '''
        store_client = pd.HDFStore(self.store_path,mode='r+')
        # 这里还可以再包一些其他参数
        df = store_client.get(table_name)
        store_client.close()
        return df

    def select_table(self,table_name,where_str = None):
        '''
        获取table中的数据
        '''
        store_client = pd.HDFStore(self.store_path,mode='r+')
        # 这里还可以再包一些其他参数,读取尽量只用只读
        df = store_client.select(table_name,where=where_str)
        store_client.close()
        return df

    def append_table(self,df,table_name):
        '''
        根据以前的数据向里面追加额外数据,插入数据类型要跟原HDF对齐就有点难受
        tips:data_columns是必须填的参数而且必须是py的原生对象
        '''
        print('数据写入中...')
        store_client = pd.HDFStore(self.store_path,mode='a')
        # 这里可能还需要检查,因为新增部分的列名可能跟之前的不同,得先检查表的属性对上列名让后再追加数据
        df.to_hdf(self.store_path,table_name,
                format='table',
                mode='a',
                data_columns = df.columns.to_list(),
                append=True)
        store_client.close()
        print('数据写入完毕...')

    def remove_table(self,table_name):
        '''
        删除node
        '''
        store_client = pd.HDFStore(self.store_path,mode='w')
        store_client.remove(table_name)
        store_client.close()

    # def update_():
    #     ''''
    #     搞修改hdf不太支持SQL类的修改操作
    #     '''
    #     pass


# -------------------------- 测试读取和写入部分 -------------------------- #

# 数据量的多进程读取是否会因为store产生影响


store_path = 'temp.h5'
# write_mode = 'a'
# h5_client = h5_helper(store_path)


# store_client = pd.HDFStore(store_path,mode='r')
# store_client.close()

# 造假数据
B = pd.DataFrame(['2021-08-20', '000300.SH', '600547.SH', '有色金属', float(0.9999),float(0.99999999), float(9999)],
                index=['pdate', 'code', 'stock', 'industry', 'weight', 'return', 'rn'],
                columns=  [100086]).T
B[['weight', 'return']] = B[['weight', 'return',]].astype('float')
B['rn'] = B['rn'] .astype('int32')


A = pd.read_csv(r'chenqian\test_2_copy.csv',index_col='index')
# 造出虚拟数据

# A.to_hdf(r'chenqian'+'\\'+ store_path,'A',mode='w',append=True,data_columns = A.columns.to_list())

# store_client = pd.HDFStore(r'chenqian'+"\\"+'temp.h5')


F  = pd.read_hdf(r'chenqian'+"\\"+'temp.h5','A',where='''(
        (code=='000300.SH')&(rev <= 0.03)
        )''')
# where='''(
#     (code=='000300.SH')&(rev <= 0.03)
#     )''')

# hdf5_path = "test_data.hdf5"
# # 和普通文件操作类似，'w'、'r'、'a' 分别表示写数据、读数据、追加数据
# hdf5_file = ts.open_file(hdf5_path, mode='w')
# # 设定压缩级别和压缩方法
# filters = ts.Filters(complevel=5, complib='blosc')
# earray = hdf5_file.create_earray(
# 	hdf5_file.root,
# 	'data', # 数据名称，之后需要通过它来访问数据
# 	ts.Atom.from_dtype(A.dtypes), # 设定数据格式（和data1格式相同）
# 	shape=(0, 4096), # 第一维的 0 表示数据可沿行扩展
# 	filters=filters,
# 	expectedrows=1000000 # 完整数据大约规模，可以帮助程序提高时空利用效率
# )
# # 将 data1 添加进 earray
# earray.append(A)
# # 写完之后记得关闭文件
# hdf5_file.close()

#






# 追加行錯誤
'''
未解决
追加行
'''
# 测试新版本的append

