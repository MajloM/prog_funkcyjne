def analyze_data(data):
    if isinstance(data, list):
        print("Przetwarzam liste danych:", data)

    elif isinstance(data, tuple):
        print("Przetwarzam krotkę danych:", data)

    else:
        print("Nieznany typ danych:", type(data))

analyze_data([1, 2, 3])
analyze_data((4, 5, 6))
analyze_data("hello")