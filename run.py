# Copyright (c) 2011 seb26. All rights reserved.
# Source code is licensed under the terms of the Modified BSD License.

import reports
import wconfig

wprefs = {

    'tfwiki': {
        'prefix': 'Team Fortress Wiki:Reports/',
        'summ': 'Updated page.',
        'summ-count': 'Updated page. ({0} articles)',
        'blacklist': [],
        'blacklist-missingArticles': [ 'WebAPI', 'WebAPI/GetPlayerItems', 'WebAPI/GetSchema' ],
        'langs': [ 'ar', 'cs', 'da', 'de', 'es', 'fi', 'fr', 'hu', 'it', 'ja', 'ko', 'nl', 'no', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sv', 'tr', 'zh-hans', 'zh-hant' ]
        },

    'pwiki': {
        'prefix': 'Portal Wiki:Reports/',
        'summ': 'Updated page.',
        'summ-count': 'Updated page. ({0} articles)',
        'blacklist': [],
        'blacklist-missingArticles': [],
        'langs': [ 'ar', 'cs', 'da', 'de', 'es', 'fi', 'fr', 'hu', 'it', 'ja', 'ko', 'nl', 'no', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sv', 'zh-hans', 'zh-hant' ]
        }
}

def run(allArticlesEn=False, allArticles=False, missingArticles=False, doOnly=False):
    if doOnly is not False:
        todo = [ doOnly ]
    else:
        todo = wprefs.keys()
    for wiki in todo:
        c = wprefs[wiki]
        r = reports.report(wiki)
        r.login()
        if allArticlesEn:
            r.allArticlesEn( c['prefix'] + 'All articles/en', c['langs'], c['blacklist'], c['summ-count'])
        if allArticles:
            r.allArticles( c['prefix'] + 'All articles/{0}', c['langs'], c['summ-count'] )
        if missingArticles:
            r.missingArticles(
                c['prefix'] + 'Missing translations/{0}',
                c['langs'],
                c['prefix'] + 'All articles/en',
                c['prefix'] + 'All articles/{0}',
                c['blacklist-missingArticles'],
                c['summ-count']
            )
    print 'run.py > done.'

run(allArticlesEn=True, allArticles=True, missingArticles=True)