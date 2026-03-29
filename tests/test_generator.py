import pytest
from pathlib import Path
import tempfile

from core.generator import Generator
from core.models.project import Project


def test_generate_paper_project_creates_expected_files():
    with tempfile.TemporaryDirectory(dir=Path.cwd()) as temp_dir:
        project_root = Path(temp_dir) / "PaperPlugin"
        project_root.mkdir()
        project = Project(name="PaperPlugin", platform="paper", path=str(project_root))

        Generator().generate(project)

        plugin_yml = project_root / "plugin.yml"
        main_java = (
            project_root / "src" / "main" / "java" / "mpm" / "paperplugin" / "Main.java"
        )

        assert plugin_yml.exists()
        assert main_java.exists()
        assert "name: PaperPlugin" in plugin_yml.read_text(encoding="utf-8")
        assert "main: mpm.paperplugin.Main" in plugin_yml.read_text(encoding="utf-8")


def test_generate_levilamina_project_creates_expected_files():
    with tempfile.TemporaryDirectory(dir=Path.cwd()) as temp_dir:
        project_root = Path(temp_dir) / "BedrockPlugin"
        project_root.mkdir()
        project = Project(name="BedrockPlugin", platform="levilamina", path=str(project_root))

        Generator().generate(project)

        cmake_lists = project_root / "CMakeLists.txt"
        main_cpp = project_root / "main.cpp"

        assert cmake_lists.exists()
        assert main_cpp.exists()
        assert "project(BedrockPlugin)" in cmake_lists.read_text(encoding="utf-8")
        assert "LL_REGISTER_PLUGIN(PluginMain);" in main_cpp.read_text(encoding="utf-8")


def test_generate_unknown_platform_raises_clear_error():
    with tempfile.TemporaryDirectory(dir=Path.cwd()) as temp_dir:
        project = Project(name="Unknown", platform="unknown", path=temp_dir)

        with pytest.raises(ValueError, match="Unknown platform"):
            Generator().generate(project)
