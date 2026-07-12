### 搞个项目

后端用Django

conda create -n modl python=3.12

conda activate mold

python -m pip install --upgrade pip

pip install django==6.0.6

pip install djangorestframework==3.17.1

pip install django-cors-headers==4.9.0

pip install pymysql

cd backend

django-admin startproject config .

### 运行项目：

python manage.py runserver

建一个app：python manage.py startapp machines

写models.py

数据库迁移

生成迁移文件--迁移

python manage.py makemigrations

创建管理员

python manage.py createsuperuser

注册

@admin.register(模型)
class 模型Admin(admin.ModelAdmin):
	...

​	...

​	后台配置都写这里
​    

浏览器
    │
    ▼
config/urls.py
    │
    ▼
machines/urls.py
    │
    ▼
views.py
    │
    ▼
HttpResponse / JsonResponse
    │
    ▼
浏览器





from django.http import JsonResponse

return JsonResponse({
    "name": "Machine01",
    "status": "running"
})



from rest_framework.response import Response

return Response(data)

在config/settings.py 里面装drf

INSTALLED_APPS = [
    ...
    "rest_framework",
]

序列化和反序列化

from rest_framework import serializers
from .models import Machine

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"



数据库(SQLite/MySQL)
        │
        ▼
Correspondence Model
        │
        ▼
CorrespondenceSerializer   ← 翻译官
        │
        ▼
JSON
        │
        ▼
Vue 页面



## 我建议我们接下来的学习顺序

你已经完成了 DRF 最基础的一步，下面建议按这个顺序学：

1. **GET 单条数据**（根据 `id` 查询一条记录）
2. **POST 新增数据**
3. **PUT 修改数据**
4. **DELETE 删除数据**



npm create vue@latest frontend

vue

| Add TypeScript? | ✅ Yes | 我们全程使用 TS |
| --------------- | ----- | --------------- |
|                 |       |                 |

| Add JSX Support? | ❌ No | Vue 初学不用 JSX |
| ---------------- | ---- | ---------------- |
|                  |      |                  |

| Add Vue Router for Single Page Application development? | ❌ No | 后面单独讲 Router，更容易理解 |
| ------------------------------------------------------- | ---- | ----------------------------- |
|                                                         |      |                               |

| Add Pinia for state management? | ❌ No | 后面讲状态管理时再加 |
| ------------------------------- | ---- | -------------------- |
|                                 |      |                      |

| Add Vitest for Unit Testing? | ❌ No | 目前不用写单元测试 |
| ---------------------------- | ---- | ------------------ |
|                              |      |                    |

| Add an End-to-End Testing Solution? | ❌ No | 以后企业开发再说 |
| ----------------------------------- | ---- | ---------------- |
|                                     |      |                  |

| Add ESLint for code quality? | ✅ Yes | 帮你检查代码规范，非常推荐 |
| ---------------------------- | ----- | -------------------------- |
|                              |       |                            |

| Add Prettier for code formatting? | ✅ Yes | 自动格式化代码，非常推荐 |
| --------------------------------- | ----- | ------------------------ |
|                                   |       |                          |

   npm install
   npm run format
   npm run dev

npm install vue-router



# Day2

安装elment Plus，及其图标

npm install element-plus

npm install @element-plus/icons-vue

# Day 3

npm install axios 

跨区域访问

pip install django-cors-headers



npm install pinia





我们改Django

backend/

config/                     # Django配置

to_mes/

    admin.py
    
    apps.py
    
    urls.py
    
    models/                 # SQLite模型
        __init__.py
        correspondence.py
        stock.py
        user.py
    
    serializers/
        __init__.py
        correspondence.py
        stock.py
    
    views/
        __init__.py
        mold.py
        stock.py
    
    services/
        __init__.py
    
        mes/                # 负责访问MES数据库
            __init__.py
            mold.py
            stock.py
    
        business/           # 业务计算
            __init__.py
            mold.py
            stock.py
    
    utils/
        db.py               # MES数据库连接
        excel.py            # Excel导出
        response.py         # 统一返回
    
    migrations/

npm install xlsx file-saver

好方法 

rm -rf node_modules
npm install

pip	install request