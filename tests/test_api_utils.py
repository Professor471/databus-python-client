from databusclient.api.utils import get_databus_id_parts_from_file_url


def test_split_full_url():
    result = get_databus_id_parts_from_file_url(
        "https://databus.dbpedia.org/dbpedia/mappings/geo-coordinates/2022.12.01/file.ttl"
    )
    assert result == (
        "databus.dbpedia.org",
        "dbpedia",
        "mappings",
        "geo-coordinates",
        "2022.12.01",
        "file.ttl",
        
    )

def test_split_short_url_fills_none():
    result = get_databus_id_parts_from_file_url(
        "https://databus.dbpedia.org/dbpedia/mappings"
    )
    assert result == (
        "databus.dbpedia.org",
        "dbpedia",
        "mappings",
        None,
        None,
        None,
    )

def test_split_http_same_as_https():
    result = get_databus_id_parts_from_file_url(
        "http://databus.dbpedia.org/dbpedia/mappings/geo-coordinates/2022.12.01/file.ttl"
    )
    assert result == (
        "databus.dbpedia.org",
        "dbpedia",
        "mappings",
        "geo-coordinates",
        "2022.12.01",
        "file.ttl",
    )

def test_split_trailing_slash_ignored():
    result = get_databus_id_parts_from_file_url(
        "https://databus.dbpedia.org/dbpedia/mappings/geo-coordinates/2022.12.01/file.ttl/"
    )
    assert result == (
        "databus.dbpedia.org",
        "dbpedia",
        "mappings",
        "geo-coordinates",
        "2022.12.01",
        "file.ttl",
    )

def test_split_empty_string():
    result = get_databus_id_parts_from_file_url(
        ""
    )
    assert result == (
        "",
        None,
        None,
        None,
        None,
        None,
    )

def test_split_too_long_keeps_first_six():
    result = get_databus_id_parts_from_file_url(
        "https://databus.dbpedia.org/a/b/c/d/e/f/g/h"
    )
    assert result == (
        "databus.dbpedia.org",
        "a",
        "b",
        "c",
        "d",
        "e",
    )