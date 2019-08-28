import os
import sys
import glob
import datetime
import logging

from PyPDF2 import PdfFileMerger

class PdfMerger:
    output_filename = 'agrupado.pdf'

    def __init__(self):
        log_filename = str(datetime.datetime.now().date()) + "-execution.log"
        logging.basicConfig(filename=log_filename,level=logging.INFO)

    def merge_pdfs_from_folder(self, target_directory):
        pdfs = sorted(glob.glob(os.path.join(target_directory, '*.pdf')))
        merged_list = glob.glob(os.path.join(target_directory, self.output_filename))
        
        if len(pdfs) <= 1 or len(merged_list) > 0:
            return
            
        merger = PdfFileMerger()

        for pdf in pdfs:
            if not pdf.endswith(self.output_filename):
                merger.append(pdf)
        
        merger.write(os.path.join(target_directory, self.output_filename))
        merger.close()

        logging.info("Merged files in " + target_directory)

    def get_content_folders(self, target_directory=''):
        directories = glob.glob(os.path.join(target_directory, '*', ''))

        self.merge_pdfs_from_folder(target_directory)
        if not directories:
            return

        for directory in directories:
            self.get_content_folders(directory)

    def main(self):
        workdir = sys.argv[1] if len(sys.argv) > 1 else ''
        self.get_content_folders(workdir)


PM = PdfMerger()
PM.main()
