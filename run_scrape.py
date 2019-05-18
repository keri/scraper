import pandas as pd
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, InvalidArgumentException


def sign_in(login, password, driver):#if on the main linked in with the sign in on top right
    select = driver.find_elements_by_css_selector
    select_one = driver.find_element_by_css_selector
    driver.get('https://www.linkedin.com/')
    try:
        sign_in = select_one('input#login-email')
        sign_in.click()
        sign_in.send_keys(login)
        password_in = select_one('input#login-password')
        password_in.click()
        password_in.send_keys(password)
        login = select_one('input#login-submit')
        login.click()
    except NoSuchElementException:       
        try:
            sign_in = select_one('a.nav__button-secondary')
            sign_in.click()
            try:
                input_name = select_one('input#username')
                input_name.send_keys(login)
                input_pwd = select_one('input#password')
                input_pwd.send_keys(password)
                login_action = select_one('div.login__form_action_container ')
                login_action.click()
            except NoSuchElementException:
                    driver.get(sign_in.get_attribute('href'))
                    input_name = select_one('input#username')
                    input_name.click()
                    input_name.send_keys(login)
                    input_password = select_one('input#password')
                    input_password.click()
                    input_password.send_keys(password)
                    login_btn = select_one('button.btn__primary--large.from__button--floating')
                    login_btn.click()
        except NoSuchElementException:
            try:
                email_input = select_one('input.login-email')
                email_input.click()
                email_input.send_keys(input)
                password_input = select_one('input.login-password')
                password_input.click()
                password_input.send_keys(password)
                submit = select_one('#login-submit')
                submit.click()

            except:
                print('nope, didnt work')
    return(driver)

def get_message_urls(driver, df):
    select = driver.find_elements_by_css_selector
    select_one = driver.find_element_by_css_selector

    message_thread_urls = []

    try:
    	unordered_list = select_one('ul.msg-conversations-container__conversations-list')
    except NoSuchElementException:
    	get_message_urls(driver, df)
    convo_list = unordered_list.find_elements_by_css_selector('a')
    for c in convo_list:
        message_thread_urls.append(c.get_attribute('href'))
    #adding the first # of messages to match the index of the df as there were some inconsistencies in the number of message urls and threads scraped.
    df['Message URL'] = message_thread_urls[:len(df)]
    return(df)


def get_full_messages(driver,df):
    select = driver.find_elements_by_css_selector
    select_one = driver.find_element_by_css_selector

    convo_list = select('li.msg-conversation-listitem')
    for convo in convo_list:
        try:
            convo.click()
            try:
                message = select_one('div.msg-s-message-list').text
                message_list = message.split('\n')
                time.sleep(1)
                try:
                    message_container = select_one('div.global-title-container')
                    profile_url = message_container.find_element_by_css_selector('a').get_attribute('href')
                except NoSuchElementException:
                    profile_url = 'unable to get'
                if message_list[0] == 'Recruiter':
                	name = message_list[0]
                	df = df.append({'First Name': name, 'Last Name':'none', 'Message': message_list, 'Date': message_list[1], 'Profile':profile_url}, ignore_index=True)
                elif '2' in message_list[0]:
                    if len(message_list) >= 4:
                    	name = message_list[3].split(' ')
                    	df = df.append({'First Name': name[0], 'Last Name': name[1], 'Message': message_list, 'Date': message_list[0], 'Profile':profile_url}, ignore_index=True)
                    else:
                    	name = message_list[1][:-21]
                    	df = df.append({'First Name': name[0], 'Last Name': name[1], 'Message': message_list, 'Date': message_list[0], 'Profile':profile_url}, ignore_index=True)
                else:
                	name = message_list[0].split(' ')
                	df = df.append({'First Name': name[0], 'Last Name': name[1], 'Message': message_list, 'Date': message_list[5], 'Profile': profile_url}, ignore_index=True)
            except NoSuchElementException:
            	df = df.append({'First Name': '' , 'Last Name': '', 'Message' : 'advertisement', 'Date': '', 'Profile':'none'}, ignore_index=True)
        except ElementNotVisibleException:
            return(df)
    return(df)
    

def get_messages(driver):
    select = driver.find_elements_by_css_selector
    select_one = driver.find_element_by_css_selector
    df = pd.DataFrame(columns=['First Name','Last Name','Message','Date','Profile'])
    #accessing the messages once logged in
    message_btn = select_one('span#messaging-tab-icon')
    message_btn.click()
    #get full message text, name and date of person
    messages_df = get_full_messages(driver,df)
    #getting url to messages
    add_message_urls_df = get_message_urls(driver,messages_df)
    return(add_message_urls_df)

def get_viewer_info(driver):
    driver.get('https://www.linkedin.com/')
    viewers = pd.DataFrame(columns=['First Name','Last Name','Profile'])
    select = driver.find_elements_by_css_selector
    select_one = driver.find_element_by_css_selector
    #go to profile page
    profile = select_one('li#profile-nav-item')
    profile.click()
    time.sleep(1)
    viewer_page = select_one('span.ember-view')
    viewer_page.click()
    time.sleep(2)
    
    #get the profile view information
    viewer_list = select('div.me-wvmp-viewer-card.display-flex.ember-view')
    first_names = []
    last_names = []
    profiles = []
    for viewer in viewer_list:
        try:
            viewer_url = viewer.find_element_by_css_selector('a').get_attribute('href')
            viewer_name = viewer.find_element_by_css_selector('span.me-wvmp-viewer-card__name-text').text.split(' ')
            first_names.append( viewer_name[0] )
            last_names.append( viewer_name[1] )
            profiles.append(viewer_url)
        except NoSuchElementException:
            pass
    viewers['First Name'] = first_names
    viewers['Last Name'] = last_names
    viewers['Profile'] = profiles

    return(viewers)



def run(login, password):
    chromedriver = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(chromedriver)
    sign_in(login, password, driver)
    #messages = get_messages(driver)
    messages = get_messages(driver)
    filename = f'{login}'+'.messages.csv'
    messages.to_csv(filename,index=False)

    #viewer information
    viewer_df = get_viewer_info(driver)
    viewerfilename = f'{login}'+'.viewerinfo.csv'
    viewer_df.to_csv(viewerfilename,index=False)

if __name__ == '__main__':
   print(len(sys.argv))
   run(sys.argv[1],sys.argv[2])

    