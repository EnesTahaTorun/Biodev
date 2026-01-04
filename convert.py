from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import os

fasta_files = [f for f in os.listdir() if f.endswith(".fasta")]

print(f"Bulunan dosyalar: {fasta_files}")

try:
    from Bio.Alphabet import generic_protein
    print("Eski Biopython tespit edildi, alfabe zorlanacak.")
    use_alphabet = True
except ImportError:
    print("Yeni Biopython tespit edildi.")
    use_alphabet = False

for fasta in fasta_files:
    print(f"\nİşleniyor: {fasta}")
    
    records = list(SeqIO.parse(fasta, "fasta"))
    corrected_records = []
    
    for record in records:
        print(f" - Sequence ID: {record.id}")
        
        seq_data = str(record.seq)
        
        if use_alphabet:
            new_seq = Seq(seq_data, generic_protein)
        else:
            new_seq = record.seq
            
        new_record = SeqRecord(
            new_seq,
            id=record.id,
            name=record.name,
            description=record.description
        )
        
        new_record.annotations['molecule_type'] = 'protein'
        
        corrected_records.append(new_record)
    
    output_file = fasta.replace(".fasta", ".gb")
    SeqIO.write(corrected_records, output_file, "genbank")
    print(f" + Oluşturuldu: {output_file}")

print("\nOperasyon tamam reis.")
