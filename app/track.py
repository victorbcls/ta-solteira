
import re
from time import sleep
import emoji
from psutil import users


def find_by_mention(username, driver):
    # driver.get(f'https://www.instagram.com/{username}')
    sleep(3)
    bio = driver.find_element(
        'xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[3]')
    most_possible_partner = ''
    has_user = False
    possible_partner = re.findall(r'[@]\w+', bio.text)
    mutual = False
    for person in possible_partner:
        has_user = True
        person = person.replace('@', '')
        driver.get(f'https://www.instagram.com/{person}')
        sleep(3)
        bio = driver.find_element(
            'xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[3]')
        possible_partner = re.findall(r'[@]\w+', bio.text)
        if '@'+username in possible_partner:
            most_possible_partner = person
            mutual = True
        else:
            most_possible_partner = person

    return {'has_user': has_user,
            'mutual': mutual,
            'partner': most_possible_partner}


def has_ring(username, driver):
    driver.get(f'https://www.instagram.com/{username}')
    sleep(3)
    bio = driver.find_element(
        'xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[3]')
    if emoji.emojize(':ring:') in bio.text:
        return {'has_ring': True}
    else:
        return {'has_ring': False}
