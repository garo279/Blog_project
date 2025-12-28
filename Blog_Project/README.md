📋 项目概述

本项目是一个基于 Django 5.2 开发的完整博客系统，实现了用户认证、文章管理、权限控制等核心功能。系统严格遵循实验要求，包含所有必要的功能模块。

🎯 实验要求完成情况

✅ 19-1. 基础博客功能

    创建 Django 项目 Blog
    
    创建应用 blogs
    
    定义 BlogPost 模型（包含 title、text、date_added 字段）
    
    创建超级用户和管理站点
    
    实现按时间顺序显示所有帖子的主页
    
    创建发布新帖子的表单
    
    创建编辑现有帖子的表单

    完整的表单测试功能

✅ 19-5. 受保护的博客功能

    每篇博客帖子与特定用户关联（owner 外键）
    
    所有帖子公开可访问
    
    只有已注册用户才能添加帖子
    
    只有已注册用户才能编辑帖子
    
    编辑时验证用户只能编辑自己的帖子

🏗️ 项目结构

    text
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
🔧 功能特性

    🔐 用户认证系统

            用户注册与登录
            
            安全的密码验证
            
            自动登录功能
            
            退出登录重定向到首页
            
            权限装饰器保护敏感操作
    

    📝 博客文章管理

            创建、编辑、删除文章
            
            文章按时间倒序排列
            
            文章字数统计
            
            搜索功能（标题、内容、作者）
            
            分页显示（每页5篇文章）
            

    👥 用户权限控制

            游客：可浏览所有文章
            
            普通用户：可创建文章，只能编辑自己的文章
            
            超级用户：可通过管理后台管理所有内容
            

    🎨 用户界面

            全中文界面，友好易用
            
            响应式设计，适配各种设备
            
            美观的渐变导航栏
            
            实时搜索框
            
            返回顶部按钮
            
            自动消失的消息提示


🚀 快速开始
1. 环境准备

bash
    
    # 克隆或下载项目
    # 进入项目目录
    cd Blog_Project
    #创建虚拟环境
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

    # 创建数据库迁移文件
    python manage.py makemigrations blogs

    # 应用数据库迁移
    python manage.py migrate
    
    # 创建超级用户（管理员）
    python manage.py createsuperuser
    # 按照提示输入用户名、邮箱、密码
3. 运行开发服务器

bash

    python manage.py runserver
4. 访问应用

首页：http://127.0.0.1:8000/

管理后台：http://127.0.0.1:8000/admin/

注册页面：http://127.0.0.1:8000/register/

登录页面：http://127.0.0.1:8000/login/

📖 使用指南
1. 管理员操作


    访问管理后台（/admin/）
    
    使用超级用户账号登录

    可以：
    
        管理所有博客文章
        
        管理用户账户

        设置用户权限

2. 普通用户操作


    注册账号：
    
        点击右上角"注册"按钮
        
        填写用户名、邮箱、密码
        
        自动登录并跳转到首页
    
    创建文章：
    
        登录后点击"写文章"
        
        填写标题和内容
        
        点击"发布文章"
    
    编辑文章：
    
        在文章列表中找到自己的文章
        
        点击"编辑"按钮
        
        修改后保存
    
    查看个人文章：
    
        点击右上角"我的文章"
        
        查看自己发布的所有文章

3. 游客操作


    浏览所有公开文章
    
    查看文章详情
    
    使用搜索功能
    
    注册或登录以发布文章

🛡️ 安全特性

CSRF 防护

    所有表单包含 CSRF 令牌
    
    防止跨站请求伪造攻击

SQL 注入防护

    使用 Django ORM 查询
    
    参数化查询，自动转义

XSS 防护

    模板自动转义 HTML
    
    安全的用户输入处理

权限验证

    @login_required 装饰器保护敏感视图
    
    编辑时验证用户所有权
    
    防止越权操作

🧪 测试功能

完成的功能测试

    ✅ 用户注册和登录
    
    ✅ 文章创建、编辑、删除
    
    ✅ 权限验证（用户只能编辑自己的文章）
    
    ✅ 搜索功能
    
    ✅ 分页功能
    
    ✅ 响应式设计
    
    ✅ 表单验证
    
    ✅ 错误处理

测试用户

    管理员：拥有所有权限
    
    普通用户：只能管理自己的文章
    
    游客：只能浏览文章

🔧 技术栈

    后端框架：Django 5.2.9
    
    数据库：SQLite3（开发环境）
    
    前端技术：HTML5、CSS3、JavaScript
    
    模板引擎：Django Template Language
    
    用户认证：Django Auth System
    
    表单处理：Django ModelForm

📁 核心文件说明
models.py

python


    class BlogPost(models.Model):
        title = models.CharField(max_length=200, verbose_name="标题")
        text = models.TextField(verbose_name="内容")
        date_added = models.DateTimeField(default=timezone.now, verbose_name="发布日期")
        owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
        # 实现每篇帖子与特定用户关联
views.py

python

    @login_required
    def edit_post(request, post_id):
        post = get_object_or_404(BlogPost, id=post_id)
        
        # 验证用户只能编辑自己的帖子
        if post.owner != request.user:
            messages.error(request, '您没有权限编辑这篇文章。')
            return redirect('blogs:index')
        # 实现受保护的编辑功能
forms.py

python
    
    class BlogPostForm(forms.ModelForm):
        class Meta:
            model = BlogPost
            fields = ['title', 'text']  # 只包含需要的字段
            
    class CustomUserCreationForm(UserCreationForm):
        # 自定义用户注册表单，添加邮箱验证

🌐 API 端点

    端点	               方法	             描述	             权限
    /	               GET	            首页，显示所有文章	     公开
    /new/	               GET/POST	            创建新文章	             需登录
    /post/<id>/	       GET	            查看文章详情	             公开
    /post/<id>/edit/       GET/POST	            编辑文章	             需登录且是作者
    /register/	       GET/POST	            用户注册	             公开
    /login/  	       GET/POST	            用户登录	             公开
    /logout/	       POST	            用户退出	             需登录
    /user/<username>/      GET	            用户文章列表	             公开
📱 响应式设计

屏幕适配

    桌面端 (>768px)：所有内容水平排列
    
    平板端 (481-768px)：Logo 和导航分行显示
    
    手机端 (≤480px)：垂直堆叠布局

移动端优化

    触摸友好的按钮大小
    
    简洁的导航菜单
    
    自适应图片和布局

🚨 故障排除

常见问题

问题1：数据库错误 no such table: blogs_blogpost

bash

    # 解决方案：
    python manage.py makemigrations blogs
    python manage.py migrate
问题2：模板找不到错误

bash

    # 检查模板路径：
    blogs/templates/blogs/index.html
问题3：权限错误

    确保用户已登录
    
    验证用户是文章的作者

问题4：静态文件404

    开发环境可忽略，不影响功能
    
    生产环境需要收集静态文件
📈 项目特点

实践价值

完整的 Django 项目示例

    适合学习和理解 Django MTV 架构
    
    包含认证、表单、模板等核心概念

实际应用场景

    真实的博客系统需求
    
    用户权限管理的典型实现
    
代码规范性

    清晰的代码结构
    
    详细的中文注释
    
    遵循 Django 最佳实践

扩展性

    易于添加新功能（如评论、分类、标签等）
    
    支持更换数据库（MySQL、PostgreSQL）
    
    可集成前端框架（Bootstrap、Vue.js）


✨ 贡献者

    项目开发：基于实验要求完成
    
    代码优化：包含完整的错误处理和用户友好设计
    
    文档编写：详细的 README 和使用指南

📞 支持

如遇到问题，请：

    查看本 README 的故障排除部分
    
    检查终端错误信息
    
    确保已正确执行所有迁移命令
    
    验证模板文件路径正确

🎉 项目状态

    ✅ 已完成所有实验要求
    
    ✅ 通过功能测试
    
    ✅ 文档完整
    
    ✅ 代码规范

最后更新：2025年12月28日

Django 版本：5.2.9

Python 版本：3.10+

项目状态：稳定运行