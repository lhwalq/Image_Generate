#-*- coding:utf8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '林欢'
#    __Desc__ = logo图标
from PIL import Image, ImageFont, ImageDraw
import os

def ergodicStr(content):
    tempContent = ''
    for str in content.decode('utf-8'):
        tempContent = str if '' == tempContent else tempContent + '\n' + str
    return tempContent

# 获取即将生成的文件夹的名称
def getLogoCharacters():
    file = open(r'./modules/logo_characters.txt', 'rb')
    dirs = []
    for item in file.readlines():
        dirs.append(item.strip('\n').strip('\r'))
    file.close()
    return ergodicStr(dirs[0])

# 获取即将生成的文件夹的名称
def getdirs():
    file = open(r'./modules/logo.txt', 'rb')
    dirs = []
    for item in file.readlines():
        dirs.append(item.strip('\n').strip('\r'))
    file.close()
    return dirs

# 初始化操作，生成工作目录及图片生成目录
def init():
    dirs = getdirs()
    # generate logo and destination
    if not os.path.exists(r'./' + str('logo')):
        os.mkdir(r'./'+ str('logo'))
    if not os.path.exists(r'./' + str('modules')):
        os.mkdir(r'./' + str('modules'))
        os.open(r'./modules/logo.txt','wb')
    if not os.path.exists(r'./' + str('logo_destination')):
        os.mkdir(r'./' + str('logo_destination'))
        # generate folders
        for item in dirs:
            print item
            if not os.path.exists(r'./logo_destination/' + item):
                os.mkdir(r'./logo_destination/' + item)

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



def generate_images_by_image(sourcepath):
    # 获取生成图片所在的文件夹列表
    dirs = getdirs()

    # font = ImageFont.truetype('GB2312.ttf', 40)

    index = 0
    for item in dirs:
        width,height = item.split('x')
        print width
        image = Image.open(sourcepath)
        # originalWidth,originalHeight = image.size

        newname = r'./logo_destination/'+generate_new_name(sourcepath,dirs[index])
        print newname
        # draw = ImageDraw.Draw(image)
        # draw.text((int(originalWidth) / 2 - 20, int(originalHeight) / 2 - 55), getLogoCharacters(), (0, 0, 0), font=font)

        image.resize((int(width), int(height)), Image.ANTIALIAS).save(newname)
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
    generate_images__patchly(r'./logo/')