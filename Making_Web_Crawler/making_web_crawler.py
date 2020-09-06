# unit 1

# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url',
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
# print(start_link)
double_quote = page.find('"', start_link)
# print(double_quote)
double_quote_2 = page.find('"', double_quote + 1)
# print(double_quote_2)
url = page[double_quote + 1:double_quote_2]
print(url)

# unit 2(lesson 5)

# defining the procedure:
# L5.6
def get_next_target(s):
    start_link = s.find('<a href=')
    start_quote = s.find('"', start_link)
    end_quote = s.find('"', start_quote + 1)
    url = s[start_quote + 1:end_quote]
    return url, end_quote

# L5.29 no links, (to get next link on a page)
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:  # if there are no links on the page
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# L5.30
def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

# L11.35 to get all links on one page
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:  # if we found valid url
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

# L11.41
#(their procedure)
def get_page(url):
    # This is a simulated get_page procedure so that you can test your
    # code on two pages "http://xkcd.com/353" and "http://xkcd.com/554".
    # A procedure which actually grabs a page from the web will be
    # introduced in unit 4.
    try:
        if url == "http://xkcd.com/353":
            return  '<?xml version="1.0" encoding="utf-8" ?><?xml-stylesheet href="http://imgs.xkcd.com/s/c40a9f8.css" type="text/css" media="screen" ?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"><html xmlns="http://www.w3.org/1999/xhtml"> <head> <title>xkcd: Python</title> <link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/c40a9f8.css" media="screen" title="Default" /> <!--[if IE]><link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/ecbbecc.css" media="screen" title="Default" /><![endif]--> <link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="/atom.xml" /> <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="/rss.xml" /> <link rel="icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /> <link rel="shortcut icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /> </head> <body> <div id="container"> <div id="topContainer"> <div id="topLeft" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s">\t<ul> <li><a href="http://xkcd.com/554"">Archive</a><br /></li>\t <li><a href="http://blag.xkcd.com/">News/Blag</a><br /></li> <li><a href="http://store.xkcd.com/">Store</a><br /></li> <li><a href="/about/">About</a><br /></li> <li><a href="http://forums.xkcd.com/">Forums</a><br /></li> </ul> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> <div id="topRight" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <div id="topRightContainer"> <div id="logo"> <a href="/"><img src="http://imgs.xkcd.com/s/9be30a7.png" alt="xkcd.com logo" height="83" width="185"/></a> <h2><br />A webcomic of romance,<br/> sarcasm, math, and language.</h2> <div class="clearleft"></div> <br />XKCD updates every Monday, Wednesday, and Friday. </div> </div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> </div> <div id="contentContainer"> <div id="middleContent" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"><h1>Python</h1><br/><br /><div class="menuCont"> <ul> <li><a href="/1/">|&lt;</a></li> <li><a href="/352/" accesskey="p">&lt; Prev</a></li> <li><a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_t">Random</a></li> <li><a href="/354/" accesskey="n">Next &gt;</a></li> <li><a href="/">&gt;|</a></li> </ul></div><br/><br/><img src="http://imgs.xkcd.com/comics/python.png" title="I wrote 20 short programs in Python yesterday. It was wonderful. Perl, Im leaving you." alt="Python" /><br/><br/><div class="menuCont"> <ul> <li><a href="/1/">|&lt;</a></li> <li><a href="/352/" accesskey="p">&lt; Prev</a></li> <li><a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_b">Random</a></li> <li><a href="/354/" accesskey="n">Next &gt;</a></li> <li><a href="/">&gt;|</a></li> </ul></div><h3>Permanent link to this comic: http://xkcd.com/353/</h3><h3>Image URL (for hotlinking/embedding): http://imgs.xkcd.com/comics/python.png</h3><div id="transcript" style="display: none">[[ Guy 1 is talking to Guy 2, who is floating in the sky ]]Guy 1: You39;re flying! How?Guy 2: Python!Guy 2: I learned it last night! Everything is so simple!Guy 2: Hello world is just 39;print &quot;Hello, World!&quot; 39;Guy 1: I dunno... Dynamic typing? Whitespace?Guy 2: Come join us! Programming is fun again! It39;s a whole new world up here!Guy 1: But how are you flying?Guy 2: I just typed 39;import antigravity39;Guy 1: That39;s it?Guy 2: ...I also sampled everything in the medicine cabinet for comparison.Guy 2: But i think this is the python.{{ I wrote 20 short programs in Python yesterday. It was wonderful. Perl, I39;m leaving you. }}</div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> <div id="middleFooter" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <img src="http://imgs.xkcd.com/s/a899e84.jpg" width="520" height="100" alt="Selected Comics" usemap=" comicmap" /> <map name="comicmap"> <area shape="rect" coords="0,0,100,100" href="/150/" alt="Grownups" /> <area shape="rect" coords="104,0,204,100" href="/730/" alt="Circuit Diagram" /> <area shape="rect" coords="208,0,308,100" href="/162/" alt="Angular Momentum" /> <area shape="rect" coords="312,0,412,100" href="/688/" alt="Self-Description" /> <area shape="rect" coords="416,0,520,100" href="/556/" alt="Alternative Energy Revolution" /> </map><br/><br />Search comic titles and transcripts:<br /><script type="text/javascript" src="//www.google.com/jsapi"></script><script type="text/javascript"> google.load(\"search\", \"1\"); google.setOnLoadCallback(function() { google.search.CustomSearchControl.attachAutoCompletion( \"012652707207066138651:zudjtuwe28q\", document.getElementById(\"q\"), \"cse-search-box\"); });</script><form action="//www.google.com/cse" id="cse-search-box"> <div> <input type="hidden" name="cx" value="012652707207066138651:zudjtuwe28q" /> <input type="hidden" name="ie" value="UTF-8" /> <input type="text" name="q" id="q" autocomplete="off" size="31" /> <input type="submit" name="sa" value="Search" /> </div></form><script type="text/javascript" src="//www.google.com/cse/brand?form=cse-search-box&lang=en"></script><a href="/rss.xml">RSS Feed</a> - <a href="/atom.xml">Atom Feed</a><br /> <br/> <div id="comicLinks"> Comics I enjoy:<br/> <a href="http://www.qwantz.com">Dinosaur Comics</a>, <a href="http://www.asofterworld.com">A Softer World</a>, <a href="http://pbfcomics.com/">Perry Bible Fellowship</a>, <a href="http://www.boltcity.com/copper/">Copper</a>, <a href="http://questionablecontent.net/">Questionable Content</a>, <a href="http://achewood.com/">Achewood</a>, <a href="http://wondermark.com/">Wondermark</a>, <a href="http://thisisindexed.com/">Indexed</a>, <a href="http://www.buttercupfestival.com/buttercupfestival.htm">Buttercup Festival</a> </div> <br/> Warning: this comic occasionally contains strong language (which may be unsuitable for children), unusual humor (which may be unsuitable for adults), and advanced mathematics (which may be unsuitable for liberal-arts majors).<br/> <br/> <h4>We did not invent the algorithm. The algorithm consistently finds Jesus. The algorithm killed Jeeves. <br />The algorithm is banned in China. The algorithm is from Jersey. The algorithm constantly finds Jesus.<br />This is not the algorithm. This is close.</h4><br/> <div class="line"></div> <br/> <div id="licenseText"> <!-- <a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/"><img alt="Creative Commons License" style="border:none" src="http://imgs.xkcd.com/static/somerights20.png" /></a><br/> --> This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/">Creative Commons Attribution-NonCommercial 2.5 License</a>.<!-- <rdf:RDF xmlns="http://web.resource.org/cc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns "><Work rdf:about=""><dc:creator>Randall Munroe</dc:creator><dcterms:rightsHolder>Randall Munroe</dcterms:rightsHolder><dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /><dc:source rdf:resource="http://www.xkcd.com/"/><license rdf:resource="http://creativecommons.org/licenses/by-nc/2.5/" /></Work><License rdf:about="http://creativecommons.org/licenses/by-nc/2.5/"><permits rdf:resource="http://web.resource.org/cc/Reproduction" /><permits rdf:resource="http://web.resource.org/cc/Distribution" /><requires rdf:resource="http://web.resource.org/cc/Notice" /><requires rdf:resource="http://web.resource.org/cc/Attribution" /><prohibits rdf:resource="http://web.resource.org/cc/CommercialUse" /><permits rdf:resource="http://web.resource.org/cc/DerivativeWorks" /></License></rdf:RDF> --> <br/> This means you\"re free to copy and share these comics (but not to sell them). <a href="/license.html">More details</a>.<br/> </div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> </div> </div> </body></html> '
        elif url == "http://xkcd.com/554":
            return  '<?xml version="1.0" encoding="utf-8" ?> <?xml-stylesheet href="http://imgs.xkcd.com/s/c40a9f8.css" type="text/css" media="screen" ?> <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"> <html xmlns="http://www.w3.org/1999/xhtml"> <head> <title>xkcd: Not Enough Work</title> <link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/c40a9f8.css" media="screen" title="Default" /> <!--[if IE]><link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/ecbbecc.css" media="screen" title="Default" /><![endif]--> <link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="/atom.xml" /> <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="/rss.xml" /> <link rel="icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /> <link rel="shortcut icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /> </head> <body> <div id="container"> <div id="topContainer"> <div id="topLeft" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <ul> <li><a href="/archive/">Archive</a><br /></li> <li><a href="http://blag.xkcd.com/">News/Blag</a><br /></li> <li><a href="http://store.xkcd.com/">Store</a><br /></li> <li><a href="/about/">About</a><br /></li> <li><a href="http://forums.xkcd.com/">Forums</a><br /></li> </ul> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> <div id="topRight" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <div id="topRightContainer"> <div id="logo"> <a href="/"><img src="http://imgs.xkcd.com/s/9be30a7.png" alt="xkcd.com logo" height="83" width="185"/></a> <h2><br />A webcomic of romance,<br/> sarcasm, math, and language.</h2> <div class="clearleft"></div> XKCD updates every Monday, Wednesday, and Friday. <br /> Blag: Remember geohashing? <a href="http://blog.xkcd.com/2012/02/27/geohashing-2/">Something pretty cool</a> happened Sunday. </div> </div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> </div> <div id="contentContainer"> <div id="middleContent" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <h1>Not Enough Work</h1><br/> <br /> <div class="menuCont"> <ul> <li><a href="/1/">|&lt;</a></li> <li><a href="/553/" accesskey="p">&lt; Prev</a></li> <li><a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_t">Random</a></li> <li><a href="/555/" accesskey="n">Next &gt;</a></li> <li><a href="/">&gt;|</a></li> </ul> </div> <br/> <br/> <img src="http://imgs.xkcd.com/comics/not_enough_work.png" title="It39;s even harder if you39;re an asshole who pronounces &lt;&gt; brackets." alt="Not Enough Work" /><br/> <br/> <div class="menuCont"> <ul> <li><a href="/1/">|&lt;</a></li> <li><a href="/553/" accesskey="p">&lt; Prev</a></li> <li><a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_b">Random</a></li> <li><a href="/555/" accesskey="n">Next &gt;</a></li> <li><a href="/">&gt;|</a></li> </ul> </div> <h3>Permanent link to this comic: http://xkcd.com/554/</h3> <h3>Image URL (for hotlinking/embedding): http://imgs.xkcd.com/comics/not_enough_work.png</h3> <div id="transcript" style="display: none">Narration: Signs your coders don39;t have enough work to do: [[A man sitting at his workstation; a female co-worker behind him]] Man: I39;m almost up to my old typing speed in dvorak [[Two men standing by a server rack]] Man  1: Our servers now support gopher. Man  1: Just in case. [[A woman standing near her workstation speaking to a male co-worker]] Woman: Our pages are now HTML, XHTML-STRICT, and haiku-compliant Man: Haiku? Woman: &lt;div class=&quot;main&quot;&gt; Woman: &lt;span id=&quot;marquee&quot;&gt; Woman: Blog!&lt; span&gt;&lt; div&gt; [[A woman sitting at her workstation]] Woman: Hey! Have you guys seen this webcomic? {{title text: It39;s even harder if you39;re an asshole who pronounces &lt;&gt; brackets.}}</div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> <div id="middleFooter" class="dialog"> <div class="hd"><div class="c"></div></div> <div class="bd"> <div class="c"> <div class="s"> <img src="http://imgs.xkcd.com/s/a899e84.jpg" width="520" height="100" alt="Selected Comics" usemap=" comicmap" /> <map name="comicmap"> <area shape="rect" coords="0,0,100,100" href="/150/" alt="Grownups" /> <area shape="rect" coords="104,0,204,100" href="/730/" alt="Circuit Diagram" /> <area shape="rect" coords="208,0,308,100" href="/162/" alt="Angular Momentum" /> <area shape="rect" coords="312,0,412,100" href="/688/" alt="Self-Description" /> <area shape="rect" coords="416,0,520,100" href="/556/" alt="Alternative Energy Revolution" /> </map><br/><br /> Search comic titles and transcripts:<br /> <script type="text/javascript" src="//www.google.com/jsapi"></script> <script type="text/javascript"> google.load("search", "1"); google.search.CustomSearchControl.attachAutoCompletion( "012652707207066138651:zudjtuwe28q", document.getElementById("q"), "cse-search-box"); }); </script> <form action="//www.google.com/cse" id="cse-search-box"> <div> <input type="hidden" name="cx" value="012652707207066138651:zudjtuwe28q" /> <input type="hidden" name="ie" value="UTF-8" /> <input type="text" name="q" id="q" autocomplete="off" size="31" /> <input type="submit" name="sa" value="Search" /> </div> </form> <script type="text/javascript" src="//www.google.com/cse/brand?form=cse-search-box&lang=en"></script> <a href="/rss.xml">RSS Feed</a> - <a href="/atom.xml">Atom Feed</a> <br /> <br/> <div id="comicLinks"> Comics I enjoy:<br/> <a href="http://threewordphrase.com/">Three Word Phrase</a>, <a href="http://oglaf.com/">Oglaf</a> (nsfw), <a href="http://www.smbc-comics.com/">SMBC</a>, <a href="http://www.qwantz.com">Dinosaur Comics</a>, <a href="http://www.asofterworld.com">A Softer World</a>, <a href="http://buttersafe.com/">Buttersafe</a>, <a href="http://pbfcomics.com/">Perry Bible Fellowship</a>, <a href="http://questionablecontent.net/">Questionable Content</a>, <a href="http://www.buttercupfestival.com/buttercupfestival.htm">Buttercup Festival</a> </div> <br/> Warning: this comic occasionally contains strong language (which may be unsuitable for children), unusual humor (which may be unsuitable for adults), and advanced mathematics (which may be unsuitable for liberal-arts majors).<br/> <br/> <h4>We did not invent the algorithm. The algorithm consistently finds Jesus. The algorithm killed Jeeves. <br />The algorithm is banned in China. The algorithm is from Jersey. The algorithm constantly finds Jesus.<br />This is not the algorithm. This is close.</h4><br/> <div class="line"></div> <br/> <div id="licenseText"> <!-- <a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/"><img alt="Creative Commons License" style="border:none" src="http://imgs.xkcd.com/static/somerights20.png" /></a><br/> --> This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/">Creative Commons Attribution-NonCommercial 2.5 License</a>. <!-- <rdf:RDF xmlns="http://web.resource.org/cc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns "><Work rdf:about=""><dc:creator>Randall Munroe</dc:creator><dcterms:rightsHolder>Randall Munroe</dcterms:rightsHolder><dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /><dc:source rdf:resource="http://www.xkcd.com/"/><license rdf:resource="http://creativecommons.org/licenses/by-nc/2.5/" /></Work><License rdf:about="http://creativecommons.org/licenses/by-nc/2.5/"><permits rdf:resource="http://web.resource.org/cc/Reproduction" /><permits rdf:resource="http://web.resource.org/cc/Distribution" /><requires rdf:resource="http://web.resource.org/cc/Notice" /><requires rdf:resource="http://web.resource.org/cc/Attribution" /><prohibits rdf:resource="http://web.resource.org/cc/CommercialUse" /><permits rdf:resource="http://web.resource.org/cc/DerivativeWorks" /></License></rdf:RDF> --> <br/> This means you"re free to copy and share these comics (but not to sell them). <a href="/license.html">More details</a>.<br/> </div> </div> </div> </div> <div class="ft"><div class="c"></div></div> </div> </div> </div> </body> </html> '
    except:
        return ""
    return ""

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

# moj:
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            crawled.append(page)
            tocrawl += get_all_links(get_page(page))
    return crawled

# njihov (to avoid duplication in tocrawl, use union procedure:
def crawl_web(seed):  # start page
    tocrawl = [seed]  # list of pages left to crawl
    crawled = []  # to keep track of all the pages that we crawled
    while tocrawl:  # if the list is not empty
        page = tocrawl.pop()  # depth-first search(we will always follow the last link on a page
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))  # add all the links on the page that we found to tocrawl
            crawled.append(page)
    return crawled

p = "https://www.w3schools.com/"
print(crawl_web(p))
q = "https://udacity.github.io/cs101x/index.html"
print(crawl_web(q))

# U12.6 Max Pages
#moj
def crawl_web(seed, max_pages):
    tocrawl = [seed]
    i = 0
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
        i = i + 1
        if i == max_pages:
            break
    return crawled

#njihov
def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []  # len(crawled) is length of crawled
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled


# U12.7 Max Depth
def crawl_web(seed, max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []  #  it keeps track of the next level of links
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled


# U15.3 Quiz: Add to index (add new entry(keyword) to the index)
index = []
def add_to_index(index,keyword,url):  # index we want to add new keyword to, keyword(a string), url (a string where keyword appears)
    for entry in index:
        if entry[0] == keyword:
            if url not in entry[1]:  # added in U16.5 Quiz: Improving the Index
                entry[1].append(url)
            return  # we have added url where it belongs and we can finish
    # not found, add a new entry
    index.append([keyword, [url]])  # if keyword does not exist in the index


# U15.4 Quiz: Lookup
def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]  # returns list of urls associated with that keyword
    return None

# U15.6 Quiz: Add page to index
# the result should be updating the index
# to include all word occurences found
# in the page content by adding
# the url to the word's associated url list

# index = []
def add_page_to_index(index,url,content):  # index, url(the location of the page where the content came from), content (the entire text of the page at the location where url is)
    words = content.split()  # use split method to divide the content into its component words and store that in the words variable
    for word in words:  # go through all the words adding each word into the index
        add_to_index(index, word, url)  # we don't have to return anything, the point is to modify index


# U15.7 Quiz: Finishing the web crawler  (changes)
# we need to update the index
# to reflect all the words that are
# found on the page that we've crawled

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []  # we are updating the index
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)  # we store the content of the page in that variable
            add_page_to_index(index, page, content)  # index, page(url that identifies location), content of that url
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index  # instaed of returning the crawled we want to return the index which is index of all the content we find starting from the seed


# U16.6 Quiz: Counting Clicks
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




#Here is an example showing a sequence of interactions:
index = crawl_web('http://www.udacity.com/cs101x/index.html')
print(lookup(index, 'good'))
#>>> [['http://www.udacity.com/cs101x/index.html', 0],
#>>> ['http://www.udacity.com/cs101x/crawling.html', 0]]
record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
print(lookup(index, 'good'))
#>>> [['http://www.udacity.com/cs101x/index.html', 0],
#>>> ['http://www.udacity.com/cs101x/crawling.html', 1]]


# U18.33 Quiz: Modifying the search engine
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}  # now we start with an empty dictionary
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_to_index(index,keyword,url):
    if keyword in index:  # now index is a dictionary, so instead of looping we can just check if the word is in hashtable
        index[keyword].append(url)  # it appends url to the value list of keyword
    else:
        # not found, add a new keyword to index
        index[keyword] = [url]


# U18.34 Quiz: Changing Lookup
def lookup(index, keyword):
    if keyword in index:  # index is a dictionary, no need to loop through
        return index[keyword]
    return None


# U22.24 Quiz: Implementing Urank
# Modify the crawl_web procedure so that instead of just returning the
# index, it returns an index and a graph. The graph should be a
# Dictionary where the key:value entries are:

#  url: [list of pages url links to]

def crawl_web(seed): # returns index, graph of outlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>:[list of pages it links to]
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)  # both the graph building and the tocrawl list depend on knowing all the links so we are going to create a new variable
            graph[page] = outlinks  # we update the graph with the page we are crawling (that is the key for the entry) and the value is list of the outgoing links from that page
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph  # we return both the index and a graph


# U22.28 Quiz: Finishing Urank
def compute_ranks(graph):
    d = 0.8  # damping factor
    numloops = 10  # we are computing the value of rank at some time step. the number of times we go through that is going to determine accuracy of our ranks

    ranks = {}  # a dictionary giving for each url the Urank
    npages = len(graph)  # the number of pages we can get from the graph (a dictionary of nodes(pages)) and len(graph) is the number of pages we crawled
    for page in graph:  # we go through the pages in graph
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):  # loop that is going to go through the number of times of numloops
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages  # each time it goes through the loop it updates the newranks based on this formula using the old ranks
            for node in graph:  # we want to go through all the pages in the graph (call them nodes)
                if page in graph[node]:  # if page is in the list graph[node] it means that node links to page and it means that we should add to newrank based on the rank of this node
                    newrank = newrank + d * (ranks[node] / len(graph[node]))  # we are going to add to newrank and the new value is going to be the old value we are summing into the value of newrank.
            newranks[page] = newrank                                          # we are going to multiply by d. And the value we are going to use here is the page rank of the node(it is the node that links to the node in the upper line and we want ot divide that by the number of outlinks from that page
        ranks = newranks  # at the end of the loop variable ranks holds what is previously newranks
    return ranks


# U23.5 Quiz: Feeling Lucky
# Feeling Lucky

# In Unit 6, we implemented a page ranking algorithm, but didn't finish the final
# step of using it to improve our search results. For this question, you will use
# the page rankings to produce the best output for a given query.

# Define a procedure, lucky_search, that takes as input an index, a ranks
# dictionary (the result of compute_ranks), and a keyword, and returns the one
# URL most likely to be the best site for that keyword. If the keyword does not
# appear in the index, lucky_search should return None.

def lucky_search(index, ranks, keyword):  # index(a hashtable of all the keywords in the pages in which they appear), ranks( which ranks each page based on the Urank algorithm), keyword we are searchin for
    pages = lookup(index, keyword)
    if not pages:
        return None
    best_page = pages[0]  # best page is the first one
    for candidate in pages:
        if ranks[candidate] > ranks[best_page]:
            best_page = candidate
    return best_page  # highest ranking page with that keyword

