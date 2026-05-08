##import requirements
import pandas as p


##import book file
book = p.read_csv('03_Library Systembook.csv')

##import customers file
customers = p.read_csv('03_Library SystemCustomers.csv')

##remove quote marks
book['Book checkout'] = book['Book checkout'].str.replace('"',"",regex=True)

##convert dates from string to datetime
book['Book Returned'] = p.to_datetime(book['Book Returned'], format='mixed')
book['Book checkout'] = p.to_datetime(book['Book checkout'], format='mixed',errors='coerce')
book = book[book['Book checkout'].notna()]

##remove lines where all entries are NaN
customers = customers.dropna(how="all")


##remove lines where all entries are NaN
book = book.dropna(how='all')


##remove lines where entries with a null books or customer id
book = book.dropna(subset=["Books","Customer ID"])

##print contents of files
print(customers)
print(book)



book['LoanLength'] = (book['Book checkout'] - book['Book Returned']).dt.days
book.loc[book['LoanLength'] <0, "LoanLength"] = 0



##export data to csv
book.to_csv("name.csv")

rows_processed = len(book)
job_name = "library_pipeline"


metrics = {
    "rows_processed":rows_processed,
    "status": "success",
    "job_name":job_name
}

metrics_df = p.DataFrame([metrics])

metrics_df.to_csv("metrics.csv")

print(metrics_df)









