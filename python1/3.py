
print("*** Election ***")
dict_vote={}

voter = input("Enter a number of voter(s) : ")
votes = input().split()
votes = [int(vote) for vote in votes]
def check(votes):
    for each in votes:
        if each>0 and each <=20:
            return True
    return False   
    
def count_redun(votes,status):
    for select in votes:
     if select>0 and select <=20 and status:
        if select not in dict_vote:
             dict_vote[select]=1
        else:
             dict_vote[select]+=1
     elif not status:
         return f"*** No Candidate Wins ***"
    return dict_vote

# print(count_redun(votes))
# print(count_redun(votes,check(votes)))
if isinstance(count_redun(votes,check(votes)),str):
    print(count_redun(votes,check(votes)))
else:
    max_key=max(count_redun(votes,check(votes)),key=count_redun(votes,check(votes)).get)
list_max=[]
for key,value in dict_vote.items():
    if dict_vote[key]==dict_vote[max_key]:
        list_max.append(key)
list_max.sort()
num_as_int = ' '.join(map(str, list_max))
print(num_as_int)




# print(dict_vote)
# print("Number of voters:", voter)
# print("Votes:", votes)

 