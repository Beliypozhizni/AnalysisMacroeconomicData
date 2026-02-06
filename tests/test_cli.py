from macro_analyzer.cli import main


def test_cli_success_prints_table_and_returns_0(tmp_path, capsys):
    f1 = tmp_path / "a.csv"
    f1.write_text("country,gdp\nA,10\nA,30\nB,100\nB,50\n", encoding="utf-8")

    rc = main(["--files", str(f1), "--report", "average-gdp"])
    captured = capsys.readouterr()

    assert rc == 0
    out = captured.out
    assert "country" in out
    assert "avg_gdp" in out
    assert "|  1 |" in out


def test_cli_invalid_file_returns_2_and_writes_to_stderr(tmp_path, capsys):
    missing = tmp_path / "missing.csv"
    rc = main(["--files", str(missing), "--report", "average-gdp"])
    captured = capsys.readouterr()

    assert rc == 2
    assert captured.out == ""
    assert "Input error:" in captured.err


def test_cli_report_argument_rejected_by_argparse(tmp_path):
    f1 = tmp_path / "a.csv"
    f1.write_text("country,gdp\nA,10\n", encoding="utf-8")

    try:
        main(["--files", str(f1), "--report", "nope"])
        assert False, "argparse should exit"
    except SystemExit as e:
        assert e.code == 2
