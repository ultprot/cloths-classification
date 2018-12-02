from icrawler.builtin import GoogleImageCrawler

dest_dir='' #directory where data are stored
keyword=''  #searching keyword of data

google_crawler = GoogleImageCrawler(storage={'root_dir': './'+dest_dir})

google_crawler.crawl(
    keyword=keyword,
    filters={'date': ((2017, 1, 1), (2017, 7, 30))},
    max_num=250,
    file_idx_offset=0)

google_crawler.crawl(
    keyword=keyword,
    filters={'date': ((2017, 7, 31), (2017, 12, 31))},
    max_num=250,
    file_idx_offset='auto')
    
google_crawler.crawl(
    keyword=keyword,
    filters={'date': ((2018, 1, 1), (2018, 7, 31))},
    max_num=250,
    file_idx_offset='auto')
    
google_crawler.crawl(
    keyword=keyword,
    filters={'date': ((2018, 8, 1), (2018, 10, 31))},
    max_num=250,
    file_idx_offset='auto')