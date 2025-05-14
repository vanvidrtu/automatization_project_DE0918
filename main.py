from operator import contains
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

class Node():
    def __init__(self, value, key, link):
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        self.link = link
    
class BST:
    def __init__(self):
        self.root = None

    
    def create_tree(self, list):

        tree = BST()
        middle = len(list)//2
        root = Node(middle, list[middle].get('subject'), list[middle].get('link'))
        i = 1

        while (middle - i) >= 0 and (middle + i) < len(list):

            tree.insert_node(middle - i, list[middle - i].get('subject'), list[middle - i].get('link'))
            tree.insert_node(middle + i, list[middle + i].get('subject'), list[middle - i].get('link'))
            i += 1
        return tree
        
    

    def insert_node(self, value, key, link):

        new_node = Node(value, key, link)

        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root

        while (True):
           
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, root, value):

        if root is None:
            root = self.root
        
        if root.value == value:
            return root.link

        if value < root.value:
            return self.contains(root.left, value)
        else:
            return self.contains(root.right, value)
        
        


def connect_driver(url):
    
    
    driver = webdriver.Edge()
    driver.get(url)
    sleep(2)

    try:
        driver.find_element(By.ID, 'accept-choices' ).click()
    except:
        pass

    return driver 

def get_subjects(driver):

    global subjects 
    subjects = []

    find= driver.find_element(By.LINK_TEXT, 'Python Tutorial')
    find.click()
    sleep(5)

    options_menu = driver.find_element(By.ID, 'leftmenuinnerinner') 
    sleep(2)

    link = options_menu.find_elements(By.TAG_NAME, 'a' )
    sleep(2)


    for i in range(len(link) - 1):  
        
        if link[i].find_elements(By.XPATH, "ancestor::div[contains(@class, 'tut_overview overview_body')]"):
            continue

        
        name_parts = link[i].get_attribute('text').split(' ')
        if name_parts[0] == "Python":
            name_parts.pop(0)
            subject_name = ' '.join(name_parts)
            
        elif name_parts[0] != "Python":
            continue

        if "overview_header" in link[i].get_attribute("class"):
            sub_div = link[i+1].find_element(By.XPATH, "ancestor::div[contains(@class, 'tut_overview overview_body')]")

            if not sub_div:
                continue  

            sub_links = sub_div.find_elements(By.TAG_NAME, 'a')
            subject = dict(subject =subject_name, link = sub_subjects(sub_links))
            subjects.append(subject)

        else: 
            subject = dict(subject= subject_name, link = link[i].get_attribute('href'))
            subjects.append(subject)
        
        sleep(0.01)
    
    return subjects

    
def sub_subjects(sublinks):

    ssubjects = []
    
    for i in range(len(sublinks)-1):

       link = sublinks[i].get_attribute('href')
       name = sublinks[i].get_attribute('text')
       subsubject = dict(subject = name, link = link)
       ssubjects.append(subsubject)
    return(ssubjects)

def get_subject_index(sublinks, input):
    
    for i in range(len(sublinks)-1):
        name = sublinks[i].get('subject').casefold()
        
        if name == input:
            return i 
        elif name in input:
            return i 
    return -1

def sort_subjects(subject_list):
    sorted_list = []
    sorted_list = sorted(subject_list, key=lambda x: x['subject'])
    return sorted_list

def subject_list(link):
    tree = BST()
    driver = connect_driver(link)
    subject_list = get_subjects(driver)
    driver.quit()
    return sort_subjects(subject_list)

def get_link(input, subjects):
    tree = BST()
    subject_tree = tree.create_tree(subjects)
    index = get_subject_index(subjects, input)
    link = subject_tree.contains(subject_tree.root ,index)
    return link

def get_webbody(driver):
    body_list = []
    i = 0
  
    page = BeautifulSoup(driver.page_source, 'html.parser')
    body = page.find('div', {'id': 'main'})
    
    
    for  el  in body.descendants:
        
        if el.name in ['h1', 'h2', 'h3', 'h4', 'p', 'li', 'pre', 'a']:
            text = el.get_text(strip=True)

            if el.name == 'a':
                classes = el.get('class', [])

                if 'w3-btn' in classes and 'w3-margin-bottom' in classes:
                    buttons = driver.find_elements(By.XPATH, f"//a[contains(@class, 'w3-btn w3-margin-bottom')]")
                    buttons[i].click()
                    code = read_example_web(buttons[i].get_attribute('href'))
                    body_list.append(code)
                    sleep(0.1)
                    i += 1
                   
                elif 'ga-featured' in classes and 'ga-youtube' in classes:
                    body_list.append(f"[VIDEO_LINK] {el.get('href')}")
                
            elif text:
                body_list.append(f"[{el.name.upper()}] {text}")
                
                
    return body_list


def read_example_web(link):

    code_list = []
    code_list.append("[CODE]")

    driver = connect_driver(link)
    sleep(0.2)

    code_container = driver.find_element(By.CLASS_NAME, "CodeMirror-code")
    lines = code_container.find_elements(By.CLASS_NAME, "CodeMirror-line")

    
    for line in lines:
        line_text = line.text.strip()
        if line_text:
            code_list.append(line_text)
    
    driver.quit()
    return code_list
    
def write_to_file(body_list):

    with open('Python_cheat_sheat.txt', 'w') as file:
        file.write(" "+"Python Cheat Sheet\n\n")
        
        for line in body_list:

            if isinstance(line, list):
                tag_name = line[0]
                line.pop(0)
            else:
                parts = line.split(" ")
                tag_name = parts[0]
                wr_line = ' '.join(parts[1:])
                print(wr_line)
        

            match tag_name:
                case "[CODE]":
                    for wr_line in line:
                        write_formatted(file, wr_line, 7, 0)
                case "[VIDEO_LINK]":
                    write_formatted(file, wr_line, 7, 0)
                case "[H1]":
                    write_formatted(file, wr_line, 2, 2)
                case "[H2]":
                    write_formatted(file, wr_line, 4, 1)
                case "[H3]":
                    write_formatted(file, wr_line, 5, 1)
                case "[H4]":
                    write_formatted(file, wr_line, 5, 1)
                case "[P]":
                    write_formatted(file, wr_line, 6, 0)
                case "[LI]":
                    write_formatted(file, '* '+ wr_line, 6, 0)    
                case _:
                    pass
    return file

def write_formatted(file, text, indent, newline):
    file.write(" " * indent +"\n" * (newline) + text + "\n" * (newline+1))
    return

def list_names(list):
    names = []
    for i in range(len(list)-1):
        name = list[i].get('subject')
        print(name)
        names.append(name)
    
    return names 
def get_sub_link(list, input):
    for i in range(len(list)-1):
        name = list[i].get('subject').casefold()
        link= list[i].get('link')
        if input == name:
            return link
    
    



def main():
    try: 
        driver = connect_driver('https://www.w3schools.com/python/default.asp')
        subjects = get_subjects(driver)
        list_names(subjects)
    except:
        print('Driver not found')
        return
    driver.quit()

    run_code = True
    while run_code: 
        print("Ievadi Python tēmu, par kuru vēlies noskaidrot informāciju,, vai 'exit' :")
        user_input = input("Ievadi tēmas nosaukumu : ").strip().casefold()

        match user_input:
            case 'exit':
                run_code = False
                
            case _:
                link = get_link(user_input, subjects)
                if link == -1:
                    print('Tēma nav atrasta')
                    continue
                elif isinstance(link, list):
                    names = list_names(link)
                    user_input = input('Izvēlies apakšmoduli šajai tēmai:').strip().casefold()
                    link = get_sub_link(link, user_input)
                    

                driver = connect_driver(link)
                body_list = get_webbody(driver)
                driver.quit()
                file = write_to_file(body_list)
                file.close()
        
main()


    