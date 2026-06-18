import random

secret = random.randint(1, 10)

guess = int(input("1 to 10 வரை ஒரு எண்ணை உள்ளிடுங்கள்: "))

if guess == secret:
    print("🎉 Correct! You Win!")
else:
    print("❌ Wrong!")
    print("Correct number was:", secret)
