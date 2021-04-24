from WebsiteCrawler import WebsiteCrawler

# メイン処理の実行
if __name__ == '__main__':

    # 走査対象のURL
    target_website = 'https://www.seibulions.jp/'

    # ユーザーエージェント
    user_agent = 'foo-Bot/1.0 (xxxxfoo@xxmail.com)'

    # 収集するURLの限界件数
    limit_number = 100

    # クローラーの作成
    crawler = WebsiteCrawler(target_website, user_agent, limit_number)

    # クローリングの実行
    result_url_list = crawler.crawl()

    # 収集したURLの出力
    print('-------- 結果出力 --------')
    for url in result_url_list:
        print(url)

    print(f'総件数：{len(result_url_list)}')