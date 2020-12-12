#!/usr/bin/env python3
from selfdrive.car.fingerprints import eliminate_incompatible_cars, all_known_cars
import cereal.messaging as messaging


# rav4 2019 and corolla tss2
fingerprint = {127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1078: 4, 1136: 8, 1151: 6, 1168: 7, 1173: 8, 1183: 8, 1191: 2, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1291: 8, 1292: 8, 1294: 8, 1307: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8, 2004: 8, 2012: 8}

candidate_cars = all_known_cars()


for addr, l in fingerprint.items():
    dat = messaging.new_message('can', 1)

    msg = dat.can[0]
    msg.address = addr
    msg.dat = " " * l

    candidate_cars = eliminate_incompatible_cars(msg, candidate_cars)
    print(candidate_cars)
