"""eFinancialCareers Jobs Search: the shared job engine (github.com/AnshumanAtrey/ats-jobs-engine) on efinancialcareers.com, the job board for finance, banking and quant roles."""
import asyncio

from ats_jobs.engine import main

if __name__ == '__main__':
    asyncio.run(main('efinancialcareers'))
