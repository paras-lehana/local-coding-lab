"""Keep reviewed visual evidence from becoming a blanket binary exemption."""
import unittest
from scripts import audit_public


class ReviewedImageTests(unittest.TestCase):
    """An image approval identifies exact reviewed bytes at an exact path."""

    def test_only_reviewed_bytes_pass(self) -> None:
        """Changing a single image byte invalidates the review exemption."""
        for name in audit_public.REVIEWED_IMAGES:
            content = (audit_public.ROOT/name).read_bytes()
            self.assertTrue(audit_public.reviewed_image(name, content))
            self.assertFalse(audit_public.reviewed_image(name, content+b"x"))

    def test_unknown_image_is_not_exempt(self) -> None:
        """Copying approved bytes under another name requires a new review."""
        name = next(iter(audit_public.REVIEWED_IMAGES))
        content = (audit_public.ROOT/name).read_bytes()
        self.assertFalse(audit_public.reviewed_image("unreviewed.png", content))
