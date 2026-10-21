# useful-codex-skills

个人 Codex 技能与环境迁移仓库，用 Git 保存技能，在不同设备上获取相同版本。

当前提供 **codex-personal-environment 1.0.0**：1 个可加载的个人技能、32 个系统及插件技能目录快照，以及 5 个缓存插件的恢复清单。它不是操作系统或 Conda 环境镜像，也不会把本地环境自动同步到 OpenAI 账户。

## 开始使用

1. [下载仓库 ZIP](https://github.com/dragonslayf/useful-codex-skills/archive/refs/heads/main.zip)，或克隆本仓库。
2. 只需要命令记录功能：按照[安装指南](docs/INSTALL.md)安装 `command-journal`。
3. 需要迁移环境：阅读[环境恢复说明](docs/MIGRATION.md)。

```bash
git clone https://github.com/dragonslayf/useful-codex-skills.git
cd useful-codex-skills
python scripts/verify_plugin.py
```

命令作用：`git clone` 下载仓库及历史到同名目录；`cd` 进入该目录；`python` 执行校验脚本，检查插件清单和所有快照文件的 SHA-256，不安装或执行技能中的脚本。Windows 可使用已安装的 Python 启动方式替代 `python`。

## 仓库内容

| 路径 | 用途 |
| --- | --- |
| `plugins/codex-personal-environment/skills/command-journal/` | 可加载技能：完整记录命令、中文解释、执行结果与对话 Markdown 日志 |
| `plugins/codex-personal-environment/environment/system-skills/` | 6 个系统技能目录快照，仅供参考 |
| `plugins/codex-personal-environment/environment/plugin-skills/` | 26 个插件技能目录快照，包含附属脚本和模板 |
| `plugins/codex-personal-environment/environment/inventory.json` | 技能来源、5 个缓存插件版本和环境摘要 |
| `plugins/codex-personal-environment/environment/config.portable.toml` | 模型和推理级别偏好，需手动合并 |
| `docs/` | 安装、更新、迁移和本次上传命令记录 |
| `scripts/` | 校验与独立插件 ZIP 打包脚本 |

插件的 `skills` 入口只指向个人技能。参考快照不自动加载；它们可能依赖原环境的工具、路径或授权。

## 更新与打包

参见[同步与维护](docs/MAINTENANCE.md)。仓库保留可审阅的源码和资源，避免额外提交一份重复的 27 MB 压缩包；可以在本地生成独立插件 ZIP。

## 来源与许可

个人技能在本次对话中创建；系统与插件快照来自原运行环境。原文件中的许可及权利声明仍适用，本仓库不为第三方内容重新授予许可。缓存插件存在不代表已启用或目标设备具备其服务权限。

不包含账户凭据、会话数据库、项目数据或运行容器。详细范围和已验证事项见[迁移说明](docs/MIGRATION.md)。
