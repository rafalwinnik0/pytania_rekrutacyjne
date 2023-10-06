nazwiska = ['AnnA KOT', 18, 'JAN NOWAK', ['nie','twoj','interes'], 'ROBERT Wąż']

naprawione_nazwiska = list(filter(lambda x: type(x) is str, nazwiska))
naprawione_nazwiska = [ x.lower().title() for x in naprawione_nazwiska]
print(naprawione_nazwiska)