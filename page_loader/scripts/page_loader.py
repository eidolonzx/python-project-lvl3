#!/usr/bin/env python3

import argparse
from page_loader.downloader import downloader


def main():
    app_desc = 'Downloads a web page and saves it to your hard drive.'
    parser = argparse.ArgumentParser(description=app_desc)
    parser.add_argument('url', help="Enter web page url")
    parser.add_argument('-o', '--output', help='Enter folder path')
    args = parser.parse_args()

    result = downloader(args.url, args.output)
    print(result)

if __name__ == '__main__':
    main()
