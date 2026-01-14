# Nunchaku PyTorch 2.8 编译指南

这个项目包含 GitHub Actions 配置文件，用于在 GitHub 服务器上编译支持 PyTorch 2.8 的 Nunchaku wheel 文件。

## 文件说明

- `.github/workflows/build_nunchaku.yml` - GitHub Actions 工作流配置
- `modify_torch_version.py` - 本地修改 torch 版本的脚本

## 使用方法

### 方法 1：使用 GitHub Actions（推荐）

1. **创建 GitHub 仓库**
   - 访问 https://github.com/new
   - 创建一个新的公开或私有仓库
   - 仓库名可以任意命名，例如 `nunchaku-torch2.8`

2. **上传文件到仓库**
   - 将 `.github` 文件夹上传到你的 GitHub 仓库
   - 可以通过以下方式上传：
     - 方式 A：使用 GitHub 网页界面上传文件
     - 方式 B：使用 Git 命令行（见下方）

3. **启用 GitHub Actions**
   - 进入你的仓库页面
   - 点击 "Actions" 标签
   - 点击 "I understand my workflows, go ahead and enable them"

4. **手动触发编译**
   - 进入 "Actions" 标签
   - 选择 "Build Nunchaku with PyTorch 2.8" 工作流
   - 点击 "Run workflow" 按钮
   - 填写参数（或使用默认值）：
     - PyTorch version: `2.8.0`
     - Python version: `3.12`
     - CUDA version: `12.8`
   - 点击 "Run workflow" 开始编译

5. **下载编译好的 wheel 文件**
   - 等待编译完成（大约需要 15-30 分钟）
   - 进入 "Actions" 标签
   - 点击最新的工作流运行记录
   - 在页面底部找到 "Artifacts" 部分
   - 下载 `nunchaku-wheel-py3.12-torch2.8.0` 文件
   - 解压下载的 zip 文件，里面包含编译好的 `.whl` 文件

### 方法 2：使用 Git 命令行上传

```bash
# 初始化 Git 仓库
git init
git add .github/
git commit -m "Add GitHub Actions workflow for building Nunchaku with PyTorch 2.8"

# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/你的用户名/你的仓库名.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 方法 3：本地修改现有 wheel（不推荐）

如果你不想等待编译，可以尝试直接修改现有的 wheel 文件：

```bash
# 运行修改脚本
python modify_torch_version.py
```

**注意**：这种方法有风险，如果 Nunchaku 包含编译好的扩展（.pyd 文件），可能与 PyTorch 2.8 不兼容。

## 安装编译好的 wheel 文件

下载并解压 wheel 文件后，使用以下命令安装：

```bash
pip install nunchaku-1.1.0+torch2.8-cp312-cp312-win_amd64.whl
```

## 验证安装

```bash
python -c "import nunchaku; print(nunchaku.__version__)"
python -c "import torch; print(torch.__version__)"
```

## 常见问题

### Q: 编译需要多长时间？
A: 大约需要 15-30 分钟，取决于 GitHub 服务器的负载情况。

### Q: 编译失败怎么办？
A: 查看 GitHub Actions 的运行日志，通常会显示具体的错误信息。常见问题包括：
- PyTorch 版本不兼容
- CUDA 版本不匹配
- 依赖包安装失败

### Q: 可以编译其他版本吗？
A: 可以，在触发工作流时可以自定义 PyTorch 版本、Python 版本和 CUDA 版本。

### Q: wheel 文件有效期是多久？
A: GitHub Actions 的 artifacts 会保留 90 天，之后会自动删除。

## 技术细节

- **编译环境**：GitHub Actions Windows runner
- **GPU 架构支持**：编译时会包含所有支持的 GPU 架构（sm_75, sm_80, sm_86, sm_89, sm_120）
- **编译模式**：使用 `NUNCHAKU_INSTALL_MODE=ALL` 确保兼容所有 GPU

## 许可证

请遵循 Nunchaku 原项目的许可证。
