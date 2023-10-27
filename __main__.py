import asyncio
import sys
import pathlib
from statuscodereader.cli import read_user_cli_args, display_check_result
from statuscodereader.sc import site_is_online_async, statuscode

def get_urls(args):
    urls = args.urls
    if args.files:
        urls += read_urls_from_files(args.files)
    return urls

def read_urls_from_files(input_file) :
       file_path = pathlib.Path(input_file)
       if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: empty input file, {input_file}", file=sys.stderr)
       else:
            print("Error: input file not found", file=sys.stderr)
            return []


def synchronous_urls_check(urls):
    for url in urls:
        statuscode(url)

async def asynchronous_check(urls):
    async def _check(url):
        error = ""
        try:
            result = await site_is_online_async(url)
        except Exception as e:
            error = str(e)
        display_check_result(url, result, error)

    await asyncio.gather(*(_check(url) for url in urls))


def main():
    user_args = read_user_cli_args()
    urls = get_urls(user_args)
    if len(urls) == 0:
        print("Error no urls to parse")
        sys.exit(1)


    if user_args:
        asyncio.run(asynchronous_check(urls))

    else:
        synchronous_urls_check(urls)



if __name__ == '__main__':
    main()






