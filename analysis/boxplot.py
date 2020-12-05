import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

gp="""1004.92145823 1007.74813205 1004.82638246 1004.23652736 1004.26703478
 1003.93447562 1003.71804909 1004.4602199  1004.0892737  1006.98950552
 1008.13347376 1008.82617816 1008.49668943 1005.94363241 1008.12318077
 1003.71505591 1008.60761855 1010.14751189 1004.79768882 1003.51884558
 1003.48501905 1007.00841513 1007.15498699 1002.92710895 1007.98500428
 1004.73097732 1005.7068924  1008.06429615 1008.25226875 1004.69652974
 1004.46083546"""
mp_10= """1003.71230743 1003.39109618 1002.86603658 1003.09716119 1006.3435667
 1004.13311453 1003.61236341 1003.02168422 1003.25317709 1002.97665097
 1003.35043242 1003.78788923 1001.72002578 1002.96967068 1003.37527361
 1005.10584612 1003.16226849 1002.73498981 1003.84699051 1004.67325986
 1004.3526509  1003.38015413 1003.48282668 1002.96967068 1004.18485586
 1004.0202895  1003.712091   1002.76696866 1003.26242537 1005.29542878
 1003.40668588"""
mp_15="""1002.99905983 1004.05967982 1003.83819571 1007.34264928 1002.29757375
 1005.69218523 1004.19115723 1003.22406167 1002.66559229 1002.96967068
 1005.48628867 1003.91302371 1004.40808747 1002.26703258 1003.52851059
 1001.62149606 1002.3397849  1002.10428731 1003.22041311 1002.44582739
 1004.55396863 1002.70804265 1004.28579581 1004.25977921 1002.36062163
 1003.22960953 1001.94492839 1002.64186796 1004.18485586 1003.0370076
 1001.92064129"""
mp_20="""1004.18485586 1003.33130033 1002.57638556 1003.42420134 1003.4140062
 1002.83065876 1003.14021919 1003.52932678 1004.63586511 1003.78585923
 1003.01685113 1004.3180602  1003.23164801 1003.82673649 1001.86874741
 1004.11954418 1004.18485586 1003.69400868 1003.84144229 1003.13392229
 1003.15747958 1002.96967068 1003.40782176 1004.62488331 1004.18485586
 1001.49506856 1002.57746499 1004.18485586 1001.47464244 1004.10398702
 1003.24894903
"""
mp_5="""1003.56737975 1003.19267592 1003.01874497 1002.96967068 1006.3908015
 1003.35291106 1003.23828969 1003.75884096 1002.96967068 1003.42710239
 1003.91301894 1003.39279462 1002.96967068 1003.34173037 1002.35916092
 1003.83035239 1003.3557296  1004.05081993 1002.89615293 1003.41881306
 1004.85863524 1006.90726177 1003.2191138  1003.46696599 1004.05071243
 1002.86837095 1002.99125401 1006.47923184 1009.24841529 1006.42240959
 1003.99783804"""
divs=[gp,mp_5,mp_10,mp_15,mp_20]
newdivs=[]
for i in range(len(divs)):
    newdivs.append(list(map(float,list(divs[i].split()))))
sns.boxplot(data=newdivs).set(xlabel="Algorithm",ylabel="Percentage Deviation")
plt.xticks(list(range(5)),["GP","MpEt_125","MpEt_1000","MpEt_3375","MpEt_8000"])
plt.title(("Boxplots of % deviation for different algorithms"))
plt.savefig('../imgs/boxplot.png')
plt.show()