import re
import erv.clsfr.classifier as classifier

def isfloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def get_product(article):
    return classifier.classify_article(article, "3-gram", "erv/clsfr/erv.clsfr.prod.clsfr.mod", "erv/clsfr/erv.clsfr.prod.vect.mod")


def get_pack_type(article):
    return classifier.classify_article(article, "3&4-gram", "erv/clsfr/erv.clsfr.pckt.clsfr.mod", "erv/clsfr/erv.clsfr.pckt.vect.mod")

    # artPackType = str(article).lower()
    # retPackType = ""

    # mvPackageType = re.findall("(harasse|har|hx)", artPackType)
    # if len(mvPackageType) > 0:
    #     retPackType = "Harasse"

    # mvPackageType = re.findall("(karton|kart|carton|cx|sch\.pack)", artPackType)
    # if len(mvPackageType) > 0:
    #     retPackType = "Tray"
        
    # mvPackageType = re.findall("(container|cont|tank|keg|fass)", artPackType)
    # if len(mvPackageType) > 0:
    #     retPackType = "Tank"

    # mvPackageType = re.findall("(bib|bag in box|box)", artPackType)
    # if len(mvPackageType) > 0:
    #     retPackType = "BagInBox"

    # return retPackType


def get_pack_size(article):
    return classifier.classify_article(article, "3&4-gram", "erv/clsfr/erv.clsfr.pcks.clsfr.mod", "erv/clsfr/erv.clsfr.pcks.vect.mod")
    # artPackSize = str(article).replace('\'','').lower()
    # retPackSize = ""

    # mvPackageSize = re.findall("\d+[\s]?ml(?i)", artPackSize)
    # if len(mvPackageSize) > 0:
    #     retPackSize = float(str(mvPackageSize[0]).replace('ml','').replace(' ',''))

    # mvPackageSize = re.findall("\d.+[\s]?cl(?i)", artPackSize)
    # if len(mvPackageSize) > 0:
    #     retPackSize = float(str(mvPackageSize[0]).replace('cl','').replace(' ','')) * 10

    # mvPackageSize = re.findall("\d.+[\s]?dl(?i)", artPackSize)
    # if len(mvPackageSize) > 0:
    #     retPackSize = float(str(mvPackageSize[0]).replace('dl','').replace(' ','')) * 100

    # mvPackageSize = re.findall("\d.+[\s]?lt(?i)", artPackSize)
    # if len(mvPackageSize) > 0:
    #     retPackSize = float(str(mvPackageSize[0]).replace('lt','').replace(' ','')) * 1000

    # if isfloat(artPackSize):
    #     retPackSize = float(artPackSize) * 10 #--> if no unit-of-measure available, the size value is considered as 'cl'

    # return retPackSize


def get_units(article):
    return classifier.classify_article(article, "3&4-gram", "erv/clsfr/erv.clsfr.unit.clsfr.mod", "erv/clsfr/erv.clsfr.unit.vect.mod")
    # artSalesUnit = str(article).replace('\'','').lower()
    # retSalesUnit = ""

    # mvSalesUnit = re.findall("[x]\s?\d+", artSalesUnit)
    # if len(mvSalesUnit) > 0:
    #     retSalesUnit = int(str(mvSalesUnit[0]).replace('x','').replace(' ',''))

    # mvSalesUnit = re.findall("\d+\s?[x]", artSalesUnit)
    # if len(mvSalesUnit) > 0:
    #     retSalesUnit = int(str(mvSalesUnit[0]).replace('x','').replace(' ',''))

    # if artSalesUnit.isnumeric():
    #     retSalesUnit = int(artSalesUnit)

    # return retSalesUnit
