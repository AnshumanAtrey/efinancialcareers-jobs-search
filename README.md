# eFinancialCareers Jobs Scraper & API - Banking & Quant Jobs

eFinancialCareers jobs scraper and API: search every job on efinancialcareers.com, the job board for finance, banking and quant roles, in every country at once, live, and get each job's title, company, place, contract type, sectors, pay as shown and as numbers, whether a recruitment agency posted it, skills, first posting date and link, newest first. Turn on full details for the description, the employer's own apply link and the job reference.

Use it as an eFinancialCareers API with no login, an efinancialcareers.com scraper for finance jobs, banking jobs, quant jobs, hedge fund, investment banking, risk and compliance jobs in London, New York, Singapore, Hong Kong, Frankfurt or Zurich, or a daily job feed from the Apify Console, the Apify API, Python, JavaScript, n8n, Make or an AI agent over MCP, and export JSON, CSV or Excel. It reads the same public JSON APIs that efinancialcareers.com's own pages call. Available as an [Apify Actor](https://apify.com/anshumanatrey/efinancialcareers-jobs-search). $0.000023 per job, $0.000034 with full details, $0.0021 per run start, no login, no API key.

**Use it from an AI assistant:**

- **Claude** (claude.ai and the desktop app): [Add eFinancialCareers Jobs to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=eFinancialCareers%20Jobs&connectorUrl=https%3A%2F%2Fmcp.apify.com%3Ftools%3Danshumanatrey%2Fefinancialcareers-jobs-search), click Continue, sign in to Apify, Allow, and ask in plain words.
- **All 18 job boards at once:** [Add Global Job Search to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Global%20Job%20Search&connectorUrl=https%3A%2F%2Fmcp.apify.com%3Ftools%3Danshumanatrey%2Fglobal-job-search-api): one connector to [Global Job Search API](https://apify.com/anshumanatrey/global-job-search-api), which searches this board and 17 more in one run, worldwide and remote, newest first, each job once.
- **Claude Code:** `claude mcp add --transport http efinancialcareers-jobs-search "https://mcp.apify.com?tools=anshumanatrey/efinancialcareers-jobs-search"`, then run `/mcp` to sign in to Apify.
- **Codex:** `codex mcp add efinancialcareers-jobs-search --url "https://mcp.apify.com?tools=anshumanatrey/efinancialcareers-jobs-search"`, then `codex mcp login efinancialcareers-jobs-search`.
- **Any other MCP client:** `https://mcp.apify.com?tools=anshumanatrey/efinancialcareers-jobs-search`, signed in with Apify or an `Authorization: Bearer <APIFY_TOKEN>` header.

## What does it do?

- **Searches every eFinancialCareers country site at once.** On 2026-11-10 the site listed about 70,400 open jobs in 66 countries: Europe 40,000 (the UK 11,500, Germany 9,900, France 9,100), North America 18,700, Asia 9,650 (India, Hong Kong, Singapore), Australia 1,200 and the Gulf 790. One run reads them all, or the places you type.
- **New jobs, not reposted ones.** eFinancialCareers moves paid jobs back to the top of its list every 6 days, so its newest jobs are often weeks old: of 196 jobs listed one morning, 90 had been posted before. Each row's `postedAt` is the job's first posting, the date its own page gives Google, and newest first and Posted in the last use it. `refreshedAt` keeps the date the site last moved it up.
- **Expired jobs left out.** The site's search still lists jobs whose own page says they expired (44 of 1,000 on 2026-11-10). Every job is opened before it is saved, so those never reach your rows.
- **Agency or employer on every row.** `agency` is true when the company that posted the job is filed under HR & Recruitment on eFinancialCareers (Robert Half, Hays, Selby Jennings, Morgan McKinley, and platforms that post for employers), false for any other industry, and `postedBy` names that company.
- **The site's own filters.** Sector (36, such as Quantitative Analytics, Investment Banking, Hedge Funds, Private Equity), seniority (intern to C-suite, named on each row), contract type, remote or office, minimum pay in any currency, and company.
- **One keyword is enough.** Type a job title and press Start, or type it the way you would in the site's box: risk manager in Zurich. Leave the form empty for the newest jobs of every kind.
- **Checks job links.** Paste eFinancialCareers job links from any country site, and each comes back open, closed or not found.

## How is it different from other eFinancialCareers scrapers?

- **The real posting date.** The other actors in the table below give the date the site last moved a job to the top, so a daily "last 24 hours" run brings back jobs posted weeks ago every 6 days. This actor dates each job by its first posting, as the job's page tells Google, and keeps the other date in `refreshedAt`.
- **Every country in one run.** Others search one country per run (blackfalcondata: United States unless you pick one), one region (solidcode: US by default) or a list of five markets (unfenced-group). This actor reads every country unless you type places, and several places at once.
- **No expired jobs.** About 4% of the jobs the site lists have expired pages; this actor drops them, the others deliver them.
- **Agency flag, seniority on the row, sectors by name.** Whether an agency posted the job, the seniority level you filtered by, and sectors as the site names them (Quantitative Analytics: Equity).
- **You pay for what you get.** One charge per delivered row, plus the run start, and a spending limit stops the run cleanly with the jobs it paid for.

Every actor on the Apify Store that names eFinancialCareers in its title or slug and had 5 or more users in the last 30 days on 2026-11-10, ordered by users, as each one's listing and input form state it:

| Feature | blackfalcondata | shahidirfan | solidcode | easyapi | unfenced-group | This actor |
|---|---|---|---|---|---|---|
| Users, 30 days | 27 | 27 | 17 | 8 | 5 | new |
| Countries a run | 1, US by default | by location | 1 region, US by default | your search links | 5 markets by default | all 66, or the places typed |
| Posting date | site's listing date | site's listing date | site's listing date | site's listing date | site's listing date | first posting (and the listing date) |
| Reposted jobs | flagged across runs | no | no | no | flagged across runs | dated by first posting in every run |
| Expired jobs left out | no | no | no | no | no | yes |
| Agency or employer | no | no | no | no | no | yes, from the site's company profile |
| Seniority filter | no | no | no | no | no | yes |
| Job link check: open, closed or not found | no | no | no | no | no | yes |

## When should I use it?

- **Job seekers:** new quant, risk, compliance, investment banking and asset management jobs by title, city, sector and seniority, on a daily schedule, with pay where it is shown.
- **Recruiters and staffing firms:** which banks, funds and fintechs hire for a role right now, where, and at what level; and with No agency jobs, the roles employers post themselves.
- **Sales and market research:** finance companies hiring, as a buying signal, and demand by sector and city.
- **Data teams and AI agents:** one clean, stable feed of eFinancialCareers jobs through the API or MCP.

## How much does it cost to scrape eFinancialCareers jobs?

Pay per event: $0.023 per 1,000 jobs, or $0.034 per 1,000 with full details, plus $0.0021 per run at the default 512 MB. Apify's free $5 monthly credit covers about 113,000 jobs in runs of 100. Platform usage is included, and there is no monthly fee.

| Event | Price | When it is charged |
|---|---|---|
| Job | $0.000023 | One saved job, and one checked link that is closed or not found |
| Job with details | $0.000034 | One saved job with full details on |
| Run start | $0.0021 per GB of memory | Charged by Apify when a run starts: once up to 1 GB and once more for each extra GB, so $0.0021 at the default 512 MB |

eFinancialCareers Jobs Scraper's Apify Store header shows the lowest discount-tier price, the GOLD price: $0.016 per 1,000 jobs. FREE users (Apify's Free plan) pay $0.000023 a job and $0.000034 with full details, BRONZE (Starter) $0.000022 and $0.000033, SILVER (Scale) $0.000019 and $0.000027, and GOLD (Business) and the enterprise tiers $0.000016 and $0.000023. Each price is what that row costs on Apify at that plan's own rates, measured on Apify runs, plus a markup of 100% on the Free plan that falls to 85% on Business. The run start is a flat fee on every plan, $0.0021 per GB of memory, and the header never shows it.

| Run (Free plan price, default memory) | Cost |
|---|---|
| 100 newest jobs | $0.0044 |
| 100 jobs with full details | $0.0055 |
| 1,000 jobs | $0.025 |
| 10,000 jobs, the most one eFinancialCareers search shows | $0.23 |

Number of jobs (`maxJobs`) and the run start set the most a run can cost, and a run stops at its spending limit with a message saying so.

## How does the price compare with other eFinancialCareers scrapers?

Every actor on the Apify Store that names eFinancialCareers in its title or slug and had 5 or more users in the last 30 days, found by searching the Store for 13 eFinancialCareers and finance job terms on 2026-11-10 (29 eFinancialCareers actors read), ordered by users. Free-plan prices from each actor's current pricing.

| Actor | Users, 30 days | Per job | Start fee | Input |
|---|---|---|---|---|
| blackfalcondata/efinancialcareers-scraper | 27 | $0.00095 | $0.01 | Keyword, one country, search links |
| shahidirfan/eFinancialCareers-Jobs-Scraper | 27 | $0.001 | $0.00005 | Keyword and location |
| solidcode/efinancialcareers-scraper | 17 | $0.0012 | $0.00005 | Keywords, region, sector, filters |
| easyapi/efinancialcareers-jobs-scraper | 8 | $0.00299 | $0.09 | Search links |
| unfenced-group/efinancialcareers-scraper | 5 | $0.00089 | $0.001 | Keyword, markets, filters |
| This actor | new | $0.000023, $0.000034 with details | $0.0021 per GB | One keyword or none, every country |

## Which inputs does it take?

Nothing is required. Type a job title and press Start, or press Start with the form empty.

| Field | What it does |
|---|---|
| Job titles to find (`searchTerms`) | One per line. A job matches when its title has every word: quant finds Quant Researcher and Senior Quant. "risk manager in Zurich" reads Zurich as the place. A pasted eFinancialCareers search link works too |
| Where the job is (`location`) | Cities, countries or regions: London, New York, Singapore, Hong Kong, Germany, EMEA, Gulf. Empty is every country |
| Job sector (`sector`) | The site's sectors: quant, investment-banking, asset-management, hedge-funds, private-equity, risk, compliance and the rest |
| Seniority level (`seniority`) | intern-graduate, junior, analyst, associate, avp-senior, vp, svp-head, director, managing-director, c-suite. Each row names its level |
| Posted in the last (`postedWithin`) | 24 hours, 3 days, 7 days, 30 days (the default), any time, or your own period such as 48 hours, by first posting |
| Number of jobs (`maxJobs`) | How many, newest first: 100 by default, 0 for every match |
| Full details (`includeDetails`) | Adds the description as text and HTML, the employer's own apply link, the job reference, and the city, region and country |
| Job type (`employmentType`) | full-time, part-time, contract, intern, temporary |
| Remote or office (`workType`) | remote, hybrid, onsite, where eFinancialCareers states it (about 1 job in 25) |
| Minimum pay (`minSalary`) | The lowest yearly pay with its currency: £100k, 150000 USD, HK$1m |
| Pay currency (`salaryCurrency`) | The currency of Minimum pay when you typed a number alone |
| No agency jobs (`excludeAgencies`) | Leaves out jobs posted by companies the site files under HR & Recruitment |
| Leave out words (`excludeTerms`) | Drops jobs whose title has these words, such as intern |
| Match full text (`searchDescriptions`) | Keeps every job the site's own search finds for your words, also in descriptions |
| Only these companies (`companies`) | Company names (Goldman Sachs, Citi) or company page links. Empty searches everyone |
| Job links to check (`jobUrls`) | Paste job links to check whether they are still open, instead of searching |

Example input:

```json
{
  "searchTerms": ["quant"],
  "location": ["London", "New York"],
  "sector": ["hedge-funds"],
  "postedWithin": "7 days",
  "maxJobs": 100
}
```

## What does the output look like?

One row per job, newest first by first posting. These rows are from a run of the example input (quant) on 2026-11-10: 650 jobs read, at least 172 matching at 43 companies, the 100 newest saved in 21 s.

| Job title (`title`) | Company name (`company`) | Main location (`location`) | Contract type (`contractType`) | Pay as shown (`salary`) | Posted by an agency? (`agency`) | First posted (`postedAt`) |
|---|---|---|---|---|---|---|
| Quant Research Analyst - Spec Fin / Securitization | PIMCO | Newport Beach, United States | Permanent | $ 205,000.00 - $ 305,000.00 |  | 2026-11-10 |
| Alternative Data Quant Researcher | Selby Jennings | New York, United States | Permanent | USD400000 - USD700000 per year | true | 2026-11-09 |
| Quant Trader | Citi | Hong Kong | Permanent | Competitive | false | 2026-11-09 |
| Senior Quant - Equity/FX Derivatives & Volatility | Barclay Simpson | London, United Kingdom | Permanent | £160k - £180k | false | 2026-11-08 |
| KDB+ Quant Developer (1 year contract) | Hays | Hong Kong | Contract | Competitive | true | 2026-11-07 |

One row as JSON:

```json
{
  "title": "Alternative Data Quant Researcher",
  "company": "Selby Jennings",
  "location": "New York, United States",
  "workType": "hybrid",
  "employmentType": "full-time",
  "salary": "USD400000 - USD700000 per year",
  "postedAt": "2026-11-09T23:07:36Z",
  "expiresAt": "2026-12-09T23:45:00Z",
  "jobUrl": "https://www.efinancialcareers.com/jobs-United_States-NY-Manhattan-Alternative_Data_Quant_Researcher.id24985574",
  "applyUrl": "https://www.efinancialcareers.com/jobs-United_States-NY-Manhattan-Alternative_Data_Quant_Researcher.id24985574",
  "status": "open",
  "platform": "efinancialcareers",
  "companySlug": "Selby-Jennings",
  "jobId": "24985574",
  "checkedAt": "2026-11-10T10:52:29+00:00",
  "salaryMin": 400000,
  "salaryMax": 700000,
  "salaryCurrency": "USD",
  "contractType": "Permanent",
  "seniority": null,
  "sectors": ["Quantitative Analytics: Equity", "Hedge Funds: IT/Quant", "Hedge Funds: Research Analysis"],
  "skills": [],
  "agency": true,
  "postedBy": "Selby Jennings",
  "postedByIndustry": "HR & Recruitment",
  "summary": "This Alternative Data Quant Researcher/Data Scientist role sits within the pod of a top-performing Equity Long/Short Portfolio Manager at a New York City hedge fund.",
  "refreshedAt": "2026-11-09T23:07:36Z"
}
```

Full details add `description`, `descriptionHtml`, `reference`, `city`, `region`, `country` and `countryCode`, and give the employer's own apply link (Workday, iCIMS, Lever) in `applyUrl` when the job is applied for there. A checked link that is closed or not found comes back with its `status` and link, and the other fields empty. A run also writes an `OUTPUT` record: how many jobs were read, matched and saved, the checked links, any notes on how your input was read, and the settings and filters sent to eFinancialCareers.

## How fast is it?

Measured on Apify at the default 512 MB on 2026-11-10: the example input (quant) took 5 s, the empty form 4 s, compliance in Singapore 3 s, quant with full details 10 s, part-time or temporary jobs in London 9 s, and 1,000 jobs 126 s (8 rows a second) with a memory peak of 136 MB. eFinancialCareers answered in 0.05 to 1.2 s a call depending on the minute, so the example took 4 s in one 1 GB run and 21 s in another. Each job is opened once to read its first posting, about 2 to 4 jobs read for every one saved, because so many of the site's newest jobs are reposts.

## Common questions

### Which posting date does it use?

eFinancialCareers Jobs Scraper uses each job's first posting, `allocation_date` on the site, which is the `datePosted` its own job page gives Google. The site shows two later dates: its search list sorts by the last time it moved a job back to the top (paid jobs move every 6 days), which this actor keeps in `refreshedAt`, and the job page says "Posted 6 days ago" from the posting before that. Newest first and Posted in the last (`postedWithin`) use the first posting, so a job posted in July and moved to the top today is not a new job here.

### Is eFinancialCareers the same on every country site?

Yes. efinancialcareers.com, .co.uk, .sg, .hk, .de, .fr, .ch, -gulf.com and the other country sites show one set of jobs: each site lists its own country first, but every site holds all about 70,400. eFinancialCareers Jobs Scraper reads them all in one search, newest first across every country, and job links from any of the sites work.

### How do I tell recruitment agencies from employers?

Every row has `agency`, `postedBy` and `postedByIndustry`, from the company profile the job's own page shows. `agency` is true when eFinancialCareers files that company under HR & Recruitment (recruitment agencies such as Robert Half, Hays, Selby Jennings and Morgan McKinley, and platforms such as Workwise that post for employers under the employer's name), false for any other industry, and empty when the company has no profile there. Of the 1,000 newest jobs saved on 2026-11-10, 82 came from such agencies and platforms, 87 from companies in other industries and 831 from companies with no profile, mostly employers' own career-site feeds but also agencies such as Michael Page; for quant jobs, where agencies are busy, 56 of 100 were marked true. Tick No agency jobs (`excludeAgencies`) to leave out the ones marked true.

### How do sector and seniority work?

Job sector (`sector`) and Seniority level (`seniority`) are eFinancialCareers' own filters, sent to its search, so they find what the site files under them. Each row names its sectors as the site does, with the sub-sector after a colon. The site does not show a job's seniority, so a run that filters by it searches each level apart and names the level on each row; without that filter `seniority` stays empty.

### What does remote mean on eFinancialCareers?

eFinancialCareers states remote, hybrid or in-office on about 1 job in 25, so Remote or office (`workType`) keeps only those jobs, and a job whose title or place says remote. Remote typed as a place asks for remote jobs too.

### What if a search finds nothing?

eFinancialCareers Jobs Scraper says why in the run's message and in its `OUTPUT` record, and charges only the run start. When eFinancialCareers' own search has no job with your words inside your place, sector, seniority or other filters, the message says so; when jobs with your words were left out by a filter checked here, it names the filter and how to loosen it, such as the 30-day period for a job first posted earlier.

### Does it need a login or an API key?

eFinancialCareers Jobs Scraper needs no eFinancialCareers login and no API key, because it reads the public JSON APIs that efinancialcareers.com's own pages call, which serve what any visitor sees. You need only an Apify account.

### How often should I run it?

Running eFinancialCareers Jobs Scraper once a day keeps a job feed fresh: set Posted in the last (`postedWithin`) to 24 hours and Number of jobs (`maxJobs`) to 0 to get every job first posted that day, about 3,500 on a weekday. Set the run up under Schedules in Apify Console, and match rows on `jobId` to skip jobs you already have.

### How do I check a list of job links?

eFinancialCareers Jobs Scraper checks whether eFinancialCareers job links are still open when you paste them into Job links to check (`jobUrls`), one per line, instead of searching. Links from every country site work. Each link comes back as one row: open with the job's fields, closed (expired), or not found.

### How do I call it from the API, Python, JavaScript, n8n or an AI agent?

eFinancialCareers Jobs Scraper runs from the Apify API, Python, JavaScript, n8n, Make or an AI agent over MCP. Each way uses your Apify token (Apify Console, Settings, API & Integrations) and takes the input as JSON keyed by the field names, such as `searchTerms` and `maxJobs`.

**API.** One call runs the actor and returns its rows. Apify stops that wait after 300 seconds, which covers most searches; a client below waits as long as a run takes.

```bash
curl -X POST "https://api.apify.com/v2/acts/anshumanatrey~efinancialcareers-jobs-search/run-sync-get-dataset-items" \
  -H "Authorization: Bearer <YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["quant"], "location": ["London"]}'
```

**Python** (`pip install apify-client`):

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("anshumanatrey/efinancialcareers-jobs-search").call(run_input={"searchTerms": ["quant"]})
for row in client.dataset(run.default_dataset_id).iterate_items():  # apify-client 3+; on 2.x use run["defaultDatasetId"]
    print(row["title"], row["company"], row["location"], row["salary"], row["agency"], row["jobUrl"])
```

**JavaScript** (`npm install apify-client`):

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: '<YOUR_APIFY_TOKEN>' });
const run = await client.actor('anshumanatrey/efinancialcareers-jobs-search').call({ searchTerms: ['quant'] });
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) console.log(row.title, row.company, row.location, row.salary, row.agency, row.jobUrl);
```

**n8n and Make.** In n8n, add the Apify node, pick Run an Actor and get dataset, choose this actor and paste the input JSON: the rows come out as n8n items. In Make, the Apify app's Run an Actor and Get Dataset Items modules do the same.

**AI agents (MCP).** Add `https://mcp.apify.com?tools=anshumanatrey/efinancialcareers-jobs-search` to your MCP client and sign in with Apify, or send `Authorization: Bearer <YOUR_APIFY_TOKEN>`. The agent gets this actor as a tool and sees every input field by its JSON key.

### Am I charged for expired jobs?

eFinancialCareers Jobs Scraper charges for an expired job only when you paste its link to check. A search returns open jobs only: an expired job the site still lists is left out and not charged. A pasted link that turns out closed or not found is one Job row, because it was checked and answered.

### Is it legal to use?

eFinancialCareers Jobs Scraper reads public job postings, and it is an independent tool, not affiliated with or endorsed by eFinancialCareers. You are responsible for how you use the data, including eFinancialCareers' terms and the privacy laws that apply to you.

## Limitations

- Pay: 82% of jobs show Competitive; `salaryMin` and `salaryMax` are filled when the job shows its pay (about 8%). A pay amount the employer entered but hides stays hidden, as on the site, and no pay period is stored.
- Work arrangement (remote, hybrid, in the office) is stated on about 1 job in 25.
- `agency` is empty when the posting company has no profile on eFinancialCareers (831 of the 1,000 newest jobs on 2026-11-10), and some agencies are among those.
- Seniority is named on a row only when the run filters by it.
- With words, eFinancialCareers ranks the titles that hold them together first, and its pages are read until one holds no title match: a title that holds the words apart, far down its ranking, can be missed (12 of 2,305 title matches over 8 common searches on 2026-11-10, such as "Business Analyst - Market Risk" for risk analyst).
- One eFinancialCareers search reaches 10,000 jobs; a bigger one says so and asks for a place, sector or seniority.
- A city is searched with the site's own radius and then kept only when the job is in the city typed: Zurich keeps Zurich, not Zug.
- A job a company posts twice with the same title at the same place is delivered once.

## Who maintains it?

Built and maintained by **Anshuman Atrey** ([@AnshumanAtrey](https://github.com/AnshumanAtrey)), who publishes a portfolio of data and OSINT actors on Apify Store. For a feature request or a bug, message [LinkedIn](https://linkedin.com/in/anshumanatrey) (fastest), open an issue on the GitHub repo, or write through [atrey.dev](https://atrey.dev).

## Sibling actors

| Actor | What it searches |
|---|---|
| [Naukri Jobs Scraper](https://apify.com/anshumanatrey/naukri-jobs-search) | Every job on naukri.com, India's largest job board, with salary and experience |
| [Foundit Jobs Scraper](https://apify.com/anshumanatrey/foundit-jobs-search) | Every foundit site: India, the Gulf, Singapore, the Philippines and more |
| [Workday Jobs Scraper](https://apify.com/anshumanatrey/workday-job-search) | Jobs from every company on Workday (myworkdayjobs.com), searched live |
| [Greenhouse Jobs Scraper](https://apify.com/anshumanatrey/greenhouse-jobs-search) | Jobs from every company on Greenhouse, searched live |
| [Lever Jobs Scraper](https://apify.com/anshumanatrey/lever-jobs-search) | Jobs from 2,300+ companies on Lever (jobs.lever.co), searched live |
| [SmartRecruiters Jobs Scraper](https://apify.com/anshumanatrey/smartrecruiters-jobs-search) | Jobs from 2,900+ companies on SmartRecruiters, searched live |
| [Ashby Jobs Scraper](https://apify.com/anshumanatrey/ashby-jobs-search) | Jobs from every company on Ashby (jobs.ashbyhq.com), searched live |

## Documentation

- Apify Store: https://apify.com/anshumanatrey/efinancialcareers-jobs-search
- GitHub repo: https://github.com/AnshumanAtrey/efinancialcareers-jobs-search (MIT license, see [LICENSE](LICENSE))
- The engine behind it: https://github.com/AnshumanAtrey/ats-jobs-engine

## Last updated

2026-11-10 (version 1.0)
