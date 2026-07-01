import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

c_card =random.choices(cards, k=2)
u_card =random.choices(cards, k=2)

print(f"Your cards: {u_card}, current score: {sum(u_card)}")
print(f"Computer's first card: {c_card[0]}")                                                                                
user_input = input("Type 'y' to get another card, type 'n' to pass: ")
if user_input == 'y':
    u_card.append(random.choice(cards))
    print(f"Your cards: {u_card}, current score: {sum(u_card)}")
    if sum(u_card) > 21:
        print("You went over. You lose 😭")
    else:
        user_input = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_input == 'y':
            u_card.append(random.choice(cards))
            print(f"Your cards: {u_card}, current score: {sum(u_card)}")
            if sum(u_card) > 21:
                print("You went over. You lose 😭")
            else:
                print("You chose to pass.")
        elif user_input == 'n':
            if sum(u_card) > 21:
                print("You went over. You lose 😭"  )
                print(f"Your final hand: {u_card}, final score: {sum(u_card)}" )
                print(f"Computer's final hand: {c_card}, final score: {sum(c_card)}")       
            else:
                print(f"Your final hand: {u_card}, final score: {sum(u_card)}" )
                print(f"Computer's final hand: {c_card}, final score: {sum(c_card)}")   
                print("You chose to pass.")