import nfc
import binascii


nfcobj1 = nfc.clf.RemoteTarget("212F")  # FeliCa
nfcobj2 = nfc.clf.RemoteTarget("106A")  # NFC

while True:
    with nfc.ContactlessFrontend("usb") as clf:
        target = clf.sense(nfcobj1, nfcobj2, iterations=3, interval=1.0)
        while target:
            tag = nfc.tag.activate(clf, target)
            print(tag)
            if tag is None:
                break

            if hasattr(tag, "idm"):
                # Felica
                idm = binascii.hexlify(tag.idm)
                print(idm.decode())
                break
            else:
                # nfc
                records = ",".join([r.text for r in tag.ndef.records])
                print(records)
                break
