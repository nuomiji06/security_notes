"""
安全学习笔记生成脚本
使用 with 语句安全地写入文件（自动关闭文件句柄）
"""

notes = [
    "1. 最小权限原则：只授予完成任务所必需的最小权限。",
    "2. 输入验证：永远不要信任用户输入，先校验再使用。",
    "3. 密码存储：使用 bcrypt/argon2 加盐哈希，绝不存明文。",
    "4. HTTPS 必备：传输层加密防止中间人窃听。",
    "5. 定期备份：备份是应对勒索软件的最后一道防线。",
]

# with 语句：进入时打开文件，退出时自动 close（即使中途抛异常）
with open("notes.txt", "w", encoding="utf-8") as f:
    for line in notes:
        f.write(line + "\n")

print("✅ notes.txt 写入完成")