from PIL import Image,ImageFont,ImageDraw  #需要安装pillow，从PIL库导入所需模块

headpath = r"F:\\images\\"#头像图片路径，需要\转译

outpath =  r"F:\\images\\"#输出图片路径，需要\转译

fontpath = r"C:\\Windows\\Fonts\\"#字体文件路径

headfile = "head.jpg" #图片名称

outfile = "output.jpg"#输出图片名称

image = Image.open(headpath+headfile, 'r')

draw = ImageDraw.Draw(image)

fontsize = min(image.size)/4

fontobj=ImageFont.truetype(font=fontpath+"AdobeDevanagari.otf",size=fontsize,index=0,encoding='')#实例字体对象

draw.text((image.size[0]-fontsize,0),text='5',fill=(255,0,0),font=fontobj,anchor=None)#用draw对象的text()方法添加文字

image.save(outpath+outfile)#保存图片