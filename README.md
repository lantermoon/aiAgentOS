# aiAgentOS

智能 Agent 业务操作系统 — 基于 FastAPI 的后台管理框架，集成 AI 模型引擎、数字员工、数据仓库等核心模块。

## 技术栈

| 层级 | 技术 |
|---|---|
| 后端框架 | FastAPI + Uvicorn |
| ORM | SQLAlchemy 2.0 + SQLite |
| 认证 | JWT (python-jose) + bcrypt |
| 前端 | Bootstrap 5 + LayUI + Font Awesome + jQuery |
| Python | 3.12+ |

## 快速开始

```bash
# 1. 克隆项目
git clone https://github.com/lantermoon/aiAgentOS.git
cd aiAgentOS

# 2. 创建虚拟环境
python -m venv venv
.\venv\Scripts\activate      # Windows
# source venv/bin/activate   # macOS / Linux

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动服务
python start_server.py
```

浏览器访问 `http://localhost:8000/`，API 文档在 `http://localhost:8000/docs`。

## 项目结构

```
aiAgentOS/
├── start_server.py              # 入口文件
├── requirements.txt             # Python 依赖
├── .env                         # 环境变量配置
│
└── app/
    ├── core/                    # 核心配置层
    │   └── config.py            # Pydantic Settings 全局配置
    ├── db/                      # 数据库层
    │   └── base.py              # SQLAlchemy 引擎与基础类
    ├── models/                  # ORM 数据模型
    │   ├── db.py                # SQLite 数据库初始化
    │   └── user.py              # 用户模型 + bcrypt + CRUD
    ├── schemas/                 # Pydantic 请求/响应 Schema
    │   └── user.py
    ├── controllers/             # 控制器层（路由）
    │   ├── base.py              # JWT 鉴权依赖 (get_current_user)
    │   ├── auth.py              # 登录 / 注册
    │   └── home.py              # 登录后主页
    ├── middleware/               # 中间件
    ├── services/                # 业务逻辑层
    ├── utils/                   # 工具函数
    │
    ├── api/v1/                  # API v1 模块目录
    │   ├── auth/                # 认证模块
    │   ├── llm/                 # 大模型问数
    │   ├── user/                # 用户管理
    │   ├── feature/             # 功能管理
    │   ├── permission/          # 权限管理
    │   ├── digital_employee/    # 数字员工（数据/天气/新闻/音乐/电影）
    │   ├── model_engine/        # 模型引擎（动态/本地-远程/token/流式）
    │   ├── outlook/             # 瞭望管理（CSRF/SSRF/批量采集）
    │   ├── data_warehouse/      # 数据仓库（关系型/非关系型/向量库）
    │   ├── deep_collect/        # 深度采集
    │   ├── api_manage/          # 接口管理
    │   ├── dashboard/           # 数智大屏（报表/数字孪生）
    │   ├── system_config/       # 系统设置
    │   └── statistics/          # 系统统计
    │
    ├── views/                   # 前端页面
    │   ├── login.html           # 登录页
    │   └── index.html           # 后台管理主页
    └── static/dist/             # 静态资源
        ├── css/                 # Bootstrap / LayUI / Font Awesome
        ├── js/                  # jQuery / Bootstrap / LayUI
        └── fonts/               # 字体文件
```

## API 接口

| 端点 | 方法 | 认证 | 说明 |
|---|---|---|---|
| `/` | GET | - | 登录页面 |
| `/login` | GET | - | 登录页面 |
| `/index` | GET | - | 后台主页 |
| `/health` | GET | - | 健康检查 |
| `/api/v1/auth/register` | POST | - | 用户注册 |
| `/api/v1/auth/login` | POST | - | 用户登录，返回 JWT |
| `/api/v1/home` | GET | Bearer | 当前用户信息 |

## 功能模块

- **用户管理** — 注册、登录、JWT 认证、bcrypt 密码加密
- **数字员工** — 数据、天气、新闻、音乐、电影智能代理
- **模型引擎** — 本地私有化模型 / 远程云端模型动态切换，Token 统计，流式响应
- **瞭望管理** — 瞭望源动态管理，CSRF/SSRF 请求伪造技术，批量数据采集
- **数据仓库** — 关系型数据库、非关系型数据库、向量库三种存储容器
- **深度采集** — 多源数据深度抓取
- **接口管理** — API 接口统一管理
- **数智大屏** — 平面炫酷报表组件 + 3D Web 数字孪生（WebGL）
- **系统设置** / **系统统计** — 系统配置与运营数据统计

## 配置说明

编辑 `.env` 文件修改配置：

```env
DEBUG=true
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=60
LLM_BASE_URL=https://api.openai.com/v1
LLM_API_KEY=your-api-key
LLM_MODEL_NAME=gpt-4o
```

## License

MIT