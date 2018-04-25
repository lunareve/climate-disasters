"""Tests for Zendesk API extension."""

from unittest import TestCase
from server import app
from flask import session

class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_index(self):
        """Test index route."""
        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn("Max 1000 records returned", result.data)


if __name__ == '__main__':

    import unittest
    unittest.main()