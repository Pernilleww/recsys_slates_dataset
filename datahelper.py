import logging
from google_drive_downloader import GoogleDriveDownloader as gdd
def download_data_files(data_dir : str = "data", overwrite=False):
    """
    Downloads the data from google drive.
    If files exist they will not be downloaded again unless overwrite=True
    """
    gdrive_file_ids = {
        'data.npz' : '1VXKXIvPCJ7z4BCa4G_5-Q2XMAD7nXOc7',
        'ind2val.json' : '1WOCKfuttMacCb84yQYcRjxjEtgPp6F4N',
        'itemattr.npz' : '1rKKyMQZqWp8vQ-Pl1SeHrQxzc5dXldnR'
    }
    for filename, gdrive_id in gdrive_file_ids.items():
        logging.info("Downloading {}".format(filename))
        gdd.download_file_from_google_drive(file_id=gdrive_id,
                                        dest_path="{}/{}".format(data_dir, filename),
                                        overwrite=overwrite)
    logging.info("Done downloading all files.")
    return True
