const scraper = require('website-scraper');
const scrape = scraper.default || scraper;
const fetch = require('node-fetch'); // we need to install this if not native
const fs = require('fs');

async function doScrape() {
  console.log("Fetching sitemap...");
  const res = await fetch('http://www.rvtr.com/sitemap.xml');
  const xml = await res.text();
  
  // Quick regex to extract <loc> URLs
  const urls = [];
  const regex = /<loc>(.*?)<\/loc>/g;
  let match;
  while ((match = regex.exec(xml)) !== null) {
      urls.push(match[1]);
  }
  
  console.log(`Found ${urls.length} URLs in sitemap.`);
  
  const options = {
    urls: urls,
    directory: './rvtr_site',
    filenameGenerator: 'bySiteStructure',
    urlFilter: (url) => {
       // Only follow internal URLs and the AWS media bucket
       return url.includes('rvtr.com') || url.includes('monograph-media.s3.amazonaws.com');
    },
    request: {
        headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    }
  };

  console.log("Starting full site scrape...");
  try {
      await scrape(options);
      console.log("Scrape completed successfully!");
  } catch(e) {
      console.error("Scrape failed:", e);
  }
}

doScrape();
