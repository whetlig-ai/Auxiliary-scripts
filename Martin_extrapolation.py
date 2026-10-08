import sys
import glob
from numpy import e as e
from numpy import sqrt as sqrt


e4 = 1/(4+1/2)**4
e3 = 1/(3+1/2)**4



basename_list = list(dict.fromkeys(list(map(lambda x: x[:(x.lower().find('ri' or 'ccsd' or '-')-1)], glob.glob('*out')))))
print(basename_list )
out_list = glob.glob('*out')

for basename in basename_list:


    with open(f'{basename}_Neese_cbs.txt', 'w') as base:

        hf_qz = 0
        hf_tz = 0
        ccsdt_qz = 0
        ccsdt_tz = 0
        ccsdt_corr_qz = 0
        ccsdt_corr_tz = 0
        e_cbs = 0

        for out in out_list:
            if f'{basename}-' in out:
                if 'qz' in out.lower():
                    with open(out, 'r') as init:
                        for line in init:
                            if 'Total Energy' in line and 'Eh' in line:
                                hf_qz = float(line.split()[-4])
                            # if 'Final correlation energy' in line:
                            #     ccsdt_corr_qz = float(line.split()[-1])
                            if 'FINAL SINGLE' in line:
                                ccsdt_qz = float(line.split()[-1])

                if 'tz' in out.lower():
                    with open(out, 'r') as init:
                        for line in init:
                            if 'Total Energy' in line and 'Eh' in line:
                                hf_tz = float(line.split()[-4])
                            # if 'Final correlation energy' in line:
                            #     ccsdt_corr_tz = float(line.split()[-1])
                            if 'FINAL SINGLE' in line:
                                ccsdt_tz = float(line.split()[-1])

        ccsdt_corr_tz = ccsdt_tz - hf_tz
        ccsdt_corr_qz = ccsdt_qz - hf_qz

        e_cbs = (ccsdt_tz*e4-ccsdt_qz*e3)/(e4-e3)

        base.write(f'HF_TZ = {hf_tz}\n'
                   f'HF_QZ = {hf_qz}\n'
                   f'CCSDT_TZ_energy = {ccsdt_tz}\n'
                   f'CCSDT_QZ_energy = {ccsdt_qz}\n'
                   f'CCSDT_CORR_TZ = {ccsdt_corr_tz}\n'
                   f'CCSDT_CORR_QZ = {ccsdt_corr_qz}\n'
                   f'E_cbs = {e_cbs}')

