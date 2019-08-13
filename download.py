"""
Download all the data.
"""
import logging
import census_map_downloader


def main():
    # Configure logging
    logger = logging.getLogger('census_map_downloader')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    data_dir = "./"
    census_map_downloader.StatesDownloader2018(data_dir=data_dir).run()


if __name__ == '__main__':
    main()
