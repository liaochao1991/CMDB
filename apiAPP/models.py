from django.db import models

# Create your models here.

'''
    权限设计
'''
class Userinfo(models.Model):
    '''人员'''
    username = models.CharField(max_length=32,blank=True,null=True,verbose_name="登录用户名")
    password = models.CharField(max_length=128,blank=True,null=True,verbose_name="密码")
    department = models.CharField(max_length=32,blank=True,null=True,verbose_name="所属部门")
    #一个岗位对应多个用户，一对多，foreignkey 的 放在 对多的表里
    pos = models.ForeignKey(to='Position',blank=True,null=True,verbose_name="职位",related_name='uspos')

    def __str__(self):
        '''
          打印request返回的值
        :return:
        '''
        return self.username
    class Meta:
        '''显示表名用的'''
        verbose_name_plural = "用户表"

class Position(models.Model):
    '''职位'''
    name = models.CharField(max_length=32, blank=True,null=True, verbose_name="职位名")
    #一个岗位有多个权限，一个权限也会有多个岗位，多对多
    #related_name反向查找使用字段
    auth = models.ManyToManyField(to="Auth",blank=True,null=True,verbose_name="权限",related_name="posau")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "职位表"
class Auth(models.Model):
    '''权限'''
    name = models.CharField(max_length=30,blank=True,null=True, verbose_name="标识")
    url = models.CharField(max_length=64, blank=True,null=True, verbose_name="路径")
    #一个组里面有多个权限，一对多
    group = models.ForeignKey(to="AuthGroup",blank=True,null=True,verbose_name="组",related_name="augro")
    #自己关联自己，当这个字段为空的时候表示对应的是查询,左侧菜单不变化
    to_display=models.ForeignKey(to="Auth",blank=True,null=True,verbose_name="显示",related_name="auau")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "权限表"

class AuthGroup(models.Model):
    '''权限组'''
    name = models.CharField(max_length=16, blank=True,null=True, verbose_name="组名")
    #一个组对应多个菜单，一对多。
    ti = models.ForeignKey(to="Menu", blank=True,null=True, verbose_name="菜单", related_name="aume")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "组表"

class Menu(models.Model):
    '''菜单'''
    title = models.CharField(max_length=16, blank=True,null=True, verbose_name="菜单名")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "菜单表"


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