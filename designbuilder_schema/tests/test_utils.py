"""Tests for the utils module"""

import pytest
import json
import tempfile
import os
from pathlib import Path
from designbuilder_schema.utils import (
    remove_prefixes,
    add_prefixes,
    file_to_dict,
    load_model,
    dict_to_file,
    save_model,
)
from designbuilder_schema.core import DSB

# Get path to samples folder relative to repository root
test_dir = Path(__file__).parent
repo_root = test_dir.parent.parent
samples_models = repo_root / "samples" / "models"


class TestPrefixFunctions:
    """Test prefix manipulation functions"""

    def test_remove_prefixes_with_at_symbol(self):
        """Test removing @ prefix from key"""
        key, value = remove_prefixes(None, "@attribute", "value")
        assert key == "attribute"
        assert value == "value"

    def test_remove_prefixes_with_hash_symbol(self):
        """Test removing # prefix from key"""
        key, value = remove_prefixes(None, "#text", "content")
        assert key == "text"
        assert value == "content"

    def test_remove_prefixes_without_prefix(self):
        """Test key without prefix remains unchanged"""
        key, value = remove_prefixes(None, "Element", "value")
        assert key == "Element"
        assert value == "value"

    def test_add_prefixes_simple_dict(self):
        """Test adding prefixes to simple dict"""
        data = {"attribute": "value", "Element": "content"}
        result = add_prefixes(data)
        assert result["@attribute"] == "value"
        assert result["Element"] == "content"

    def test_add_prefixes_with_text_key(self):
        """Test converting 'text' key to '#text'"""
        data = {"text": "some text"}
        result = add_prefixes(data)
        assert result["#text"] == "some text"

    def test_add_prefixes_nested_dict(self):
        """Test adding prefixes to nested dict"""
        data = {"Element": {"attribute": "value", "Child": "content"}}
        result = add_prefixes(data)
        assert result["Element"]["@attribute"] == "value"
        assert result["Element"]["Child"] == "content"

    def test_add_prefixes_list(self):
        """Test adding prefixes to list of dicts"""
        data = [{"attribute": "value1"}, {"attribute": "value2"}]
        result = add_prefixes(data)
        assert result[0]["@attribute"] == "value1"
        assert result[1]["@attribute"] == "value2"


class TestFileOperations:
    """Test file I/O operations"""

    def test_file_to_dict_json(self):
        """Test loading JSON file to dict"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"test": "data"}, f)
            temp_file = f.name

        try:
            result = file_to_dict(temp_file)
            assert result == {"test": "data"}
        finally:
            os.unlink(temp_file)

    def test_file_to_dict_unsupported_format(self):
        """Test that unsupported file format raises ValueError"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("some text")
            temp_file = f.name

        try:
            with pytest.raises(ValueError, match="Unsupported file format"):
                file_to_dict(temp_file)
        finally:
            os.unlink(temp_file)

    def test_dict_to_file_json(self):
        """Test saving dict to JSON file"""
        data = {"dsbXML": {"name": "test", "version": "1.0"}}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_file = f.name

        try:
            dict_to_file(data, temp_file)
            with open(temp_file, "r") as f:
                result = json.load(f)
            assert "dsbJSON" in result
            assert result["dsbJSON"]["name"] == "test"
        finally:
            os.unlink(temp_file)

    def test_dict_to_file_xml(self):
        """Test saving dict to XML file"""
        data = {"dsbXML": {"name": "test", "version": "1.0"}}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
            temp_file = f.name

        try:
            dict_to_file(data, temp_file)
            with open(temp_file, "r") as f:
                content = f.read()
            assert "<?xml version" in content
            assert "dsbXML" in content
            assert "name=" in content or "<name>" in content
        finally:
            os.unlink(temp_file)

    def test_dict_to_file_unsupported_format(self):
        """Test that unsupported file format raises ValueError"""
        data = {"dsbXML": {"name": "test"}}
        with pytest.raises(ValueError, match="Unsupported file format"):
            dict_to_file(data, "test.txt")


class TestModelOperations:
    """Test model loading and saving operations"""

    def test_load_model_from_sample(self):
        """Test loading a model from sample XML file"""
        sample_path = samples_models / "EmptySite.xml"
        if sample_path.exists():
            model = load_model(str(sample_path))
            assert isinstance(model, DSB)
            assert model.name
            assert model.Site is not None
        else:
            pytest.skip("Sample file not found")

    def test_save_model_json(self):
        """Test saving a model to JSON file"""
        sample_path = samples_models / "EmptySite.xml"
        if not sample_path.exists():
            pytest.skip("Sample file not found")

        model = load_model(str(sample_path))
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_file = f.name

        try:
            save_model(model, temp_file)
            assert os.path.exists(temp_file)
            with open(temp_file, "r") as f:
                content = json.load(f)
            assert "dsbJSON" in content
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_save_model_xml(self):
        """Test saving a model to XML file"""
        sample_path = samples_models / "EmptySite.xml"
        if not sample_path.exists():
            pytest.skip("Sample file not found")

        model = load_model(str(sample_path))
        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
            temp_file = f.name

        try:
            save_model(model, temp_file)
            assert os.path.exists(temp_file)
            with open(temp_file, "r") as f:
                content = f.read()
            assert "<?xml version" in content
            assert "dsbXML" in content
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
