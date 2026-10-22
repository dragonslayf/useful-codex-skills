# 安装

## 方式一：安装单个技能

将以下任一完整文件夹复制到目标设备的用户技能目录：

- `plugins/codex-personal-environment/skills/command-journal`
- `plugins/codex-personal-environment/skills/yinxiang-skill`

当前官方文档列出的用户技能目录为 `~/.agents/skills/`；源环境使用的是 `~/.codex/skills/`。`~` 表示当前用户主目录，请按目标客户端实际发现路径选择。不要把同一技能同时复制到多个扫描目录。

最终结构应为 `用户技能目录/技能名/SKILL.md`。如果已有同名技能，先比较内容并备份，再决定更新，避免直接覆盖本地修改。

在新对话中输入：

> 使用 $command-journal，执行任务时完整记录命令及中文说明，并写入本对话对应的 Markdown 文件。

技能匹配相关任务时也可被自动选择，但它是模型工作流指令，不是拦截每次 Shell 执行的系统审计程序。请检查实际生成的日志。

安装 `yinxiang-skill` 后，在新对话中说“授权印象笔记”，按提示到印象笔记官方页面获取 Token 并完成本机授权。仓库不包含 Token，不要把 Token 写入 Git 或公开分享。

## 方式二：作为完整插件安装

插件根目录为 `plugins/codex-personal-environment`，清单位于其 `.codex-plugin/plugin.json`，不得只复制 SKILL.md 或省略隐藏目录。

使用目标客户端提供的本地插件导入或个人插件分享入口，选择完整插件目录或由打包脚本生成的 ZIP。客户端是否提供该入口需要在目标设备确认；本仓库没有登记远程插件市场，不能直接假定仓库 URL 就是可安装市场地址。

如果客户端没有对应入口，先使用方式一。原环境的 `codex://` 本地链接依赖原设备的个人市场路径，不适合作为其他设备的安装链接。

## 验证安装

- 新建对话，确认可发现 command-journal 和 yinxiang-skill（插件安装后可能显示插件命名空间）。
- 明确调用该技能执行一个正常任务，确认生成 `command-logs/日期-对话标识.md`。
- 日志应包含完整命令、中文参数说明、工作目录及结果；建议命令应注明未执行。
- 续聊应追加同一文件，新对话应创建独立文件。
- 对 yinxiang-skill，完成本机授权后执行一次只读查询，确认能够访问印象笔记；不要把 Token 写入仓库。

官方参考：[Build skills](https://learn.chatgpt.com/docs/build-skills)。
