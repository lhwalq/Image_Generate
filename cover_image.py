#-*- coding:utf8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '林欢'
#    __Desc__ = 书的图片
from PIL import Image, ImageFont, ImageDraw
import os

# 获取即将生成的文件夹的名称
def getdirs():
    file = open(r'./modules/cover.txt', 'rb')
    dirs = []
    for item in file.readlines():
        dirs.append(item.strip('\n').strip('\r'))
    file.close()
    return dirs

# 初始化操作，生成工作目录及图片生成目录
def init():
    dirs = getdirs()
    # generate logo and destination
    if not os.path.exists(r'./' + str('cover')):
        os.mkdir(r'./'+ str('cover'))
    if not os.path.exists(r'./' + str('modules')):
        os.mkdir(r'./' + str('modules'))
        os.open(r'./modules/cover.txt','wb')
    if not os.path.exists(r'./' + str('cover_destination')):
        os.mkdir(r'./' + str('cover_destination'))
        # generate folders
        for item in dirs:
            print item
            content,height = item.split(',')
            if not os.path.exists(r'./cover_destination/' + content):
                os.mkdir(r'./cover_destination/' + content)

# 获取对应于cfg.txt文件夹下的分辨率比率
# def getpercent():
#     dirs = getdirs()
#     # file = open(r'./modules/percent.txt','wb')
#     percent = []
#     for item in dirs:
#         width,height = item.split('x')
#         percent.append(float(int(width)*int(height))/(192*192))
#     return percent


# 获得源图片的图片名称
def get_true_name(pathname):
    return pathname.split('/')[-1]


# 根据不同的适配方案，生成对应的图片文件名称
def generate_new_name(sourcepath,diritem):
   sourcename= sourcepath.split('/')[-1]
   prefix = sourcename.split('.')[0]
   affix = sourcename.split('.')[-1]
   return str(diritem)+str('/')+prefix+str('-')+str(diritem)+str('.')+affix

def ergodicStr(content):
    tempContent = ''
    for str in content.decode('utf-8'):
        tempContent = str if '' == tempContent else tempContent + '\n' + str
    return tempContent

def generate_images_by_image(sourcepath):
    # 获取生成图片所在的文件夹列表
    dirs = getdirs()

    font = ImageFont.truetype('GB2312.ttf', 20)

    index = 0
    for item in dirs:
        content,height = item.split(',')
        image = Image.open(sourcepath)

        newname = r'./cover_destination/'+generate_new_name(sourcepath,content)
        print newname
        draw = ImageDraw.Draw(image)
        draw.text((45 - 10, 60 - int(height)), ergodicStr(content), (0, 0, 0), font=font)

        image.resize((90, 120), Image.ANTIALIAS).save(newname)
        index +=1

def generate_images__patchly(sourcepath):
    source_images = os.listdir(sourcepath)
    for item in source_images:
        newname = sourcepath+item
        generate_images_by_image(newname)


if __name__=="__main__":
    # init()
    # logo = r'./logo/'
    # generate_images__patchly(logo)
    # user_input = sys.argv[1]
    # if user_input == "init":
    init()
    # elif user_input == "generate":
    generate_images__patchly(r'./cover/')