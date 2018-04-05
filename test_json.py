json_string = '{"title":"365 days: 2011 in review.","doi":"10.1038/480426a","pmid":"22193080","tq":["Top 40 countries by the number of scientific papers published. Source","Top 40 countries by the number of scientific papers published.","Countries numbers of scientific papers published","Top 40 countries by the number of scientific papers published. Source #dataviz: #science","Countries numbers of scientific papers published: #data on #science"],"ads_id":"2011Natur.480..426V","altmetric_jid":"4f6fa62f3cf058f6100082d3","issns":["0028-0836","1744-7933"],"journal":"news@nature.com","cohorts":{"pub":1917,"sci":350,"com":87,"doc":63},"context":{"all":{"count":9370416,"mean":7.5525844170068,"rank":625,"pct":99,"higher_than":9374411},"journal":{"count":303,"mean":110.46613245033,"rank":1,"pct":99,"higher_than":302},"similar_age_3m":{"count":255184,"mean":5.4346507330036,"rank":5,"pct":99,"higher_than":255179},"similar_age_journal_3m":{"count":132,"mean":109.0693129771,"rank":1,"pct":99,"higher_than":131}},"authors":["Richard Van Noorden","Van Noorden R"],"type":"news","altmetric_id":502878,"schema":"1.5.4","is_oa":false,"cited_by_fbwalls_count":22,"cited_by_feeds_count":5,"cited_by_gplus_count":34,"cited_by_posts_count":2695,"cited_by_tweeters_count":2418,"cited_by_accounts_count":2479,"last_updated":1498437197,"score":1714.702,"history":{"1y":1.35,"6m":0,"3m":0,"1m":0,"1w":0,"6d":0,"5d":0,"4d":0,"3d":0,"2d":0,"1d":0,"at":1714.702},"url":"http://dx.doi.org/10.1038/480426a","added_on":1324491937,"published_on":1324512000,"subjects":["science"],"readers":{"citeulike":"0","mendeley":"95","connotea":"0"},"readers_count":95,"images":{"small":"https://badges.altmetric.com/?size=64&score=1715&types=btttttfg","medium":"https://badges.altmetric.com/?size=100&score=1715&types=btttttfg","large":"https://badges.altmetric.com/?size=180&score=1715&types=btttttfg"},"details_url":"http://www.altmetric.com/details.php?citation_id=502878"}'

import json
parsed_json = json.loads(json_string)

# print parsed_json

print parsed_json['history']['1y'] 

print parsed_json.has_key('cited_by_fbwalls_count')

parsed_json['history']['add'] = 1

print parsed_json['history']['add']