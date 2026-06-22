import random

# 游戏开始
print("=" * 40)
print("     欢迎来到猜数字游戏！")
print("=" * 40)
print("我已经想好了一个1-100之间的数字。")
print("你一共有7次机会，加油！\n")

# 随机生成一个1-100的秘密数字
secret = random.randint(1, 100)
# 最多猜7次
max_attempts = 7
attempts = 0

while attempts < max_attempts:
    # 剩余次数
    remaining = max_attempts - attempts
    print(f"还剩 {remaining} 次机会")

    # 获取玩家输入
    guess = input("请输入你猜的数字：")

    # 检查输入是否合法（必须是数字）
    if not guess.isdigit():
        print("❌ 请输入有效的数字！\n")
        continue

    guess = int(guess)

    # 检查数字范围
    if guess < 1 or guess > 100:
        print("❌ 数字要在1-100之间哦！\n")
        continue

    # 比较猜的数字和秘密数字
    attempts += 1

    if guess < secret:
        print("📈 太小了，再大一点！\n")
    elif guess > secret:
        print("📉 太大了，再小一点！\n")
    else:
        # 猜对了！
        print(f"\n🎉 恭喜你！就是 {secret}！")
        print(f"你一共猜了 {attempts} 次。")
        break
else:
    # 7次都没猜对，游戏结束
    print(f"\n💔 很遗憾，7次机会用完了。")
    print(f"正确答案是 {secret}。")
    print("下次再来挑战吧！")

print("\n感谢游玩，再见！")