"""Build both editions before the existing deployment audit is allowed to run."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec=importlib.util.spec_from_file_location('book_editions',Path(__file__).resolve().parents[1]/'src/storybuilderbook/editions.py')
editions=importlib.util.module_from_spec(spec);spec.loader.exec_module(editions)

class EditionBuildTests(unittest.TestCase):
    def root(self, folder):
        root=Path(folder).resolve();(root/'book.toml').write_text('[build]\nbuild-dir="gh-pages/docs"\n')
        (root/'editions/bn').mkdir(parents=True);(root/'editions/bn/book.toml').write_text('[book]\nlanguage="bn"\n')
        return root

    def test_builds_english_then_bangla_into_one_deploy_tree(self):
        with tempfile.TemporaryDirectory() as folder,patch.object(editions.subprocess,'run') as run:
            root=self.root(folder);output=editions.build_editions(root)
            self.assertEqual(output,root/'gh-pages/docs')
            self.assertEqual(run.call_args_list[0].args[0],['mdbook','build',str(root)])
            self.assertEqual(run.call_args_list[1].args[0],['mdbook','build',str(root/'editions/bn'),'--dest-dir',str(output/'bn')])

    def test_failed_english_build_stops_before_later_steps(self):
        with tempfile.TemporaryDirectory() as folder,patch.object(editions.subprocess,'run',side_effect=subprocess.CalledProcessError(1,'mdbook')) as run:
            with self.assertRaises(subprocess.CalledProcessError):editions.build_editions(self.root(folder))
            self.assertEqual(run.call_count,1)

    def test_failed_bangla_build_is_not_reported_as_success(self):
        with tempfile.TemporaryDirectory() as folder,patch.object(editions.subprocess,'run',side_effect=[None,subprocess.CalledProcessError(1,'mdbook')]):
            with self.assertRaises(subprocess.CalledProcessError):editions.build_editions(self.root(folder))

if __name__=='__main__':unittest.main()
