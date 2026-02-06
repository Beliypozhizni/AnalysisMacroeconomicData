import pytest
from macro_analyzer.io import read_rows, InputError

def test_read_rows_reads_and_combines_multiple_files(tmp_path):
    f1 = tmp_path / "a.csv"
    f1.write_text("country,gdp\nA,10\nB,20\n", encoding="utf-8")
    f2 = tmp_path / "b.csv"
    f2.write_text("country,gdp\nA,30\n", encoding="utf-8")

    rows = read_rows([str(f1), str(f2)])
    assert rows == [
        {"country": "A", "gdp": "10"},
        {"country": "B", "gdp": "20"},
        {"country": "A", "gdp": "30"},
    ]

def test_read_rows_raises_on_missing_file(tmp_path):
    missing = tmp_path / "missing.csv"
    with pytest.raises(InputError) as e:
        read_rows([str(missing)])
    assert "File not found" in str(e.value)

def test_read_rows_raises_on_directory(tmp_path):
    d = tmp_path / "dir"
    d.mkdir()
    with pytest.raises(InputError) as e:
        read_rows([str(d)])
    assert "Not a file" in str(e.value)

def test_read_rows_raises_on_empty_csv(tmp_path):
    f = tmp_path / "empty.csv"
    f.write_text("", encoding="utf-8")
    with pytest.raises(InputError) as e:
        read_rows([str(f)])
    assert "missing header" in str(e.value).lower()
