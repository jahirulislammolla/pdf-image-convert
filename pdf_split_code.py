
import pymupdf
from pathlib import Path

input_pdf = r"F:\pdf\Davidson's_Principles_and_Practice_of_Medicine_25eTRUE_1.pdf"
output_dir = Path("split_output")
output_dir.mkdir(exist_ok=True)

pages_per_file = 200

with pymupdf.open(input_pdf) as pdf:
    total_pages = len(pdf)

    for start in range(0, total_pages, pages_per_file):
        end = min(start + pages_per_file, total_pages)

        with pymupdf.open() as new_pdf:
            new_pdf.insert_pdf(pdf, from_page=start, to_page=end - 1)

            output_file = output_dir / f"Part_{start // pages_per_file + 1:02d}.pdf"
            new_pdf.save(str(output_file))

        print(f"Created: {output_file} | Pages {start + 1}-{end}")

print("All PDF files created successfully!")
