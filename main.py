from telethon import TelegramClient, events, sync

api_id = 5193417
api_hash = '55909d877eef1f996884aee6734dddb9'


def get_group(client, msg):
    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)


    print()
    i = 0
    for g in chats:
        print(str(i) + '- ' + g.title)
        i += 1


    g_index = input(msg)
    
    return chats[int(g_index)]



def get_messages(client, group):
    messages = client.get_messages(group, limit=100)
    for i in messages:
        print(i)



if __name__ == '__main__':
    phone = input('Enter phone number: ')

    client = TelegramClient(phone, api_id, api_hash)
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))

    target_group = get_group(client, 'Choose your group number: ')

    get_messages(client, target_group) 
