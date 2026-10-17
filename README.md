```text
Receipt/
├── .gitignore          
├── README.md       # Setup, run commands, and notes
├── LICENSE         # Project license
├── src/            # All your active application code
├── docs/           # Documentation files 
├── data/           # Data files 
└── tests/          # Your unit tests
```

Experiment #1 (planned: 10/17/26)
1. Launch program &rarr; Browse images or b. Find by filename 
2. Select active receipt &rarr; show image while processing
3. Retrieve existing database record &rarr; Process as if new receipt entry else display saved info 
    * Saved info &rarr; View, Add, Edit, Delete, History
4. Check info before accepting it
    * Consider temp stash (resume function) if program exits accidentally
5. Persist changes &rarr; Add info into receipt records and audit log
    * Receipt records structure &rarr; Merchant, Transaction date, Subtotal, Tax, Total paid
    * Audit log structure &rarr; When (date/time), What (category), value change (prior, new state)
6. Return to receipt selection or exit