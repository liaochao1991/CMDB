from django.db import models

# Create your models here.
class Userinfo(models.Model):
    username = models.CharField(max_length=30,null=True,verbose_name="账户")
    password = models.CharField(max_length=30,null=True,verbose_name="密码")
    specialty = models.CharField(max_length=32, null=True,verbose_name="专业")
    cla_name = models.ManyToManyField(to='Class')
    def __str__(self):
        return self.username

class School(models.Model):
    #blank表示在django可以为空,verbose_name表示在django中的显示
    name = models.CharField(max_length=128,null=True,blank=True,verbose_name='名字')
    #URLField表示在会判断会不会是url,其他形式的也一样其实功能跟上面的一样
    address = models.URLField(max_length=128,null=True,blank=True,verbose_name='地址')
    email = models.EmailField(max_length=128,null=True,blank=True,verbose_name='邮箱')
   # true_false = models.BooleanField(max_length=32,null=True,blank=True,verbose_name='是否')
    date = models.DateField(verbose_name='时间',null=True)
    # 对应下面的班级表，一对多，可以理解为一个学校可以有多个班级,1对多
    cla =models.ForeignKey(to='Class',default=1)
    def __str__(self):
        return self.name

class Number(models.Model):
    #学号可以11对应，1对1
    num = models.OneToOneField(to='Userinfo',verbose_name='学号')
    def __str__(self):
        return self.num

#定义班级
class Class(models.Model):
    #id
    sch=models.ForeignKey(to="School",default=1) #cla_id
    name = models.CharField(max_length=128, null=True, blank=True, verbose_name='名字')
    #多个班级多个用户，多对多的关系
    user = models.ManyToManyField(to='Userinfo')
    def __str__(self):
        return self.name

class Disk(models.Model):
    '''磁盘'''
    path = models.CharField(max_length=64, blank=True, null=True, verbose_name='挂载路径')
    size = models.CharField(max_length=16, blank=True, null=True, verbose_name='磁盘大小/G')
    remarks = models.CharField(max_length=2048, blank=True, null=True, verbose_name='备注')
    def __str__(self):
        return self.size
    class Meta:
        verbose_name_plural = "磁盘"
class Region(models.Model):
    name = models.CharField(max_length=64,blank=True,null=True,verbose_name='区域')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "区域表"

class Host(models.Model):    # 最基础的主机表
    '''主机,阿里云eth0 内网网卡， eth1 公网网卡'''
    hostname = models.CharField(max_length=64, blank=True, null=True, verbose_name='主机名')
    ecsname = models.CharField(max_length=64, blank=True, null=True, verbose_name='实例名')
    login_port = models.CharField(max_length=16, default='22', blank=True, null=True, verbose_name='登录端口')
    cpu = models.CharField(max_length=8, blank=True, null=True, verbose_name='CPU')
    mem = models.CharField(max_length=8, blank=True, null=True, verbose_name='内存')
    speed = models.CharField(max_length=8, blank=True, default='5', null=True, verbose_name='带宽')
    eth1_network = models.CharField(max_length=32, blank=True, null=True, verbose_name='公网IP')
    eth0_network = models.CharField(max_length=32, verbose_name='私网IP')
    sn = models.CharField(max_length=64, blank=True, null=True, verbose_name='SN')
    kernel = models.CharField(max_length=64, blank=True, null=True, verbose_name='内核版本')  # 内核+版本号
    remarks = models.CharField(max_length=2048, blank=True, null=True, verbose_name='备注')
    createtime = models.CharField(max_length=32, blank=True, null=True, verbose_name='创建时间')
    expirytime = models.CharField(max_length=32, blank=True, null=True, verbose_name='到期时间')
    #os = models.CharField(max_length=32, blank=True, null=True, verbose_name='操作系统')
    #ForeignKey
    #lab = models.ForeignKey(to='Lable',default=1,blank=True, null=True, verbose_name='标签')
    #os = models.ForeignKey(to='Os',default=1,blank=True, null=True, verbose_name='操作系统')  # os+版本号
    source = models.ForeignKey(to='Source',default=1,blank=True, null=True, verbose_name='来源IP')
    region = models.ForeignKey(to='Region',default=1,blank=True, null=True, verbose_name='地域')

    #  ManyToManyField
    logining = models.ManyToManyField(to='Login',default=1,  verbose_name='所属用户')
    disks = models.ManyToManyField(to='Disk',default=1,  verbose_name='磁盘')

    #这个字段只运行再内存里。这些信息不占磁盘的信息。
    state_choices = (
        (1, 'Running'),
        (2, '下线'),
        (3, '关机'),
        (4, '删除'),
        (5, '故障'),
    )
    state = models.SmallIntegerField(verbose_name='主机状态', choices=state_choices, blank=True, null=True, )

    def __str__(self):
        return self.hostname


    class Meta:
        verbose_name_plural = "主机表"

class Login(models.Model):
    '''登录相关'''
    login_name = models.CharField(max_length=16, default='root', verbose_name='登录用户名')
    login_pwd= models.CharField(max_length=64, blank=True, null=True, verbose_name='登录密码')
    auth=models.CharField(max_length=8,blank=True, null=True, verbose_name='具有权限')
    def __str__(self):
        return self.login_name
    class Meta:
        verbose_name_plural = "主机用户表"


class Source(models.Model):
    '''来源：阿里云、物理机（某机房等）'''
    name = models.CharField(max_length=16, blank=True, null=True, verbose_name='来源')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "主机来源表"