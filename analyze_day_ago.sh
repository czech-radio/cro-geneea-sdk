#!/bin/bash
source /root/irozhlas/cro-geneea-sdk/.venv/bin/activate
source /root/irozhlas/cro-geneea-sdk/secret
for i in `find /root/irozhlas/irozhlas-scraper/output/*.txt -newermt $(date +%Y-%m-%d -d '1 day ago') -type f -print`; do
	cro.geneea -i $i -t analysis -f xml;
	sleep 1;
done
mv /root/irozhlas/irozhlas-scraper/output/*.xml /root/irozhlas/irozhlas-scraper/output/xml
