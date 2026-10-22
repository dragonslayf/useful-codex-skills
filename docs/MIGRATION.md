# 环境恢复与边界

## 已保存

- 2 个个人技能：command-journal、yinxiang-skill，可通过插件加载。
- 6 个系统技能快照：imagegen、openai-docs、plugin-creator、review-agent、skill-creator、skill-installer。
- 26 个插件技能目录快照及其附属资源。
- 5 个缓存插件的名称与版本：github、openai-templates、plugin-management、sites、work-pets。准确版本见 inventory.json。
- 源环境运行时摘要及模型偏好。

## 在目标设备恢复

1. 安装目标设备支持的 Codex 客户端并登录。
2. 获取本仓库，校验文件，然后安装个人技能或完整插件。
3. 按 inventory.json 安装需要的原插件，重新完成服务连接和授权。源环境缓存存在不能证明插件处于启用状态。
4. 按需将 config.portable.toml 中的模型偏好合并到目标配置，模型必须对目标账户可用。不要覆盖整个配置文件。
5. 系统技能优先使用客户端自带版本。快照中的绝对路径、同级技能引用及环境专用工具需要逐项适配，不能直接假定可执行。
6. 测试实际任务，确认模型、工具、文件写入和技能日志均正常。

## 未包含

账户凭据、令牌（包括印象笔记 Token）、会话及记忆数据库、项目代码和数据集、Conda/Python 软件环境、操作系统镜像、远程工具实现均不在此包中。原 /workspace 的项目 trusted 设置未导出，因为它属于本机信任选择。

inventory.json 中的绝对来源路径仅用于追溯，不是目标设备必须创建的目录。自定义 command-journal 会根据目标工作区创建日志；yinxiang-skill 在新设备上需要重新完成印象笔记授权。

## 已验证与尚未验证

原插件通过插件创建工具的格式校验；原 ZIP 完成压缩包与逐文件 SHA-256 校验。仓库维护脚本还会检查文件丢失、额外文件和哈希不一致。

目标设备安装、账户权限、模型可用性、远程服务连接及模板实际执行尚需在目标设备验证。Git 同步文件不等于同步账户授权，也不会自动安装插件更新。
