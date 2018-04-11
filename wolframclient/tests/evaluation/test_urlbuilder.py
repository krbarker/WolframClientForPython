from __future__ import absolute_import, print_function, unicode_literals

import unittest

from wolframclient.evaluation.cloud.cloudsession import URLBuilder, APIUtil
from wolframclient.evaluation.configuration import WolframPublicCloudConfig

class TestURLBuilder(unittest.TestCase):
    def test_append_no_base(self):
        builder = URLBuilder('')
        url = builder.append('http://wolfram.com').append('foo').get()
        self.assertEqual(url, 'http://wolfram.com/foo')

    def test_simple_append(self):
        builder = URLBuilder('http://wolfram.com')
        url = builder.append('foo').get()
        self.assertEqual(url, 'http://wolfram.com/foo')
        
    def test_simple_append_end_slash(self):
        builder = URLBuilder('http://wolfram.com/')
        url = builder.append('foo').get()
        self.assertEqual(url, 'http://wolfram.com/foo')

    def test_simple_append_start_slash(self):
        builder = URLBuilder('http://wolfram.com')
        url = builder.append('/foo').get()
        self.assertEqual(url, 'http://wolfram.com/foo')

    def test_simple_append_two_slash(self):
        builder = URLBuilder('http://wolfram.com/')
        url = builder.append('/foo').get()
        self.assertEqual(url, 'http://wolfram.com/foo')

    def test_extend(self):
        builder = URLBuilder('http://wolfram.com/')
        url = builder.extend('foo','bar','baz').get()
        self.assertEqual(url, 'http://wolfram.com/foo/bar/baz')

    def test_api_url_path(self):
        url = APIUtil.user_api_url('dorianb', 'foo/bar')
        self.assertEqual(url, 'https://www.wolframcloud.com/objects/dorianb/foo/bar')

    def test_api_url_basic(self):
        url = APIUtil.user_api_url('dorianb', 'name')
        self.assertEqual(
            url, 'https://www.wolframcloud.com/objects/dorianb/name')