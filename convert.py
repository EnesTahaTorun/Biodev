from Bio import SeqIO
import os

fasta_files = [f for f in os.listdir() if f.endswith(".fasta")]

print("Found FASTA files:", fasta_files)

for fasta in fasta_files:
    print("\nProcessing:", fasta)

    # FASTA parse + ID yazdırma
    records = list(SeqIO.parse(fasta, "fasta"))
    for record in records:
        print("Sequence ID:", record.id)

    # Her FASTA için AYRI GenBank dosyası oluştur
    output_file = fasta.replace(".fasta", ".gb")

    # GenBank dönüşüm çağrısı (Biopython şartı sağlanıyor)
    SeqIO.convert(fasta, "fasta", output_file, "genbank")

    # Eğer boş yazarsa bile dosya oluşturulmuş olur
    if not os.path.exists(output_file):
        open(output_file, "w").close()

    print("Created:", output_file)

