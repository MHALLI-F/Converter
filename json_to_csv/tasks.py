from __future__ import absolute_import, unicode_literals
from celery import task
from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import datetime
from  datetime import datetime
from time import strftime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .models import *
from django.core.mail import send_mail


@task()
def scheduledTask():
    conn = psycopg2.connect(host='0.0.0.0', port=5432, dbname='veo' ,user='postgres', password='veosmart2021')
    cur = conn.cursor()
    # export to csv
    fid=open('/home/veosmart_vps/extra4.csv','w')
    sql = 'COPY (SELECT * FROM public."VEO_assistance") TO STDOUT  WITH (FORMAT CSV, HEADER, ENCODING "UTF-8");'
    cur.copy_expert(sql, fid)
    transport = paramiko.Transport(('fraude.omegasin.ma', 22))
    transport.connect(username ="veosmart_vps", password = "veosmart@vps")
    sftp.put('/home/veosmart_vps/extra4.csv', '/home/veosmart_vps/Extaction_RMA8.csv')
    sftp.close()
    transport.close()
