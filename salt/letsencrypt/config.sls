# -*- coding: utf-8 -*-
# vim: ft=sls

{% from "letsencrypt/map.jinja" import letsencrypt with context %}

letsencrypt-config:
  file.managed:
    - name: /etc/letsencrypt/cli.ini
    - makedirs: true
    - source: salt://letsencrypt/cli.ini
    - template: jinja
