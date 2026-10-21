# 同步、校验与打包

以下命令均从仓库根目录执行，是供使用者执行的操作示例。

## 获取远程更新

```bash
git pull --ff-only
python scripts/verify_plugin.py
```

`git pull --ff-only` 获取远程提交并仅允许快进更新；分支分叉时停止，不自动创建合并提交。先处理本地修改。第二条命令检查插件完整性。若使用复制安装，仍需将更新后的个人技能复制到目标技能目录；插件安装则按目标客户端流程重新安装，随后新建对话验证。

## 本地修改后刷新校验清单

```bash
python scripts/verify_plugin.py --refresh
python scripts/verify_plugin.py
```

`--refresh` 会根据当前插件文件重新生成 SHA256SUMS.json，因此只能在审查过本地修改后运行，不能用来掩盖下载损坏。第二次运行独立检查生成的清单。功能更新时维护插件版本和文档；提交前检查变更，避免加入凭据或本地会话日志。

## 生成独立插件 ZIP

```bash
python scripts/package_plugin.py
```

脚本先校验文件，再生成 `dist/codex-personal-environment-版本号.zip`；ZIP 顶层是完整插件目录，保留 .codex-plugin 隐藏目录。生成后检查 ZIP CRC，并打印压缩包 SHA-256。已有同名 ZIP 会被本次生成结果替换，dist 已被 Git 忽略。

## 版本管理范围

只提交技能、明确需要的资源和文档。系统及原插件的参考快照不会自动追踪上游更新，更新时需保留来源并重新校验。Git 仓库同步依赖主动提交与拉取，本仓库没有后台自动同步服务。
