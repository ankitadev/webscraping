import requests
import io
from lxml import etree
import pandas as pd

cookies = {
    "__RequestVerificationToken": "LQ-rjWV1DpCIPXeTx6m3ccu3n7b9q3fboP0H5CQPtTOENfLm3rVcnlSAjvYJP-McTo8Yj6JKCVduxdJMAowKRxaTWGQ1",
    "_ga": "GA1.2.1306214453.1531244122",
    "_gat": "1",
    "_gid": "GA1.2.1168674989.1531244122",
    "ai_session": "TBRoj|1531244123340|1531245886599.6",
    "ai_user": "ZWC+B|2018-07-10T17:35:22.439Z",
    "incap_ses_220_1000181": "wAXBGvhukCs+s+rIZKMNA1juRFsAAAAApWwPx0E5ypsXnlQIoE6ipg==",
    "nlbi_1000181": "+mNaU2JPKTjqSOy515tZWQAAAAC97hLdMXG7NXy0NVVyxE3O",
    "visid_incap_1000181": "Pvh8BpJjRa6RdgHrBq0bwVjuRFsAAAAAQUIPAAAAAAAJFM5KKS3UYlXYF1BOgmqL"
}


def criteria(entity_id):
    return 'C' + entity_id[1:]


def get_search(entity_id):
    response = requests.get(
        url='https://businesssearch.sos.ca.gov/CBS/SearchResults',
        params={
            'SearchType': 'NUMBER',
            'SearchCriteria': criteria(entity_id),
            'SearchSubType': 'Exact',
        },
        cookies=cookies
    )
    return response.text


def get_token(entity_id):
    html = get_search(entity_id)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(io.StringIO(html), htmlparser)
    elts = tree.xpath('//*[@id="formSearchResults"]/input[1]')
    assert len(elts) == 1
    elt = elts[0]
    assert elt.attrib['name'] == '__RequestVerificationToken'
    return elt.attrib['value']


def get_detail(entity_id):
    token = get_token(entity_id)
    response = requests.post(
        url="https://businesssearch.sos.ca.gov/CBS/Detail",
        data={
            '__RequestVerificationToken': token,
            'SearchType': 'NUMBER',
            'SearchCriteria': criteria(entity_id),
            'SearchSubType': 'Exact',
            'enitityTable_length': '10',
            'EntityId': entity_id,
        },
        cookies=cookies
    )
    return response.text


def get_info(entity_id):
    # I'm just going to pull the table of documents but you can parse
    # the result of the html in this function.
    html = get_detail(entity_id)
    documents = pd.read_html(html)[0]
    return documents


# Make sure things are working
for entity_id in ['00400000', '00303928']:
    info = get_info(entity_id)
    print(info)