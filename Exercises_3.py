# U15.3 Quiz: Add to index
print("# U15.3 Quiz: Add to index")

index = []

def add_to_index(index,keyword,url):
    for e in index:
        if e[0] == keyword:
            if url not in e[1]:  # added in U16.5 Quiz: Improving the Index
                e[1].append(url)
            return  # it means get out of the function(procedure). 'break' here would mean go out of 'for' loop
    index.append([keyword, [url]])

add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'standing','http://ert.org')
print(index)
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']],
#>>> ['computing', ['http://acm.org']]]


# U15.4 Quiz: Lookup
print("# U15.4 Quiz: Lookup")

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
    return []

print(lookup(index,'udacity'))
#>>> ['http://udacity.com','http://npr.org']

# U15.6 Quiz: Add page to index
print("# U15.6 Quiz: Add page to index")
index = []
def add_page_to_index(index,url,content):
    f = content.split()
    for e in f:
        add_to_index(index, e, url)

add_page_to_index(index, 'fake.text', "This is a test")
print(index)
# >>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
# >>> ['test',['fake.text']]]


# U15.7 Quiz: Finishing the web crawler
print("# U15.7 Quiz: Finishing the web crawler")

# def crawl_web(seed):
#     tocrawl = [seed]
#     crawled = []
#     index = []
#     while tocrawl:
#         page = tocrawl.pop()
#         if page not in crawled:
#             content = get_page(page)
#             add_page_to_index(index, page, content)
#             union(tocrawl, get_all_links(content))
#             crawled.append(page)
#     return index


# U16.4 Quiz: Better splitting
print("# U16.4 Quiz: Better splitting")
# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

# moj
def split_string(source,splitlist):
    f = source.split(splitlist[0])
    for e in splitlist:
        n = 0
        while n < len(f):
            if f[n] == e or f[n] == '':
                f.remove(f[n])
                n = n - 1
            while e in (f[n]):
                if f[n][0] == e:
                    f[n] = f[n][1:]
                    if f[n] == '':
                        f.remove(f[n])
                        n = n - 1
                if f[n][len(f[n]) - 1] == e:
                    f[n] = f[n][:-1]
                    if f[n] == '':
                        f.remove(f[n])
                        n = n - 1
                if f[n][0] != e or f[n][len(f[n]) - 1] != e:
                    break
            r = []
            if e in f[n]:
                r = f[n].split(e)
                if f.index(f[n]) < len(f) - 1:
                    f = f[:f.index(f[n])] + r + f[f.index(f[n + 1]):]
                else:
                    f = f[:f.index(f[n])] + r
            n += 1
    return f

# njihov:
def split_string(source,splitlist):
    output = []
    atsplit = True  # At a split point
    for char in source:  # iterate through string by each letter
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                # add character to last word
                output[-1] = output[-1] + char
    return output

# Slobin:
def split_string(source,splitlist):
    output = [source]
    result = []
    for s in splitlist:
        for element in output:
            result.extend(element.split(s))
            while '' in result:
                result.remove('')
        output = result
        result = []
    return output


out = split_string("This is a test-of the,string separation-code!", ", !-")
print(out)
# >>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print(out)
# >>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print(out)
# >>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']


# U16.6 Quiz: Counting Clicks
print("# U16.6 Quiz: Counting Clicks")


def record_user_click(index, keyword, url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1] + 1

def add_to_index(index,keyword,url):
    # format of index: [[keyword, [[url, count], [url, count],...[url, count],...]
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return
            entry[1].append([url, 0])
            return
    # not found, add a new keyword to index
    index.append([keyword, [[url, 0]]])

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return '''<html> <body> This is a test page for learning to crawl!
<p> It is a good idea to
<a href="http://www.udacity.com/cs101x/crawling.html">
learn to crawl</a> before you try to
<a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
<a href="http://www.udacity.com/cs101x/flying.html">fly</a>.</p></body></html>'''

        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return '''<html> <body> I have not learned to crawl yet, but I am
quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.
</body> </html>'''

        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '''<html> <body> I cant get enough
<a href="http://www.udacity.com/cs101x/index.html">crawling</a>!</body></html>'''

        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '<html><body>The magic words are Squeamish Ossifrage!</body></html>'
    except:
        return ""
    return ""

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

#Here is an example showing a sequence of interactions:
index = crawl_web('http://www.udacity.com/cs101x/index.html')
print(lookup(index, 'good'))
#>>> [['http://www.udacity.com/cs101x/index.html', 0],
#>>> ['http://www.udacity.com/cs101x/crawling.html', 0]]
record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
print(lookup(index, 'good'))
#>>> [['http://www.udacity.com/cs101x/index.html', 0],
#>>> ['http://www.udacity.com/cs101x/crawling.html', 1]]


# U17.1 Quiz: Word Count
print("# U17.1 Quiz: Word Count")

def count_words(s):
    f = s.split()
    return len(f)


passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print(count_words(passage))
#>>>56


# U17.3 Quiz: Converting Seconds
print("# U17.3 Quiz: Converting Seconds")


def convert_seconds(sec):
    ss = sec % 60
    ms = int(sec / 60)
    hs = int(sec/60/60)
    if ms >= 60:
        hs = int(ms / 60)
        ms = ms % 60
    if ss == 1:
        s = str(ss) + ' second'
    else:
        s = str(ss) + ' seconds'
    if ms == 1:
        m = str(ms) + ' minute'
    else:
        m = str(ms) + ' minutes'
    if hs == 1:
        h = str(hs) + ' hour'
    else:
        h = str(hs) + ' hours'
    return h + ', ' + m + ', ' + s


print(convert_seconds(3661))
#>>> 1 hour, 1 minute, 1 second

print(convert_seconds(7325))
#>>> 2 hours, 2 minutes, 5 seconds

print(convert_seconds(7261.7))
#>>> 2 hours, 1 minute, 1.7 seconds

