import sys
import argparse
import urllib.request
import urllib.error
from WebsiteCrawler import WebsiteCrawler


def _url_checker():
    """
        urlが有効かつ存在するかをチェックする
    """
    try:
        f = urllib.request.urlopen(target_website)
        f.close()
    except (ValueError, urllib.error.URLError):
        print(f'url {target_website} is not available.')
        sys.exit(1)


# メイン処理の実行
if __name__ == '__main__':

    # 引数の取得
    parser = argparse.ArgumentParser(
        prog='URL Craawler',
        description='引数で与えられたURLをクロールしてURLリストを生成します。',
        usage='python main.py $url --max-count max_url_count')
    parser.add_argument('arg1', help='target url')
    parser.add_argument('-m', '--max_count', default='100', help='max url list count')
    args = parser.parse_args()

    # 走査対象のURL
    # target_website = 'https://www.seibulions.jp/'
    target_website = args.arg1
    _url_checker()

    # 収集するURLの限界件数
    try:
        limit_number = int(args.max_count)
    except ValueError:
        print(f'bad number: {args.max_count}')
        sys.exit(1)

    # ユーザーエージェント
    user_agent = 'foo-Bot/1.0 (xxxxfoo@xxmail.com)'

    # クローラーの作成
    crawler = WebsiteCrawler(target_website, user_agent, limit_number)

    # クローリングの実行
    result_url_list = crawler.crawl()

    # 収集したURLの出力
    print('-------- 結果出力 --------')
    for url in result_url_list:
        print(url)

    print(f'総件数：{len(result_url_list)}')
