from weiboSpider import Spider

if __name__ == "__main__":
    cookie = '_T_WM=e633802c234ba96dc0656a5d433c0b4d; SUB=_2A2578m9tDeRxGeRG71cV8SfMzD-IHXVZHXElrDV6PUJbrdBeLRffkW1LHeuQeoJ-dm8CIDWMnBdTxi12UBZLGg..; SUHB=0RyqaABFQU1WoA; SSOLoginState=1458970429; H5_INDEX=0_all; H5_INDEX_TITLE=YKRC17; gsid_CTandWM=4uwFCpOz5DPebDw5qaQ1jbWdR1b'
    # user_id = 'u/3826119232'
    user_id = 'njjnga'
    Spider(cookie, user_id, 940, 2304).run()
