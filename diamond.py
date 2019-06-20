import random

diamond = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
heart = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #user
club = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #computer


def show_diamondCard():
    card_on_desk = random.choice(diamond)
    diamond.remove(card_on_desk)
    return card_on_desk

def bidding_club(card_on_desk):
    index = (len(diamond) // 2) + 1
    if (card_on_desk < index ):
        club_card = random.choice(club[:index])
        club.remove(club_card)
    else:
        club_card = random.choice(club[index - 1:])
        club.remove(club_card)
    return club_card

    
def bidding_heart():
    heart_card = int(input("enter your bid:"))
    heart.remove(heart_card)
    return heart_card

def banker(club_card, heart_card, card_on_desk, heart_score, club_score):
    if (club_card > heart_card ):
        club_score += card_on_desk
        print("u lost the bid!")
    elif (club_card < heart_card ):
        heart_score += card_on_desk
        print("u won the bid!")
    else:
        divide = card_on_desk / 2
        heart_score += divide
        club_score += divide
        print("its a tie!")

def winner(heart_score, club_score):
    if(heart_score > club_score):
        print("you won the game!!!!!")
    else:
        print("oops, you lost the game!!")
    
        
rounds_completed = 0
heart_score = 0
club_score = 0
while(rounds_completed < 13) :
    print("round number: ", rounds_completed + 1 )
    print("-----------------")
    card_on_desk = show_diamondCard()
    print("Card On Desk-----> ", card_on_desk)
    club_card = bidding_club(card_on_desk)
    heart_card = bidding_heart()
    banker(club_card, heart_card, card_on_desk, heart_score, club_score)
    print("club:{} heart:{}".format(club_card, heart_card))
    print("round {} finished...............\n".format(rounds_completed + 1))
    print("your cards: ", heart)
    print("opponents cards: ", club )
    print("\n")
    rounds_completed += 1

print(winner(heart_score, club_score))
    


