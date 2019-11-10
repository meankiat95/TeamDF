from flashtext.keyword import KeywordProcessor
from flashtext.keyword import KeywordProcessor
from PIL.ExifTags import TAGS
from PIL import Image


def getNumberofRow():
    with open("hello.csv") as csvfile:
        row_count = sum(1 for row in csvfile)  # fileObject is your csv.reader
        return row_count


def percentage1(a,b):
    try:
        ans=float(b)/float(a)
        ans=ans*100
    except:
        return 0
    else:
        return ans
def classification(textSplit):
    keyword_cyber_security_risk = ["ad fraud", "cyberattack", "malware", "botnets", "CnC", "Command and Control",
                                   "compromised accounts", \
                                   "hacking", "key logging", "phishing", "spyware", "worm", "trojan", "RAT", "APT",
                                   "adware", "fileless attack", "cryptocurrency mining", \
                                   "spam", "ransomware", "denial-of-service", "sql injection", "man-in-the-middle",
                                   "compromised pcs", "spam site", "malicious payload", "apt", \
                                   "advanced persistent threat", "spoofing", "virus", "slowloris", "xss",
                                   "cross-site scripting", "exploit", "vulnerability", "cve", "day zero","backdoor","blackhat"
                                   ,"bruteForce","botNet","cracking","forensics","exploit","scanning","enumeration","reconnaisance",""
                                   "adware", "autorun worms", "advanced persistent threats", "attack vector", "backdoor", "blended attack",
                                   "botnet", "browser hijacker", "brute force attack", "clickjacking", "command and control servers",
                                   "content spoofing", "cross site scripting", "xss" "xsrf", "data theft", "denial of service attack", "dictionary attack",
                                   "drive-by download", "email spoofing", "email virus", "exploit", "form grabber",
                                   "identity theft", "insider attack", "keylogger",
                                   "likejacking", "malware", "mman in the middle" "ransomware", "rootkit", "spam",
                                   "spyware", "SQL injection", "wabbit", "website spoofing "
                                   ,"ip","tcp","router","network","cisco", ""]

    Adult_Content = ["pornography", "violence", "blood", "gore", "sex", "nudity", "erotic", "hardcore", "fetish",
                     "intercourse", "explicit content", "hentai", "masturbation", "dick", 'pussy', "penis", "vagina", "anus",
                     'boobs', 'porn', 'xxx']

    keyword_Aggressive = ["attacking", "fighting", "invading", "assailing", "threaten", "slashing", "beating", "destroy",
                          "destruction", 'assault']

    Keyword_arts = ["painting", "drawing", "ceramics", "pottery", "photography", "sculpture", "dance"]

    keyword_automotive = ['alfa romeo', 'aston martin', 'audi', 'bentley', 'bmw', 'bugatti', 'chevrolet', 'chrysler',
                          'citroen', 'dodge', 'ferrari', 'honda', 'toyota', 'hyundai', 'kia', 'lamborghini', 'lexus',
                          'mazda', 'mercedes', 'skoda', 'mitsubishi', 'nissan', 'porsche', 'subaru', 'suzuki', 'tesla',
                          'volkswagen', 'volvo', 'horsepower', 'torque']

    keyword_cloud_service = ["cloud backup", "cloud storage", "cloud processing", "iaas", "paas", "saas", "aws", "azure",
                             "google cloud", "amazon web services", "infrastructure as a service", "platform as a service",
                             "software as a service", "cloud software", "IBM cloud", "vmware", "salesforce", "oracle cloud",
                             "sap cloud", "alibaba cloud", "cloud service"]

    keywords_IM = ["discord", "skype", "viber", "whatsapp", "facebook messenger", "wechat", "telegram", "line", "qq mobile"]

    keyword_Criminal_Activities = ["arson", "assault", "bigamy", "blackmail", "bribery", "burglary", "child abuse",
                                   "conspiracy", "espionage", "forgery", "fraud", "genocide", "hijacking", "homicide",
                                   "kidnap", "manslaughter", "mugging", "murder", "kill", "perjury", "rape", "riot",
                                   "robbery", "shoplift", "slander", "smuggle", "treason", "trespass", "gang fights",
                                   "steal", "theft", "cyber crime", "corruption", "domestic", "violence", "ransom",
                                   "vandalism", "child abuse ","terrorism", "militia", 'insurgent', 'bombing', 'terrorist', 'make bomb', 'bomb making', 'bombs']



    keyword_dating = ["online dating", "tinder", "okcupid", "valentines", "romantic", "roses", "presents", "anniversary",
                      "rings", "dating ideas", "movie dates", 'wedding', 'hook up']

    keyword_softwareDevelopement = ["pycharm", "netbeans", "sqlite", "linux", "visual studio", "node.js", "codenvy",
                                "angularjs", "eclipse","react native", 'python', 'java', 'c++', 'ruby on rails', 'flutter',
                                'javascript', 'html', 'maven', 'node.js', 'html', 'css', 'php', 'database', 'sql', 'db'
                                , 'pip',  'web development', 'code', 'debug', 'c#', 'kotlin', 'objective-c', 'visual basic'
                                , 'perl', 'matlab', 'libraries', 'stack development', 'backend', 'frontend', 'framework',
                                'software develop', 'machine learning', 'tensorflow', 'AI', 'API',
                                'application programming interface']

    keyword_Ecommerce_Tools = ["ecommerce website tools", "research tools", "business tools", "marketing tools",
                               "analytics tools", "bigcommerce", "x-cart", "shopify", "woocommerce", "prestashop",
                               "junglescout", "semrush", "ahrefs", "sourcify", "veeqo", "tickspot", "asana",
                               "inventory source", "oberlo", "shipwire", "tradegecko", "shippingeasy", "wave", "ecomdash",
                               "mailchimp", "campaign monitor", "feeds4", "active campaign", "bulk.ly", "buffer",
                               "omnistar", "antavo", "smile.lo", "user testing", "wishpond", "klaviyo", "buzzstream",
                               "exitbee", "metrilo", "storeya", "instasize", "visual website optimizer",
                               "optimizely analytics", "google analytics", "neatly", 'search engine optimization', 'SEO']

    keyword_Entertainment = ["plays", "comedy", "puppet shows", "sports", "performance art", "animation", "karaoke",
                             "video games", "dance", "magic", "television programs", "music", "acting", "nightclubs",
                             "fashion shows", "netflix", "concerts", "circus", "parties", "symphonies", "theatre",
                             "variety shows"]

    keyword_Software_Downloads_Sites = ["download.com", "filehippo", "zdnet download", "softpedia", "tucows",
                                        "freewarefiles", "majorgeeks", "filecluster", "soft32", "torrent", "softonic",
                                        "freewarehome", "ninite", "download crew", "filehorse", "filepuma", "sourceforge",
                                        "software" "informer", "alternativeto"]

    keyword_Finance_Accounting = ["Accounts payable", "accounts receivable", "accrued expense", "balance sheet",
                                  "book value", "equity", "inventory", "zoho books", "xero"]

    keyword_Food_drinks = ["macdonald", "kfc", "grabfood", "subway", "jolibee", "coke", "laksa", "chicken rice",
                           "yong tau foo", "buffet", "pizza", "bbq", "black pepper", "beef", "mutton", "curry",
                           "nasi lemak", "carrot cake", "green tea", "bubble tea", "pudding jelly", "cake", "bread", "milo",
                           "ice cream", "fishball"]

    keyword_Gambling = ["poker", "roulette", "slot-machines", "bingo", "baccarat", "casino war", "craps", "carribean stud",
                        "keno", "let it ride", 'betting']

    keyword_government_legal = ["moe", "mof", "mha", "mfa", "mti", "msf", "mod", "mol", "mom", "moh", "mot", ".gov.sg",
                                'government', 'ministry of', 'minister', 'minister of']

    keyword_Hobbies_Interests = ["Sports", "music", "travel", "fishing", "social work", "volunteer work",
                                 "painting", "dancing", "reading", "writing", "gardening", "animal care", "cooking",
                                 "bowling", "computer gaming", "fashion", "ice skating", "magic", "origami", "photography",
                                 "sculpting", "comedy", "winemaking", "yoga", "computer programming", "diving", "football",
                                 "basketball", "tennis", "badminton", "table tennis", "soccer", "rugby", "jogging",
                                 "marathon", "cycling", "rock climbing", "swimming", "cheerleading", "fencing", "laser tag",
                                 "darts", "eating", "sleeping", "hockey", "weightlifting", "volleyball", "martial arts",
                                 "hiking", "backpacking", "archery", "wrestling", "boxing", "poker", "chess"]

    keyword_insurance = ["life insurance", "health insurance", "travel insurance", "home insurance", "child insurance",
                         "maid insurance", "car insurance", "pet insurance", "personal accident insurance",
                         "term life insurance", "whole life insurance", "ntuc income", "great eastern", "prudential", "AIA",
                         "aviva", "savings plan", "integrated shield plan", "trip delays", "baggage delay", "lost items",
                         "medical coverage", "missed flights"]

    keyword_jobsearch = ["career@gov", "jobstreet", "gumtree", "indeed", "jobsdb", "stjobs", "mycareerfuture",
                         "jobscentral", "linkedin", "startupjobs"]

    Keyword_kids = ["hasbro", "nursery rhythms", "fox kids", "smiggle", "kiddy palace", "Playground", "toy r us", "avent",
                    "enfagrow", "kinder joy"]

    keyword_Military = ["army", "air force", "navy", "rank", "infrantry", "armour", "artillery", "special forces",
                        "rangers", "guards", "military police", "signals", "combat engineers", "field engineers", "sar 21",
                        "machine guns", "missile launcher", "weapons", "medic", "tanks", "fighter jets", "helicopter",
                        "armoured vehicles", "rocket artillery", "armoured carriers", "sergeant", "officer", "encik"]

    keyword_news_and_media = ["cna", "bbc", "thestraitstime", "thenewspaper", "mediacorp", "techredar", "asiaone", "yahoo",
                              "msn", "flipboard", "twitter", "dailymail", "today", "thebusinesstimes", 'reporters']

    keyword_peer2peer = ["pirate bay", "kickass torrent", "torrent", "rarbg", "1337x", "torlock", "YTS", " qBittorrent",
                         "Vuze", "Deluge", "uTorrent", "BitTorrent", "EZTV", "ETTV", "Popcorn Time", "LimeTorrents"]

    keyword_pets = ["cat", "dog", "rabbit", "hamster", "fish", "bird", "guinea pig", "chinchilla", "cow", "chicken",
                    "sheep", "lamb", "pig", "llama", "turtle", "tortoise", "frog"]

    keywords_realEstate = ["hdb", "bungalow", "studio", "semi-detached", "condos", "landed", "propnex realty",
                           "huttons asia", "era", "propseller", 'condominium', 'apartment', 'mansionette',
                           'property guru', 'property agent']

    keyword_Search_engines = ['google', 'yahoo', 'bing', 'duckduckgo', 'wiki.com',
                              'gibiru', 'boardreader', 'baidu', 'torsearch', 'ask.com']

    keywords_shopping = ["qoo10", "lazada", "shopee", "zalora", "taobao", "amazon", "carousell", "ebay", "redmart",
                         "reebonz" "online shopping", "online sale", "free shipping", "free delivery", "next day delivery"]

    Keyword_social = ["imgur", "facebook", "twitter", "instagram", "tumblr", "flicker", "google+", "youtube", "pinterest",
                      "reddit", "snapchat", "baidu tieba", "skype", "telegram", "whatsapp", "hardwarezone", "forum"]

    keyword_mediaStreaming = ["netflix", "youtube", "apple Tv", "chromecast", "subsonic", "audio galaxy", "tudou", "baidu",
                              "dailymotion", "vimeo"]

    keywords_trading_invest = ["stocks", "money", "profits", "srs", "blue-chip", "growth", "dividend", "nasdaq",
                               "corporate bonds", "etf"]

    Keyword_translation = ["google translate", "yandex", "babelfish", "tradukka", "linguee", "systranet", "permondo",
                           "translatesonline.com"]

    keyword_webhosting_isp_telco = ["singtel", "starhub", "m1", "circlelife", "tpg", "myrepublic", "viewquest", "alibaba",
                                    "apc", "amazon web"]

    keyword_web_hosting = ["bluehost", "inmotion hosting", "hostgator", "hostinger", "godaddy", "tsohost", "wix",
                           "siteground", "hostwinds", "weebly", "squarespace", "vodien", "a2 hosting", "dreamHost",
                           "website hosting", "domain name", "namecheap", "host website", "domain registration", "whois",
                           "website server", "apache", "nginx" "web host"]

    keyword_proxies_vpn = ["expressvpn", "nordvpn", "ipvanish", "hotspot shield", "tunnelbear", "hidester", "hide.me",
                           "proxysite.com", "kproxy", "VPNbook", "whoer.net", "megaproxy"]

    keyword_webmail = ["gmail", "hotmail", "live", "yahoo", "outlook", "aol", "zoho", "protonmail"]

    keyword_travel = ['booking.com', 'tripadvisor', 'expedia', 'airbnb', 'agoda', 'priceline', 'skyscanner',
                      'kayak.com', 'makemytrip', 'cheapoair', 'trivago', 'travelocity', 'orbitz', 'hotelurbano',
                      'book hotel', 'air tickets', 'airfares', 'hotels', 'cheap flight', 'cheap hotel', 'airline', 'flights']

    keyword_drugs = ['marijuana', 'opium', 'heroin', 'cocaine', 'barbiturates', 'meth', 'ice',
                     'crystal meth', 'ecstacy', 'weed', 'cannabis']

    Keyword_weapons = ["gun", "sword", "machine gun", "butterfly knife", "rocket", "bazooka", "flamethrower", "pistol",
                       "rifle", "grenade", "sniper"]

    keyword_sports = ["soccer", "football", "tennis", "basketball", "hockey", "bowling", "table-tennis", "kayaking",
                      "canoeing", "snorkeling", "diving", "swimming", "scuba-diving", 'martial arts']

    Keyword_religion = ["Buddihsm", "Hinduism", "Sikhism", "Christianity", "Islam", "Judaism", "Spiritism", "Shinto",
                        "Taoism"]

    Keyword_technology = ["cloud computing", "5g", "computer ai", "wireless", "ssd", "smartphone", "drones", "robots",
                          "gaming", "smartwatch"]

    keyword_cyber_security_solutions = ["identity and access management", "IAM", "cloud security",
                                        "risk and compliance management", "encryption", "data loss prevention", "DLP",
                                        "UTM", "unified threat management", "firewall", "antivirus", "antimalware", "IDS",
                                        "intrusion detection system", "intrusion prevention system", "IPS",
                                        "disaster recovery", "ddos mitigation", "cyber security solution", "IT security",
                                        "cisco", "symantec", "norton", "trend micro", "avast", "carbon black",
                                        "crowd strike", "fortinet", "palo alto", "splunk", "mcafee", "sophos", "proofpoint",
                                        "imperva", "fireye", "LogRythm", "Netskope", "trustwave"]

    keyword_education = [".edu", "coursera", "khan academy", "open culture", "udemy", "academic earth", "edx", "university",
                         "polytechnic", "diploma", "bachelors", "degree", "phd", "masters", "professor", "scholarship",
                         "schooling", "teaching", "learning", "education", "online learning", "distance learning",
                         "institute"]

    keyword_tobacco = ['marlboro', 'camel', 'cigarette', 'tobacco', 'lucky strike', 'winston', 'dunhill',
                       'lung cancer', 'viceroy', 'smoking', 'vape', 'e-cigarette', 'cigar', 'vaping', 'vaporiser', 'electronic cigarette']

    keywords=keyword_cyber_security_risk+Adult_Content+keyword_Aggressive+Keyword_arts+keyword_automotive+keyword_cloud_service+\
             keywords_IM+keyword_Criminal_Activities+keyword_dating+keyword_softwareDevelopement+keyword_Ecommerce_Tools+keyword_Entertainment+\
             keyword_Software_Downloads_Sites+keyword_Finance_Accounting+keyword_Food_drinks+keyword_Gambling+keyword_government_legal+\
             keyword_Hobbies_Interests+keyword_insurance+keyword_jobsearch+Keyword_kids+keyword_Military+keyword_news_and_media+\
             keyword_peer2peer+keyword_pets+keywords_realEstate+keyword_Search_engines+keywords_shopping+Keyword_social+keyword_mediaStreaming+\
             keywords_trading_invest+Keyword_translation+keyword_webhosting_isp_telco+keyword_web_hosting+keyword_proxies_vpn+keyword_webmail+keyword_travel+\
             keyword_drugs+Keyword_weapons+keyword_sports+Keyword_religion+Keyword_technology+keyword_cyber_security_solutions+keyword_education+keyword_tobacco

    kp0=KeywordProcessor()
    kp1=KeywordProcessor()
    kp2=KeywordProcessor()
    kp3=KeywordProcessor()
    kp4=KeywordProcessor()
    kp5=KeywordProcessor()
    kp6=KeywordProcessor()
    kp7=KeywordProcessor()
    kp8=KeywordProcessor()
    kp9=KeywordProcessor()
    kp10=KeywordProcessor()
    kp11=KeywordProcessor()
    kp12=KeywordProcessor()
    kp13=KeywordProcessor()
    kp14=KeywordProcessor()
    kp15=KeywordProcessor()
    kp16=KeywordProcessor()
    kp17=KeywordProcessor()
    kp18=KeywordProcessor()
    kp19=KeywordProcessor()
    kp20=KeywordProcessor()
    kp21=KeywordProcessor()
    kp22=KeywordProcessor()
    kp23=KeywordProcessor()
    kp24=KeywordProcessor()
    kp25=KeywordProcessor()
    kp26=KeywordProcessor()
    kp27=KeywordProcessor()
    kp28=KeywordProcessor()
    kp29=KeywordProcessor()
    kp30=KeywordProcessor()
    kp31=KeywordProcessor()
    kp32=KeywordProcessor()
    kp33=KeywordProcessor()
    kp34=KeywordProcessor()
    kp35=KeywordProcessor()
    kp36=KeywordProcessor()
    kp37=KeywordProcessor()
    kp38=KeywordProcessor()
    kp39=KeywordProcessor()
    kp40=KeywordProcessor()
    kp41=KeywordProcessor()
    kp42=KeywordProcessor()
    kp43=KeywordProcessor()
    kp44=KeywordProcessor()
    kp45=KeywordProcessor()
    for word in keywords:
        kp0.add_keyword(word)
    for word in keyword_cyber_security_risk:
        kp1.add_keyword(word)
    for word in Adult_Content:
        kp2.add_keyword(word)
    for word in keyword_Aggressive:
        kp3.add_keyword(word)
    for word in Keyword_arts:
        kp4.add_keyword(word)
    for word in keyword_automotive:
        kp5.add_keyword(word)
    for word in keyword_cloud_service:
        kp6.add_keyword(word)
    for word in keywords_IM:
        kp7.add_keyword(word)
    for word in keyword_Criminal_Activities:
        kp8.add_keyword(word)
    for word in keyword_dating:
        kp9.add_keyword(word)
    for word in keyword_softwareDevelopement:
        kp10.add_keyword(word)
    for word in keyword_Ecommerce_Tools:
        kp11.add_keyword(word)
    for word in keyword_Entertainment:
        kp12.add_keyword(word)
    for word in keyword_Software_Downloads_Sites:
        kp13.add_keyword(word)
    for word in keyword_Finance_Accounting:
        kp14.add_keyword(word)
    for word in keyword_Food_drinks:
        kp15.add_keyword(word)
    for word in keyword_Gambling:
        kp16.add_keyword(word)
    for word in keyword_government_legal:
        kp17.add_keyword(word)
    for word in keyword_Hobbies_Interests:
        kp18.add_keyword(word)
    for word in keyword_insurance:
        kp19.add_keyword(word)
    for word in keyword_jobsearch:
        kp20.add_keyword(word)
    for word in Keyword_kids:
        kp21.add_keyword(word)
    for word in keyword_Military:
        kp22.add_keyword(word)
    for word in keyword_news_and_media:
        kp23.add_keyword(word)
    for word in keyword_peer2peer:
        kp24.add_keyword(word)
    for word in keyword_pets:
        kp25.add_keyword(word)
    for word in keywords_realEstate:
        kp26.add_keyword(word)
    for word in keyword_Search_engines:
        kp27.add_keyword(word)
    for word in keywords_shopping:
        kp28.add_keyword(word)
    for word in Keyword_social:
        kp29.add_keyword(word)
    for word in keyword_mediaStreaming:
        kp30.add_keyword(word)
    for word in keywords_trading_invest:
        kp31.add_keyword(word)
    for word in Keyword_translation:
        kp32.add_keyword(word)
    for word in keyword_webhosting_isp_telco:
        kp33.add_keyword(word)
    for word in keyword_web_hosting:
        kp34.add_keyword(word)
    for word in keyword_proxies_vpn:
        kp35.add_keyword(word)
    for word in keyword_webmail:
        kp36.add_keyword(word)
    for word in keyword_travel:
        kp37.add_keyword(word)
    for word in keyword_drugs:
        kp38.add_keyword(word)
    for word in Keyword_weapons:
        kp39.add_keyword(word)
    for word in keyword_sports:
        kp40.add_keyword(word)
    for word in Keyword_religion:
        kp41.add_keyword(word)
    for word in Keyword_technology:
        kp42.add_keyword(word)
    for word in keyword_cyber_security_solutions:
        kp43.add_keyword(word)
    for word in keyword_education:
        kp44.add_keyword(word)
    for word in keyword_tobacco:
        kp45.add_keyword(word)
    x= textSplit
    y0 = len(kp0.extract_keywords(x))
    y1 = len(kp1.extract_keywords(x))
    y2 = len(kp2.extract_keywords(x))
    y3 = len(kp3.extract_keywords(x))
    y4 = len(kp4.extract_keywords(x))
    y5 = len(kp5.extract_keywords(x))
    y6 = len(kp6.extract_keywords(x))
    y7 = len(kp7.extract_keywords(x))
    y8 = len(kp8.extract_keywords(x))
    y9 = len(kp9.extract_keywords(x))
    y10 = len(kp10.extract_keywords(x))
    y11 = len(kp11.extract_keywords(x))
    y12 = len(kp12.extract_keywords(x))
    y13 = len(kp13.extract_keywords(x))
    y14 = len(kp14.extract_keywords(x))
    y15 = len(kp15.extract_keywords(x))
    y16 = len(kp16.extract_keywords(x))
    y17 = len(kp17.extract_keywords(x))
    y18 = len(kp18.extract_keywords(x))
    y19 = len(kp19.extract_keywords(x))
    y20 = len(kp20.extract_keywords(x))
    y21 = len(kp21.extract_keywords(x))
    y22 = len(kp22.extract_keywords(x))
    y23 = len(kp23.extract_keywords(x))
    y24 = len(kp24.extract_keywords(x))
    y25 = len(kp25.extract_keywords(x))
    y26 = len(kp26.extract_keywords(x))
    y27 = len(kp27.extract_keywords(x))
    y28 = len(kp28.extract_keywords(x))
    y29 = len(kp29.extract_keywords(x))
    y30 = len(kp30.extract_keywords(x))
    y31 = len(kp31.extract_keywords(x))
    y32 = len(kp32.extract_keywords(x))
    y33 = len(kp33.extract_keywords(x))
    y34 = len(kp34.extract_keywords(x))
    y35 = len(kp35.extract_keywords(x))
    y36 = len(kp36.extract_keywords(x))
    y37 = len(kp37.extract_keywords(x))
    y38 = len(kp38.extract_keywords(x))
    y39 = len(kp39.extract_keywords(x))
    y40 = len(kp40.extract_keywords(x))
    y41 = len(kp41.extract_keywords(x))
    y42 = len(kp42.extract_keywords(x))
    y43 = len(kp43.extract_keywords(x))
    y44 = len(kp44.extract_keywords(x))
    y45 = len(kp45.extract_keywords(x))

    Total_matches = y0
    per1 = float(percentage1(y0, y1))
    per2 = float(percentage1(y0, y2))
    per3 = float(percentage1(y0, y3))
    per4 = float(percentage1(y0, y4))
    per5 = float(percentage1(y0, y5))
    per6 = float(percentage1(y0, y6))
    per7 = float(percentage1(y0, y7))
    per8 = float(percentage1(y0, y8))
    per9 = float(percentage1(y0, y9))
    per10 = float(percentage1(y0, y10))
    per11 = float(percentage1(y0, y11))
    per12 = float(percentage1(y0, y12))
    per13 = float(percentage1(y0, y13))
    per14 = float(percentage1(y0, y14))
    per15 = float(percentage1(y0, y15))
    per16 = float(percentage1(y0, y16))
    per17 = float(percentage1(y0, y17))
    per18 = float(percentage1(y0, y18))
    per19 = float(percentage1(y0, y19))
    per20 = float(percentage1(y0, y20))
    per21 = float(percentage1(y0, y21))
    per22 = float(percentage1(y0, y22))
    per23 = float(percentage1(y0, y23))
    per24 = float(percentage1(y0, y24))
    per25 = float(percentage1(y0, y25))
    per26 = float(percentage1(y0, y26))
    per27 = float(percentage1(y0, y27))
    per28 = float(percentage1(y0, y28))
    per29 = float(percentage1(y0, y29))
    per30 = float(percentage1(y0, y30))
    per31 = float(percentage1(y0, y31))
    per32 = float(percentage1(y0, y32))
    per33 = float(percentage1(y0, y33))
    per34 = float(percentage1(y0, y34))
    per35 = float(percentage1(y0, y35))
    per36 = float(percentage1(y0, y36))
    per37 = float(percentage1(y0, y37))
    per38 = float(percentage1(y0, y38))
    per39 = float(percentage1(y0, y39))
    per40 = float(percentage1(y0, y40))
    per41 = float(percentage1(y0, y41))
    per42 = float(percentage1(y0, y42))
    per43 = float(percentage1(y0, y43))
    per44 = float(percentage1(y0, y44))
    per45 = float(percentage1(y0, y45))
    allP = [per1, per2, per3, per4, per5, per6, per7, per8, per9, per10, per11, per12, per13, per14, per15,
            per16, per17, per18, per19, per20, per21, per22, per23, per24, per25, per26, per27, per28,
            per29, per30, per31, per32, per33, per34, per35, per36, per37, per38, per39, per40, per41,
            per42, per43, per44, per45]
    allP.sort(key=float)
    if y0 == 0:
        Category = 'None'
    else:
        if per1 >= allP[-1]:
            Category = 'Cyber-Security Risk'
        elif per2 >= allP[-1]:
            Category = 'Adult Content'
        elif per3 >= allP[-1]:
            Category = 'Aggresive'
        elif per4 >= allP[-1]:
            Category = 'Arts'
        elif per5 >= allP[-1]:
            Category = 'Automotive'
        elif per6 >= allP[-1]:
            Category = 'Cloud Services'
        elif per7 >= allP[-1]:
            Category = 'Instant Messaging'
        elif per8 >= allP[-1]:
            Category = 'Criminal Activities'
        elif per9 >= allP[-1]:
            Category = 'Dating'
        elif per10 >= allP[-1]:
            Category = 'Software Development'
        elif per11 >= allP[-1]:
            Category = 'Ecommerce Tools'
        elif per12 >= allP[-1]:
            Category = 'Entertainment'
        elif per13 >= allP[-1]:
            Category = 'Software Download Sites'
        elif per14 >= allP[-1]:
            Category = 'Finance & Accounting'
        elif per15 >= allP[-1]:
            Category = 'Food and Drinks'
        elif per16 >= allP[-1]:
            Category = 'Gambling'
        elif per17 >= allP[-1]:
            Category = 'Government'
        elif per18 >= allP[-1]:
            Category = 'Hobbies and Interests'
        elif per19 >= allP[-1]:
            Category = 'Insurance'
        elif per20 >= allP[-1]:
            Category = 'Job Search'
        elif per21 >= allP[-1]:
            Category = 'Kids'
        elif per22 >= allP[-1]:
            Category = 'Military'
        elif per23 >= allP[-1]:
            Category = 'News & Media'
        elif per24 >= allP[-1]:
            Category = 'Peer 2 Peer'
        elif per25 >= allP[-1]:
            Category = 'Pets'
        elif per26 >= allP[-1]:
            Category = 'Real Estate'
        elif per27 >= allP[-1]:
            Category = 'Search Engine'
        elif per28 >= allP[-1]:
            Category = 'Shopping'
        elif per29 >= allP[-1]:
            Category = 'Social'
        elif per30 >= allP[-1]:
            Category = 'Media Streaming'
        elif per31 >= allP[-1]:
            Category = 'Trading & Investment'
        elif per32 >= allP[-1]:
            Category = 'Translation'
        elif per33 >= allP[-1]:
            Category = 'WebHosting_ISP_Telco'
        elif per34 >= allP[-1]:
            Category = 'Webhosting'
        elif per35 >= allP[-1]:
            Category = 'Proxies & VPN'
        elif per36 >= allP[-1]:
            Category = 'Webmail'
        elif per37 >= allP[-1]:
            Category = 'Travel'
        elif per38 >= allP[-1]:
            Category = 'Drugs'
        elif per39 >= allP[-1]:
            Category = 'Weapons'
        elif per40 >= allP[-1]:
            Category = 'Sports'
        elif per41 >= allP[-1]:
            Category = 'Religion'
        elif per42 >= allP[-1]:
            Category = 'Technology'
        elif per43 >= allP[-1]:
            Category = 'Cyber-Security Technologies'
        elif per44 >= allP[-1]:
            Category = 'Education'
        elif per45 >= allP[-1]:
            Category = 'Tobacco'

    return Category


def get_labeled_exif(exif):
    labeled = {}
    if exif.items() != None:
        for (key, val) in exif.items():
            labeled[TAGS.get(key)] = val

        return labeled
    else:
        return None

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()
