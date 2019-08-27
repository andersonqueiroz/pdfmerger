import os
import sys
import glob
from PyPDF2 import PdfFileMerger

class PdfMerger:
    output_filename = 'agrupado.pdf'

    def merge_pdfs_from_folder(self, target_directory):
        pdfs = glob.glob(os.path.join(target_directory, '*.pdf'))
        
        if len(pdfs) <= 1:
            return
            
        merger = PdfFileMerger()

        for pdf in pdfs:
            merger.append(pdf)
        
        merger.write(os.path.join(target_directory, self.output_filename))
        merger.close()
        print("Merged files in " + target_directory)

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
