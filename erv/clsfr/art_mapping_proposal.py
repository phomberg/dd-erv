import erv.clsfr.feature_extraction as ftrext
import erv.models as models

def get_article_mapping_proposal(article):
    product = ftrext.get_product(article)
    pack_type = ftrext.get_pack_type(article)
    pack_size = ftrext.get_pack_size(article)
    units = ftrext.get_units(article)

    mappings = models.get_article(product, pack_type, pack_size, units)

    art_mappings = {
                    "Article": article
                    ,"Product": product
                    ,"PackType": pack_type
                    ,"PackSize": pack_size
                    ,"Units": units
                    ,"MappingProposals": mappings
                   }

    return art_mappings
