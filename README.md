🎯 Django 博客系统

一个功能完整的博客应用，基于 Django 5.2 开发，实现了用户认证、文章管理、权限控制等核心功能。

✨ 功能特性

🔐 用户认证

    ✅ 用户注册与登录
    
    ✅ 安全的密码验证
    
    ✅ 自动登录功能
    
    ✅ 退出登录自动跳转首页

📝 博客管理

    ✅ 文章的创建、编辑、删除
    
    ✅ 文章按时间倒序排列
    
    ✅ 实时搜索功能（标题/内容/作者）
    
    ✅ 分页显示（每页5篇）
    
    ✅ 文章字数统计

🛡️ 权限控制

    游客：可浏览所有文章
    
    普通用户：可创建文章，只能编辑自己的文章
    
    管理员：可管理所有内容和用户

🎨 用户界面

    📱 响应式设计，适配各种设备
    
    🇨🇳 全中文界面，友好易用
    
    🔍 实时搜索框
    
    ⬆️ 返回顶部按钮
    
    💬 自动消失的消息提示

🚀 快速开始

1. 环境准备

bash

    # 克隆项目
    git clone <repository-url>
    cd Blog_Project

    # 创建虚拟环境
    python -m venv venv
    
    # 激活虚拟环境
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    
    # 安装依赖
    pip install django==5.2.9

2. 数据库初始化

bash

    # 应用数据库迁移
    python manage.py makemigrations blogs
    python manage.py migrate
    
    # 创建超级用户
    python manage.py createsuperuser
    # 按照提示输入用户名、邮箱、密码
3. 启动服务

bash

    python manage.py runserver

4. 访问应用

    🌐 首页: http://127.0.0.1:8000/
    
    ⚙️ 管理后台: http://127.0.0.1:8000/admin/
    
    📝 注册页面: http://127.0.0.1:8000/register/
    
    🔑 登录页面: http://127.0.0.1:8000/login/

📁 项目结构

    Blog_Project/
    ├── manage.py                    # Django 项目管理脚本
    ├── requirements.txt             # 项目依赖
    ├── db.sqlite3                   # SQLite 数据库文件
    ├── Blog/                        # 项目主目录
    │   ├── __init__.py
    │   ├── settings.py              # 项目配置
    │   ├── urls.py                  # 主 URL 路由
    │   ├── asgi.py
    │   └── wsgi.py
    └── blogs/                       # 博客应用
        ├── __init__.py
        ├── admin.py                 # 管理后台配置
        ├── apps.py                  # 应用配置
        ├── models.py                # 数据模型定义
        ├── views.py                 # 视图函数
        ├── forms.py                 # 表单定义
        ├── urls.py                  # 应用 URL 路由
        └── migrations/              # 数据库迁移文件
        └── templates/blogs/         # HTML 模板
            ├── base.html            # 基础模板
            ├── index.html           # 首页
            ├── new_post.html        # 新建文章页
            ├── edit_post.html       # 编辑文章页
            ├── post_detail.html     # 文章详情页
            ├── user_posts.html      # 用户文章列表
            ├── login.html           # 登录页
            └── register.html        # 注册页
🔧 核心功能实现

数据模型

python

    class BlogPost(models.Model):
        title = models.CharField(max_length=200, verbose_name="标题")
        text = models.TextField(verbose_name="内容")
        date_added = models.DateTimeField(default=timezone.now, verbose_name="发布日期")
        owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
        # 实现每篇帖子与特定用户关联
权限验证

python

    @login_required
    def edit_post(request, post_id):
        post = get_object_or_404(BlogPost, id=post_id)
        
        # 验证用户只能编辑自己的文章
        if post.owner != request.user:
            messages.error(request, '您没有权限编辑这篇文章。')
            return redirect('blogs:index')

📱 响应式设计

    设备类型	              布局特点
    桌面端 (>768px)	      所有内容水平排列
    平板端 (481-768px)     Logo 和导航分行显示
    手机端 (≤480px)	      垂直堆叠布局

🛠️ 技术栈

    后端框架: Django 5.2.9
    
    数据库: SQLite3（开发环境）
    
    前端技术: HTML5, CSS3, JavaScript
    
    用户认证: Django Auth System
    
    表单处理: Django ModelForm

🧪 测试功能

完成的功能测试：

    ✅ 用户注册和登录
    
    ✅ 文章创建、编辑、删除
    
    ✅ 权限验证（用户只能编辑自己的文章）
    
    ✅ 搜索功能
    
    ✅ 分页功能
    
    ✅ 响应式设计

🚨 故障排除

常见问题

问题1: no such table: blogs_blogpost 错误

bash

    # 解决方案
    python manage.py makemigrations blogs
    python manage.py migrate
问题2: 模板找不到错误

bash

    # 检查模板路径
    blogs/templates/blogs/index.html
问题3: 权限错误

    确保用户已登录
    
    验证用户是文章的作者

📈 项目状态

    ✅ 已完成所有实验要求
    
    ✅ 通过功能测试
    
    ✅ 文档完整
    
    ✅ 代码规范



最后更新: 2025年12月28日

Django 版本: 5.2.9

Python 版本: 3.10+

项目状态: 稳定运行
