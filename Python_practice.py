
my_votes = int(input("How many votes did you get in the election? "))
total_votes=int(input("What is the total votes in the election? "))

message_to_canidate = (
    f"you received {my_votes:,} number of votes."
    f"The total number of votes in the elections was {total_votes:,}."
    f"You received {my_votes/total_votes *100:.2f} % of the total votes.")

print(message_to_canidate)