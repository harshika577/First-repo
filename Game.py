import random
print("🎯 Number Guessing Game ")
print("Nenu 1-100 madhya oka number anukunna. 5 chances ")

secret = random.randint(1, 100)

for attempt in range(1, 6):
    guess = int(input(f"\nAttempt {attempt}/5: Nee guess cheppu: "))
    
    if guess == secret:
        print(f"🔥 GETHE RA! {attempt} attempts lo correct kottesav!")
        break
    elif guess < secret:
        print("⬆️ Chinnadi cheppav. Konchem peddadi kottu")
    else:
        print("⬇️ Peddadi cheppav. Konchem chinnadi kottu")
else:
    print(f"\n😭 Game Over ra. Nenu anukunna number: {secret}")
