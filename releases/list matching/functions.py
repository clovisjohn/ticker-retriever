def coingecko_list():
    '''
return the latest coingecko tokens list
    '''
    f = requests.get("https://api.coingecko.com/api/v3/coins/list")
    data = json.loads(f.text)
    
    return [i["symbol"].upper() for i in data] + [j["name"] for j in data]


def msg_list(m):
    '''
take a string as input, the string is the chat history file path
return list of messages
    '''
    with open(m, encoding="utf8") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        
    
    l=[]
    
    for i in soup.find_all('div', class_='text'):
        temp=i.get_text()
        temp=re.sub("\\n","",temp)
        temp=temp.rstrip()
        l.append(temp)
        
    return " ".join(l)
