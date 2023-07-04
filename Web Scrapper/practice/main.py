from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as website:
    content = website.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)        #-----> printing title
# print(soup.title.string) #-----> to get only string
# print(soup.title.name)   #-----> to get the name 
# print(soup.prettify())   #-----> printing whole doc
# print(soup.li)           #-----> printing first li item
# print(soup.p)            #-----> printing first para
# print(soup.a)            #-----> printing first anchor

all_anchor_tags = soup.find_all(name="a")  #find_all() to print every item in the doc
# print(all_anchor_tags)
for tag in all_anchor_tags:
    # print(tag.getText())  # ----> to get the text 
    print(tag.get("href"))  # ----> for getting a specific attribute


# this is how specific name and id can be specified
heading = soup.find(name="h1", id="name")
print(heading)

# this is how specific name and class can be specified (underscore taaki it doesnt clash with class of python)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)


# how to drill down to a particular element in a website?
# ans ---> same as how we do in css
name = soup.select_one("#name")   # ----> for one
print(name)

heading = soup.select(".heading")  # ----> for more than one
print(heading)