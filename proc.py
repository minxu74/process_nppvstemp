#!/usr/bin/env python

import glob
import netCDF4 as nc4

dirname='/qfs/people/yang954/script/SPRUCE/process_pft/NPPvsT_PFT_20200524'

treatments=['T0.00', 'T2.25', 'T4.50', 'T6.75', 'T9.00'] 
years=['2016', '2017', '2018']


for gr in range(2):
    with open("nppvstemp_{}.txt".format(gr+1), "w") as fw:
        for yr in years:
            fmtstr = ''
            for tr in treatments:
                fnvar = dirname + '/' + tr + '.NPP.sum.' + yr + '.nc'
                fntmp = dirname + '/' + tr + '_' + yr + '_ann_temp.nc'
                with nc4.Dataset(fnvar, 'r') as fv, nc4.Dataset(fntmp, 'r') as ft:
                     pftstr = '{:9.3f}'.format(ft.variables["TBOT"][gr])
                     for pft in range(fv.dimensions["pft"].size):
                         if fv.variables["pfts1d_ixy"][pft] == gr+1:
                            if fv.variables["NPP_sum"][pft] != fv.variables["NPP_sum"]._FillValue:
                                # pfts1d_itype_veg
                                # print (yr, tr, fv.variables["NPP_sum"][pft], ft.variables["TBOT"][0])
                                pftstr+="{:9.3f}".format(fv.variables["NPP_sum"][pft], ft.variables["TBOT"][gr])
                fw.write("{} {}\n".format(yr, pftstr))
                #fmtstr += pftstr
            print (yr, tr, fmtstr)
            #fw.write("{} {}\n".format(yr, fmtstr))

