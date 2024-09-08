import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = webdriver.ChromeOptions()
# options.add_argument('--auto-open-devtools-for-tabs')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.instagram.com')
time.sleep(2)

# Input your credentials
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

# your_username = 'iamsatwik_'
# your_password =  'humming1bird'
your_username = 'deekshaaa_ch'
your_password =  'gaynigga@69'

username.send_keys(your_username)
password.send_keys(your_password)
password.send_keys(Keys.RETURN)

time.sleep(10)  # Wait for login to complete

# Navigate to your profile
driver.get('https://www.instagram.com/' + your_username + '/')
time.sleep(2)

# profile_pic_element = driver.find_element(By.XPATH, '//img[contains(@alt, "profile")]')
# profile_pic_url = profile_pic_element.get_attribute('src')

# response = requests.get(profile_pic_url)
# if response.status_code == 200:
#     with open('profile_picture.jpg', 'wb') as file:
#         file.write(response.content)

# print(f"Profile picture downloaded successfully from {profile_pic_url}")

# # Click on the follower list
# followers_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'followers')
# followers_link.click()
# time.sleep(2)

# # Scroll to load all followers
# followers_panel = driver.find_element(By.XPATH, '//div[@role="dialog"]/div/div[2]/div/div/div[3]')
# last_height = driver.execute_script("return arguments[0].scrollHeight", followers_panel)

# while True:
#     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', followers_panel)
#     time.sleep(2)
#     new_height = driver.execute_script("return arguments[0].scrollHeight", followers_panel)
#     if new_height == last_height:
#         break
#     last_height = new_height

# # Extract follower names
# followers = []
# followers_elements = driver.find_elements(By.XPATH, '//div[@role="dialog"]//a')
# for follower_element in followers_elements:
#     name = follower_element.text
#     followers.append(name)

# # Close the follower dialog
# follower_close = driver.find_element(By.XPATH, '//div[@role="dialog"]//button')
# follower_close.click()
# time.sleep(2)

# # Click on the following list
# following_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'following')
# following_link.click()
# time.sleep(2)

# # Scroll to load all followers
# following_panel = driver.find_element(By.XPATH, '//div[@role="dialog"]/div/div[2]/div/div/div[4]')
# last_height = driver.execute_script("return arguments[0].scrollHeight", following_panel)

# while True:
#     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', following_panel)
#     time.sleep(2)
#     new_height = driver.execute_script("return arguments[0].scrollHeight", following_panel)
#     if new_height == last_height:
#         break
#     last_height = new_height

# # Extract follower names
# followings = []
# following_elements = driver.find_elements(By.XPATH, '//div[@role="dialog"]//a')
# for following_element in following_elements:
#     name = following_element.text
#     followings.append(name)

# # Close the following dialog
# following_close = driver.find_element(By.XPATH, '//div[@role="dialog"]//button')
# following_close.click()
# time.sleep(2)

# followers.remove('')
# print("Number of Followers: ",len(followers))
# print("List of Followers", followers)

# followings.remove('')
# print("Number of Followings: ",len(followings))
# print("List of Followings", followings)

# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# # Find posts in the DOM
# posts = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')

# # Loop through each post
# for post_index, post in enumerate(posts):
#     post_url = post.get_attribute('href')
#     driver.execute_script("window.open('');")
#     driver.switch_to.window(driver.window_handles[1])
#     driver.get(post_url)
#     post_id = post_url.replace('https://www.instagram.com', '')

#     time.sleep(2)

#     try:
#         media_elements = driver.find_element(By.XPATH, '//div[@role="button"]//img')
#         media_element_time = driver.find_element(By.XPATH, f'//a[@href="{post_id}"]//time').get_attribute('datetime')

#         print(media_element_time)
#         # Handle multiple images or videos in a carousel post
#         try:
#             presentation = driver.find_element(By.XPATH, '//div[@role="presentation"]')
#             media_index = 0
#             unique_urls = set()
#             while True:
#                 time.sleep(2)
#                 media_elements = presentation.find_elements(By.XPATH, "//li//img")
                
#                 for media_element in media_elements:
#                     media_url = media_element.get_attribute('src')
#                     unique_urls.add(media_url)
#                 try:
#                     next_button = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Next"]'))
#                     )
#                     next_button.click()
#                     media_index += 1
#                 except Exception:
#                     break
            
#             # Download the images
#             for media_index, media_url in enumerate(unique_urls):
#                 response = requests.get(media_url)
#                 if response.status_code == 200:
#                     with open(f'post_{post_index + 1}_media_{media_index + 1}.jpg', 'wb') as file:
#                         file.write(response.content)
#                 print(f"Post {post_index + 1}, media {media_index + 1} downloaded successfully from {media_url}")

#         except Exception:
#             media_url = media_elements.get_attribute('src')

#             response = requests.get(media_url)
#             if response.status_code == 200:
#                 with open(f'post_{post_index + 1}.jpg', 'wb') as file:
#                     file.write(response.content)
#             print(f"Post {post_index + 1} downloaded successfully from {media_url}")

#     except Exception as e:
#         print(f"Error processing post {post_index + 1}: {e}")

#     # Close the current tab and switch back to the original tab
#     driver.close()
#     driver.switch_to.window(driver.window_handles[0])

driver.get('https://www.instagram.com/direct/inbox/?hl=en')
time.sleep(2)

notify_close = driver.find_element(By.XPATH, '//div[@role="dialog"]//button[2]')
notify_close.click()

msg_list = driver.find_element(By.XPATH, '//div[@role="list"]/div/div/div')
last_height = driver.execute_script("return arguments[0].scrollHeight", msg_list)
chatters = []
attempt = 0
scroll_pause_time = 5

while attempt < 5:
    chatting_elements = msg_list.find_elements(By.XPATH, '//div[@role="listitem"]')
    # chatters.append(chatting_element.text for chatting_element in chatting_elements)
    for chatting_element in chatting_elements:
        chatter_info = {}
        try:
            # Extracting username or relevant field
            chatter_element = chatting_element.find_elements(By.XPATH, './/span[@dir="auto"]')
            username = chatter_element[0].text
            chatter_info['username'] = username
            
            # Extracting other info, such as message or time (example)
            message = chatter_element[1].text
            chatter_info['message'] = message
            
        except Exception as e:
            print(f"Error extracting fields: {e}")
    
        # Add the dictionary to the list of chatters
        chatters.append(chatter_info)

    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', msg_list)
    time.sleep(scroll_pause_time)

    new_height = driver.execute_script("return arguments[0].scrollHeight", msg_list)
    if new_height == last_height:
        attempt += 1
    else:
        attempt = 0
    last_height = new_height
    # msg_user = driver.find_elements(By.XPATH, '//*[@id="mount_0_0_yt"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div')
    # msg_height = driver.execute_script("return arguments[0].scrollHeight", msg_user)

    # while True:
        # driver.execute_script('arguments[0]')

    # print(chatting_element.text)
unique_chatters = set(tuple(chatter.items()) for chatter in chatters)
unique_chatters = [dict(chatter) for chatter in unique_chatters]

print(unique_chatters)
print(len(unique_chatters))

# Close the browser
driver.quit()