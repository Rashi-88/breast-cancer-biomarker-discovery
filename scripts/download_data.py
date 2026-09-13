import GEOparse

print("Downloading Breast Cancer dataset...")

gse = GEOparse.get_GEO(
    geo="GSE42568",
    destdir="data",
    silent=False
)

print("Download completed!")