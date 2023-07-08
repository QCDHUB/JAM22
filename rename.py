#!/usr/bin/env python
import sys,os
import copy
from subprocess import Popen, PIPE, STDOUT

#--from tools
from tools.tools    import load,save,checkdir,lprint

cwd = os.getcwd()

#--use this to rename the LHAPDF files

if __name__=="__main__":


    wdir = 'pos_gluon'
    #dirname = 'JAM22-FF_hadron_nlo'
    #newname = 'JAM22-FF_hadron_nlo_pos_gluon'
    #dirname = 'JAM22-FF_kaon_nlo'
    #newname = 'JAM22-FF_kaon_nlo_pos_gluon'
    #dirname = 'JAM22-FF_pion_nlo'
    #newname = 'JAM22-FF_pion_nlo_pos_gluon'
    #dirname = 'JAM22-PDF_proton_nlo'
    #newname = 'JAM22-PDF_proton_nlo_pos_gluon'
    dirname = 'JAM22-PPDF_proton_nlo'
    newname = 'JAM22-PPDF_proton_nlo_pos_gluon'

    #wdir = 'neg_gluon'
    #dirname = 'JAM22-FF_hadron_nlo'
    #newname = 'JAM22-FF_hadron_nlo_neg_gluon'
    #dirname = 'JAM22-FF_kaon_nlo'
    #newname = 'JAM22-FF_kaon_nlo_neg_gluon'
    #dirname = 'JAM22-FF_pion_nlo'
    #newname = 'JAM22-FF_pion_nlo_neg_gluon'
    #dirname = 'JAM22-PDF_proton_nlo'
    #newname = 'JAM22-PDF_proton_nlo_neg_gluon'
    #dirname = 'JAM22-PPDF_proton_nlo'
    #newname = 'JAM22-PPDF_proton_nlo_neg_gluon'

    print('\nrenaming LHAPDF tables for %s to %s'%(dirname,newname))
    old = '%s/%s'%(wdir,dirname)
    new = '%s/%s'%(wdir,newname)
    
    checkdir(new)
    F=os.listdir(old)

    cnt=0
    for f in F:
        cnt+=1
        lprint('progress %d/%d'%(cnt,len(F)))
        cmd=['cp','%s/%s'%(old,f),'%s/%s'%(new,f.replace(dirname,newname))]
        p=Popen(cmd,  stdout=PIPE, stderr=STDOUT)
        output = p.stdout.read()
    print








