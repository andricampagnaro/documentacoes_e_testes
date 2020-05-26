from unicodedata import normalize
import csv
import gzip
import io

def encode(name):
    ascii_name = normalize("NFKD", name).encode("ascii", errors="ignore").decode("ascii")
    return ascii_name.upper()

def load_data():
    fobj = io.TextIOWrapper(gzip.open("nomes.csv.gz"), encoding="utf-8")
    csv_reader = csv.DictReader(fobj)
    data = {row["first_name"]: row["classification"] for row in csv_reader}
    fobj.close()
    return data

name_data = load_data()
print(f"Dicionário de nomes criado com {len(name_data)} nomes.")

def classify_download(name):
    encoded_name = encode(name)
    return name_data[encoded_name]

print(classify_download("Dirce"))
