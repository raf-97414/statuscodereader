import argparse
from statuscodereader.sc import site_is_online_async
def read_user_cli_args():
    parser = argparse.ArgumentParser(prog="status code reader", description="Display status code of website")
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more website URLs",
        action='store',
        dest='urls'
    )

    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
        action='store',
        dest='files'
    )

    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="run the connectivity check asynchronously",
    )

    return parser.parse_args()

#def display_check_result():
      #argvvv = read_user_cli_args().urls
      #for i in range(0,len(argvvv)):
       #target_url, stat = site_is_online_async(argvvv[i])
      # print('The status of {0} is: {1}'.format(target_url, stat))

def display_check_result(target_url, stat, error=""):
        print('The status of {0} is: {1}'.format(target_url, stat))






