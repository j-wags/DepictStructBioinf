annotations = {}

#### NOTE THAT POSNS USES PYTHON INDEXING - THE FIRST RESIDUE IS 0


annotations['shiv_vif_interact_a3d'] = {'parent':'a3d_ntd',
                                        'label':'Vif Interaction Surface for A3D (Shiv)',
                                        'posns':[i - 1 for i in [128]],
                                        'help':'Shivender: The primary residue implicated for Vif-binding in the case of A3G-NTD is D128 (Huthoff and Malim, 2007, Santa-Marta et al., 2005 and Xu et al., 2004), located on loop 7, which is diametrically opposite the region being discussed (Fig. 5).',
                                        'checkAA':'D'
                                        }


annotations['shiv_vif_interact_a3h'] = {'parent':'a3h',
                                        'label':'Vif Interaction Surface for A3H (Shiv)',
                                        'posns':[i - 1 for i in [121]],
                                        'help':'Shivender: Thus, the role of individual, binding-critical residues, such as D128 in A3G, may be exerted not only by the currently accepted direct interaction of Vif-A3G, but also by indirectly influencing the interaction interface. Similarly, residue E121 in A3H, a critical determinant for Vif binding (Zhen et al., 2012), is located on the a-4 helix and close to loop 7 in the A3H homology model (labeled as K121 in Fig. 5 as the target A3H sequence used for his study is the isoform 1 (NP_001159475.1) sequence). A3H isoforms that contain K105 and E121 are known to show stronger anti-viral activity against HIV-1 (Zhen et al., 2010).',
                                        'checkAA':'K'
                                        }


annotations['aydin_vif_interact_a3c_reg'] = {'parent':'a3c',
                                             'label':'Vif Interaction Surface for A3C (Aydin)',
                                             'posns':[i - 1 for i in [72,75,76,79,80,81,86,106,107,111,129,141]],
                                             'help':'Aydin Table 1:  A3C | I72, 75FCxxILS81, Y86, 106EF107, H111, P129, E141 | Kitamura et al., 2012',
                                             'checkAA':'LFCILSYEFHPE'} # Had to change I72->L 


annotations['aydin_vif_interact_a3d_ctd_reg'] = {'parent':'a3d_ctd',
                                                 'label':'Vif Interaction Surface for A3D CTD (Aydin)',
                                                 'posns':[i-205 for i in [268,271,272,275,276,277,282,302,303,307,337]], #figure out this offset for aydin domains
                                                 'help':'Aydin Table 1:  A3D-CTD | L268, 271FC272, 275ILS277, Y282,302EF303, H307, E337 | Kitamura et al., 2012',
                                                 'checkAA':'LFCILSYEFHE'}


annotations['aydin_vif_interact_a3f_ctd_reg'] = {'parent':'a3f_ctd',
                                                 'label':'Vif Interaction Surface for A3F CTD (Aydin)',
                                                 'posns':[i-192 for i in [255,258,259,264,269,290,294,286,289,316,320,324]], #figure out this offset for aydin domains
                                                 'help':'Aydin Table 1:  A3F-CTD | L255, 258FC259, S264, Y269, F290, H294, E286, E289, E316, S320, E324 | Albin et al., 2010, Kitamura et al., 2012, Siu et al., 2013 and Smith and Pathak, 2010',
                                                 'checkAA':'LFCSYFHEEESE'}


annotations['aydin_vif_interact_a3g_ntd_reg'] = {'parent':'a3g_ntd',
                                                 'label':'Vif Interaction Surface for A3G NTD (Aydin)',
                                                 'posns':[i - 1 for i in [128,129,130]],
                                                 'help':'Aydin Table 1:  A3G-NTD | 128DPD130 | Huthoff and Malim, 2007, Lavens et al., 2010,Mangeat et al., 2004 and Schrofelbauer et al., 2004',
                                                 'checkAA':'DPD'}


annotations['aydin_ssdna_interact_a3a'] = {'parent':'a3a',
                                           'label':'ssDNA Interaction Surface for A3A (Aydin)',
                                           'posns':[i - 1 for i in [57,70,72,102,103,104,105,133,135,138]],
                                           'help':'Aydin Table 3:  A3A | N57, H70, E72, 102FSWG105, D133, L135, E138 | Byeon et al., 2013',
                                           'checkAA':'NHEFSWGDLE'}



annotations['aydin_ssdna_interact_a3f_ctd'] = {'parent':'a3f_ctd',
                                               'label':'ssDNA Interaction Surface for A3F CTD (Aydin)',
                                               'posns':[i-192 for i in [277,305,307,308,309,310,313,316,367,369]],
                                               'help':'Aydin Table 3:  A3F | W277, 305RxYYFW310, 313DY314, K367, Q369 | Siu et al., 2013 ', 
                                               'checkAA':'WRYYFWDYKQ'}



annotations['aydin_ssdna_interact_a3g_ctd_brim_chen'] = {'parent':'a3g_ctd',
                                                         'label':'"Brim"/Chen ssDNA Interaction Surface for A3G CTD (Aydin)',
                                                         'posns':[i-197 for i in [213,215,254,256,259,285,288,291,313,314,315,320,367]], 
                                                         'help':'Aydin Table 3:  A3G: brim model | 213RxR215, 254ExR256, E259, W285, C288, C291, 313RIY315, R320, H367 | Chen et al., 2008', 
                                                         'checkAA':'RREREWCCRIYRH'}



annotations['aydin_ssdna_interact_a3g_ctd_straight_furukawa'] = {'parent':'a3g_ctd',
                                                                 'label':'"Straight"/Furukawa ssDNA Interaction Surface for A3G CTD (Aydin)',
                                                                 'posns':[i-197 for i in [198,204,208,215,238,240,242,243,246,254,256,257,260,261,262,263,265,266,271,272,274,275,278,283,284,305,306,316,319,337,348,351,352,362]], # Cut out 195
                                                                 'help':'Aydin Table 3:   A3G: straight model | 196SxD198, F204, N208, R215, R238, G240, 242LC243, A246, 254ExRH257,260LCFLxVI266, 271LDxDQ275, R278, 283TS284, 305VS306, D316, G319, I337, D348, 351VD352, D362 | Furukawa et al., 2009',
                                                                 'checkAA':'DFNRRGLCAERHLCFLVILDDQRTSVSDGIDVDD'}

                                                                 #'posns':[i-195 for i in [195,198,204,208,215,238,240,242,243,246,254,256,257,260,261,262,263,265,266,271,272,274,275,278,283,284,305,306,316,319,337,348,351,352,362]],
                                                                 #'checkAA':'SDFNRRGLCAERHLCFLVILDDQRTSVSDGIDVDD'}



annotations['aydin_ssdna_interact_a3g_ctd_kinked_holden'] = {'parent':'a3g_ctd',
                                                             'label':'"Kinked"/Holden ssDNA Interaction Surface for A3G CTD (Aydin)',
                                                             'posns':[i-197 for i in [211,213,216,244,257,285,313,315,316,317,318,320,374,376]], 
                                                             'help':'Aydin Table 3:   A3G: kinked model | 211WxR213, H216, N244, H257, W285, 313RxYDDQ318, R320, 374RxR376 | Holden et al., 2008', 
                                                             'checkAA':'WRHNHWRYDDQRRR'}


annotations['aydin_rna_interact_a3g_ntd'] = {'parent':'a3g_ntd',
                                             'label':' RNA Interaction Surface for A3G NTD (Aydin)',
                                             'posns':[i - 1 for i in [24,30,65,94,97,124,127]],
                                             'help':'Aydin: A large pocket within A3G-NTD was identified as both a RNA binding and oligomerization site (Huthoff et al., 2009). Mutations to critical residues forming this pocket in both the A3G-NTD (R24, R30, H65, W94, C97, Y124, and W127) (Figure 6) and A3C (R122) resulted in reduced packaging and impaired antiviral activity due to inefficient RNA binding (Belanger et al., 2013, Bulliard et al., 2009, Friew et al., 2009, Huthoff et al., 2009 and Stauch et al., 2009). With the exception of R24 and W127, these residues are conserved in all A3 domains, indicating that a common RNA binding site might be conserved across A3 proteins.',
                                             'checkAA':'RRHWCYW'}


annotations['aydin_rna_interact_a3c'] = {'parent':'a3c',
                                         'label':' RNA Interaction Surface for A3C (Aydin)',
                                         'posns':[i - 1 for i in [122]],
                                         'help':'Aydin: A large pocket within A3G-NTD was identified as both a RNA binding and oligomerization site (Huthoff et al., 2009). Mutations to critical residues forming this pocket in both the A3G-NTD (R24, R30, H65, W94, C97, Y124, and W127) (Figure 6) and A3C (R122) resulted in reduced packaging and impaired antiviral activity due to inefficient RNA binding (Belanger et al., 2013, Bulliard et al., 2009, Friew et al., 2009, Huthoff et al., 2009 and Stauch et al., 2009). With the exception of R24 and W127, these residues are conserved in all A3 domains, indicating that a common RNA binding site might be conserved across A3 proteins.',
                                         'checkAA':'R'}



annotations['test1'] = {'parent':'a3a',
                       'label':'Test Region',
                       'posns':[9,10,11,12,13,14,15],
                       'checkAA':'RHLMDPH',
                       'help':'An arbitrary region of the human A3A sequence.'
                       }
annotations['test2'] = {'parent':'a3g_ctd',
                       'label':'Another Test Region',
                       'posns':[i-197 for i in [297,301,303,334]],
                       'checkAA':'KKKK',
                       'help':'Another arbitrary region, this time in the A3G C terminal domain'
                       }


annotations['zn_coordinating'] = {'parent':'a3g_ctd',
                                  'label':'Zinc-coordinating amino acids',
                                  'posns':[i-197 for i in [288,257,291]],
                                  'checkAA':'HCC',
                                  'help':'Zinc-coordinating amino acids. Mainly used for check correctness of sequence alignments.'
                                  }
annotations['trp_by_catalytic_site'] = {'parent':'a3g_ctd',
                                        'label':'Tryptophan by catalytic pocket',
                                        'posns':[i-197 for i in [285]],
                                        'checkAA':'W',
                                        'help':'Trp near the catalytic site. Mainly used for check correctness of sequence alignments.'
                                  }

annotations['asp_314_in_a3b_ctd'] = {'parent':'a3b_ctd',
                                     'label':'Asp314 in A3Bctd',
                                     'posns':[i-192 for i in [314]],
                                     'checkAA':'D',
                                     'help':'Aspartate which has been shown to be important for -1 base specificity.'
                                  }



# Template
'''
annotations[''] = {'parent':'',
                   'label':''
                   'posns':[],
                   'help':'',
                   'checkAA':''}
'''
