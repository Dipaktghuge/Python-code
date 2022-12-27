def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type==1:
        express_queue.append(person_name)
        return express_queue
    elif ticket_type==0:
        normal_queue.append(person_name)
        return normal_queue
    return[]
print(add_me_to_the_queue(['Tony', 'Bruce'], ['RobotGuy', 'WW'], 0, 'HawkEye'))
print(add_me_to_the_queue(['Tony', 'Bruce'], ['RobotGuy', 'WW'], 1, 'RichieRich'))
print(add_me_to_the_queue(['Suppandi'], ['Kalia'],0,'Shambhu'))


def find_my_friend(queue, friend_name):
    if friend_name in queue:
        return queue.index(friend_name)
    else:
        raise ValueError("friend is notin Queue")
queue=['Suppandi', 'Kalia', 'Shambhu', 'Tantri', 'Hodja']
friend="kalia"
print(f"{friend} is at index{queue,friend} in the queue{queue}")

def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name) # from docs.python.org!
    return queue

queue, index, friend =['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 0, 'Bucky'
print(f"Original Queue: {queue}.")
print(f"{friend} inserted is at index {index}. \
    New Queue: {add_me_with_my_friends(queue, index, friend)}.")

index, friend = 1, "Asterix"
print(f"{friend} inserted is at index {index}. \
    New Queue: {add_me_with_my_friends(queue, index, friend)}.")

index, friend = 5, "TinTin"
print(f"{friend} inserted is at index {index}. \
    New Queue: {add_me_with_my_friends(queue, index, friend)}.")

def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue

queue,person=['Natasha', 'Steve', 'Ultron', 'Wanda', 'Rocket'],'Ultron'
print(f"Original Queue:{queue}")
print(f"{person} removed.New queue:{remove_the_mean_person(queue,person)}")
def how_many_namefellows(queue, person_name):
	
    return queue.count(person)
queue,person=['Natasha', 'Steve', 'Ultron','Ultron', 'Wanda', 'Rocket','Ultron'],'Ultron'
print(f"Original Queue:{queue}")
print(f"{person} appears:{how_many_namefellows(queue,person)}")	
def remove_the_last_person(queue):
	"""

	:param queue: list - names in the queue.
	:return: str - name that has been removed from the end of the queue.
	"""
	pass
def sorted_names(queue):
    return sorted(queue)
queue=['Steve', 'Ultron', 'Natasha', 'Rocket']
print(f"Original Queue:{queue}")
print(f" appears:{sorted_names(queue)}")	
