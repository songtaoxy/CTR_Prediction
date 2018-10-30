import os
import time

# 接口列表
from arrow import formatter


# 生成文件所在目录
dir_js = './hi-js/src/js/cases/bdhijs/'
dir_runner = './hi-js/src/js/runner/'
dir_html = './hi-js/src/hmtl/'

def folder_detect(folder_name):
    if not (os.path.exists(folder_name)):
        os.makedirs(folder_name)
        print('makedir:', folder_name)


# 检测文件是否存在
# falg=w, 如果不存在, 则新建该文件. 该功能主要是批量建立新文件
# flag=r, 如果不存在, 则保存, 提醒 手动新建该文件. 主要功能:将配置中的注释信息写到上面批量新建的文件中.
def file_detect(file_name, flag):
    if not (os.path.exists(file_name)):
        # with open(file_name,'w') as file_new:
        #     file_new.write('zhangyunjing')
        if (flag == 'w'):
            f = open(file_name, 'w')
            f.close()
        elif (flag == 'r'):
            print("文件不存在, 需要建立")






'''
模块的名字
'''
module_00_name = "../00_test"
module_01_name = '../../01_tensorflow_aanconda_install'
module_02_name = '../../02_tensorflow_usage'
module_03_name = '../../03_神经网络_简单分类_mnist_data'
module_04_name = '../../004_神经网络_交叉熵_优化器_dropout'

module_09_name = '../../09_objectdetection'
module_09_02_name = '../../09_object_detection_homewor'

module_08_name = '../../08_densenet_homework'
module_07_name = '../../07_cnn_homework'
module_06_name = '../../06_tensorflow_usage_homework'

module_05_name = '../../../python3_usage'

module_04_name = '../../ctr_prediction'

root_out = '/output'
sets_ffm = '/output/ffm/set'
field2count_ffm = '/output/ffm/field2count'
dict_ffm = '/output/ffm/dict'


sets_fm = '/output/fm/set'
field2count_fm = '/output/fm/field2count'
dict_fm = '/output/fm/dict'



sets_deep_fm = '/output/deepfm/set'
field2count_deep_fm = '/output/deepfm/field2count'
dict_deep_fm = '/output/deepfm/dict'


'''
模块下面的dir
'''
dir_dic = {
    'archived': 'archived',
    'modules': 'modules',
    'out': 'out',
    'model': 'out/model',
    'log': 'out/log',
    'ref_doc': 'ref_doc',
    'resources': 'resources',
    'src': 'src',
    'datasets': 'datasets',
    'train': 'datasets/train',
    'test': 'datasets/test',
    'raw': 'datasets/raw',

}

dir_dic_tinymind={

    'root_out': '/output',
    'sets_ffm': '/output/ffm/sets',
    'field2count_ffm': '/output/ffm/field2count',
    'dict_ffm': '/output/ffm/dict',
    'sets_fm': '/output/fm/sets',
    'field2count_fm': '/output/fm/field2count',
    'dict_fm': '/output/fm/dict',
    'sets_deep_fm': '/output/deepfm/sets',
    'field2count_deep_fm': '/output/deepfm/field2count',
    'dict_deep_fm': '/output/deepfm/dict'


}

def create_folder_local():
    keys = dir_dic.keys()
    for key in keys:
        # dir_name = module_01_name+os.sep+dir_dic[key]
        # dir_name = module_02_name+os.sep+dir_dic[key]
        # dir_name = module_03_name+os.sep+dir_dic[key]
        # dir_name = module_09_name + os.sep + dir_dic[key]
        # dir_name = module_08_name + os.sep + dir_dic[key]
        # dir_name = module_07_name + os.sep + dir_dic[key]
        # dir_name = module_06_name + os.sep + dir_dic[key]
        #dir_name = module_04_name + os.sep + dir_dic[key]
        dir_name = module_09_02_name+ os.sep + dir_dic[key]
        folder_detect(dir_name)
        
        
def create_folder_tinymind():
    keys = dir_dic_tinymind.keys()
    for key in keys:
        dir_name = dir_dic_tinymind[key]
        folder_detect(dir_name)

def create_folder_judge(flag):
    if flag=='local':
        create_folder_local()
    elif flag == 'tinymind':
        create_folder_tinymind()
        


