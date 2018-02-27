from PIL import Image,ImageFont,ImageDraw,ImageColor  #需要安装pillow，从PIL库导入所需模块

headpath = r"F:\\images\\"  # 头像图片路径，需要\转译

outpath = r"F:\\images\\"  # 输出图片路径，需要\转译

fontpath = r"C:\\Windows\\Fonts\\"  # 字体文件路径

headfile = "head.jpg"  # 图片名称

outfile = "output.jpg"  # 输出图片名称


def add_num(img):

    w, h = image.size #获取图片对象宽和高

    fillcolor = ImageColor.colormap.get('white')#定义填充颜色

    draw = ImageDraw.Draw(image)#实例化draw对象

    fontsize = min(image.size)/4
    #字体大小按图片宽、高中最小的1/4设置

    draw.pieslice([(w / 3 * 2, 0), (w, h / 3)], 0, 360, fill="red")
    # 绘制圆形，第一个参数界定绘制区域，我选择了宽高为原图1/3的右上角区域

    fontobj=ImageFont.truetype(font=fontpath+'simsunb.ttf', size=int(fontsize))
    #实例字体对象，size应转换为int类型，否则是float

    draw.text((w*0.78, h*0.03), text='1', fill=fillcolor, font=fontobj, anchor=None)
    #用draw对象的text()方法添加文字，第一个参数是坐标，第二个参数是文本绘制内容，第三个是字体对象

    image.save(outpath+outfile)#保存图片


if __name__ == '__main__':

    image = Image.open(headpath + headfile, 'r')

    add_num(image)

    image.close()