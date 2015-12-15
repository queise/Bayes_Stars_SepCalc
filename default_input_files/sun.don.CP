 &NL_CESAM
 NOM_CHEMIN='/local/tmp/jordi/dmp2k/data/', 
 NOM_OUTDIR='/local/tmp/jordi/allst/outputs/',
 NOM_CTES='ctes_94',
 NOM_DES='no_des',
 NOM_OUTPUT='osc_adia',
 N_MAX=1000,
 PRECISION='np' 
 /
 &NL_MASS
 MTOT=MTOTDEFAULT,
 NOM_PERTM='pertm_ext',
 MDOT=0.d0
 /
 &NL_EVOL 
 AGEMAX=AGEMAXDEFAULT,
 ARRET='post',
 DTLIST=1.d10,
 LOG_TEFF=10.d0,
 NB_MAX_MODELES=2000,
 HE_CORE=-1.D0,
 T_STOP=5.d8,
 X_STOP=-0.1d0
 /
 &NL_CHIM
 GRILLE_FIXE=f,
 NOM_ABON='solaire_agss09',
 MODIF_CHIM=.FALSE.,
 GARDE_XISH=.FALSE., 
 X0=X0DEFAULT,
 Y0=Y0DEFAULT,
 ZSX0=0.
 /
 &NL_CONV
 NOM_CONV='conv_jmj',
 ALPHA=1.8d0,
 OVSHTS=0.2d0,
 OVSHTI=0.d0,
 JPZ=F, 
 CPTURB=0.d0,
 LEDOUX=F
 /
 &NL_DIFF
 DIFFUSION=t, 
 NOM_DIFFM='diffm_mp',
 NOM_DIFFT='difft_nu',
 D_TURB=10.d0,
 RE_NU=1.d0,
 NOM_FRAD='no_frad'
 /
 &NL_ROT
 W_ROT=0.d0,
 UNIT='jours', 
 NOM_DIFFW='diffw_0',
 NOM_THW='rot_0',
 NOM_PERTW='pertw_0',
 P_PERTW=0.d0,
 LIM_JPZ=.FALSE.,
 NOM_DES_ROT='no_des'
 /
 &NL_ETAT
 NOM_ETAT='etat_opalZ',
 F_EOS='EOSDEFAULT',7*' '
 /
 &NL_OPA 
 NOM_OPA='opa_yveline',
 F_OPA='opa_yveline_agss09.bin',7*' '
 /
 &NL_NUC
 NOM_NUC='ppcno3a9',
 NOM_NUC_CPL='NACRE',
 MITLER=F
 /
 &NL_ATM
 NOM_ATM='lim_atm',
 NOM_TDETAU='edding',
 TAU_MAX=20.d0,
 LIM_RO=T
 /
&NL_DARKMATTER
 MASSWIMP =  0.,
 SCATCSH =  1.E-44,
 SCATCSH_SD =  1.E-38,
 ANNIHCS =  3.E-26,
 VSUNESCAPE =  618.,
 VSTAR =  220.,
 VWIMPRMS =  270.,
 RHODMHALO =  0./
&NL_DMPPHYSICS
 CAPTURE = 'dsntcapsunnum',
 WPDIST = 'dmdistribution',
 KNUDSEN = 'dmetransport',
 EN_TRANSPORT = 'none',
 EN_PROD = 'none',
 OPA_KLARGE = 'dmklarge',
 OPA_KSMALL = 'dmksmall',
 ANNIHILATION = 'dmannihilation'/
