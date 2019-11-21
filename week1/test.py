vpn_vip = {
 'prn1-cmdf-ra-vpn1': ('prnvpn01','prn1-ra-vpn1-cluster'),
 'prn1-cmdf-ra-vpn2': ('prnvpn02','prn1-ra-vpn1-cluster'),
 'prn1-cmdf-ra-vpn3': ('prnvpn03','prn1-ra-vpn1-cluster'),
 'prn1-cmdf-ra-vpn4': ('prnvpn04','prn1-ra-vpn1-cluster'),
 'frc3-b03f24-ra-vpn1': ('frcvpn01',''),
 'frc3-b03b24-ra-vpn2': ('frcvpn02',''),
 'frc3-b03f24-ra-vpn3': ('frcvpn03',''),
 'frc3-b03b24-ra-vpn4': ('frcvpn04',''),
 'sin103-pop-ra-vpn1': ('sinvpn01',''),
 'sin103-pop-ra-vpn2': ('sinvpn02',''),
 'lha2-pop-ra-vpn1': ('lhavpn01',''),
 'lha2-pop-ra-vpn2': ('lhavpn02',''),
 'nrt1-pop-hra-vpn1': ('pekvpn01',''),
 'nrt1-pop-hra-vpn2': ('pekvpn02',''),
 'nrt1-pop-hra-vpn3': ('pekvpn03',''),
 'nrt1-pop-hra-vpn4': ('pekvpn04',''),
}

for k,v in vpn_vip.items():
    print("Key: {}\nValue1: {}\nValue2: {}".format(k, vpn_vip[k][0], vpn_vip[k][1]))
