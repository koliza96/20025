#========SEND======@ZERO_CYBER_TEM
#TG====== https://t.me/ZERO_CYBER_TEM
#=======____FREE______=======
#========______GIVE==========
import requests
import time

def get_friends_list(access_token):
    url = "https://graph.facebook.com/me/friends"
    params = {'access_token': access_token}
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            friends_data = response.json().get('data', [])
            return friends_data
        else:
            error_message = response.json().get('error', {}).get('message', 'Unknown error')
            print(f"Failed to fetch friends list. Error: {error_message}")
            return []
    except Exception as e:
        print(f"An error occurred while fetching the friends list: {e}")
        return []

def unfriend_single_person(friend_name,friend_id, access_token):
    url = f"http://m.facebook.com/a/removefriend.php?friend_id={friend_id}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    params = {'fb_dtsg_ag': 'AQFrMxhXW-VJ:AXgK5u3C5cGa', 'confirm': 'Confirm'}
    
    try:
        response = requests.post(url, headers=headers, params=params, cookies={'locale': 'en_US'})
        if response.status_code == 200:
            print(f"Successfully unfriended : {friend_name}")
        else:
            print(f"Failed to unfriend : {friend_name}")
    except Exception as e:
        print(f"An error occurred : {friend_name}: {e}")

def unfriend_all_friends(access_token):
    friends_list = get_friends_list(access_token)
    
    if not friends_list:
        print("No friends found or failed to retrieve friends list.")
        return
    
    total_friends = len(friends_list)
    print(f"Total number of friends : {total_friends}")
    
    for friend in friends_list:
        friend_id = friend.get('id')
        friend_name = friend.get('name')
        unfriend_single_person(friend_name,friend_id, access_token)
        time.sleep(2)  
    
if __name__ == "__main__": 
    access_token = input("input your token : ")    
    unfriend_all_friends(access_token)