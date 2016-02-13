import subprocess
import unittest


class TestCodeReviewPython(unittest.TestCase):
    def test_informs_user_when_hassattr_is_used_in_python2(self):
        module_under_review = 'module_under_review.py'
        stdout = subprocess.check_output([
            'python',
            'code_review_python.py',
            module_under_review
        ])

        concern = (
            'hasattr should be avoided in Python 2,'
            'see https://hynek.me/articles/hasattr/'
        )
        expexted_message = "{file}:{lineno} {concern}\n".format(
            file=module_under_review,
            lineno=6,
            concern=concern
        )
        self.assertEquals(
            stdout,
            expexted_message
        )
