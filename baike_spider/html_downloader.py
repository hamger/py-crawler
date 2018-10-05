#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request as req

class HtmlDownloader(object):
  def download(self, url):
    if url is None:
      return None
    
    response = req.urlopen(url)
    if response.getcode() != 200:
      return None
    
    return response.read()