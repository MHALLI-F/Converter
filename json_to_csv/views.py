from django.shortcuts import render
import pandas as  pd
import csv
from django.http import HttpResponse
from ftplib import FTP
import ftplib
import paramiko, sys
def json_to_csv(request):
    #dt=pd.read_csv("https://firebasestorage.googleapis.com/v0/b/photo-8dc9b.appspot.com/o/Extraction_RMA%20(4).csv?alt=media&token=155d9345-b1c5-46f1-952a-30c2703b9817")
    df=pd.read_json("https://hook.integromat.com/hock73ivs5vj68a4igv4cyg7nhcbhvby")
    #df.to_csv('extraction.csv')
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="Extraction_RMA.csv"'},)
    writer = csv.writer(response)
    writer.writerow(list(df.columns))
   # dt = dt.set_index('id')
   # df = df.set_index('id')
    #for i in range(df.shape[0]):
        
        
     #   dt.loc[i]=df.loc[i]
    for j in  range(df.shape[0]):

        writer.writerow(df.loc[j])
    return response

import psycopg2
import gzip
def jsoncsv(request):

    
    
    conn = psycopg2.connect(host='0.0.0.0', port=5432, dbname='veo' ,user='postgres', password='veosmart2021')
    cur = conn.cursor()

    # export to csv
    fid=open('/home/veosmart_vps/Extaction_RMA_local.csv','w')
    sql = 'COPY (SELECT * FROM public."VEO_veoservices") TO STDOUT  WITH (FORMAT CSV, HEADER, ENCODING "UTF-8");'
    cur.copy_expert(sql, fid)
    fid.close()


    

    transport = paramiko.Transport(('fraude.omegasin.ma', 22))
    transport.connect(username ="veosmart_vps", password = "veosmart@vps")

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put('/home/veosmart_vps/Extaction_RMA_local.csv', '/home/veosmart_vps/Extaction_RMA.csv')
    sftp.close()

    transport.close()
    return render(request,'home.html')



# Create your views here.

def connFTP():
   # host = "41.137.6.162" # adresse du serveur FTP
  #  port = 1125
 #   user = "Veosmart" # votre identifiant
#    password = "$Pass%2022"#/ votre mot de passe
    host = "105.73.80.39" # adresse du serveur FTP
    port = 22
    user = "veosmart_vps" # votre identifiant     
    password = "veosmart@vps"#/ votre mot de passe

    transport = paramiko.Transport((host, port))
    transport.connect(username =user, password =password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    #ftp1 = ftplib.FTP()
    #ftp1.connect(host, port)
    #ftp1.login(user,password)
                
    return sftp
import  os
from django.http import HttpResponse
import pysftp
from django.http import HttpResponseRedirect

def json_to_csv2(request):


    

    return render(request,'home.html')

